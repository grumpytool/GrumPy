from time import sleep
from venv import logger

import requests
from requests import exceptions
from github import Github, GithubException
from celery import shared_task
from celery_progress.backend import ProgressRecorder
from Miner.Activity_performance.MinersClass import MinerClass
from Miner.Activity_performance.RequestVerificationClass import VerificationClass
from Miner.Activity_performance.MinersClass import MinerClass
from Miner.Issues_Persistence.Connections import Connections
from celery.contrib.abortable import AbortableTask

from Miner.models import Miner, Token, Repositories


@shared_task(bind=True, base=AbortableTask)
def test_worker(self, NAME, miner_id):
    progress_recorder = ProgressRecorder(self)
    i = 0
    total = 50
    miner = Miner.objects.get(id=miner_id)
    print(miner.repo_list.split())

    while (i < 20):
        if self.is_aborted():
            return 'Task aborted'
        string = str(NAME) + ' Testing task - Downloading'
        progress_recorder.set_progress(i + 1, total, string)
        sleep(3)
        i += 1

    Miner.objects.filter(pk=miner_id).update(minerstatus='Finished')
    return str(NAME) + 'Testing task - Task finished'


@shared_task(bind=True, base=AbortableTask)
def mining_worker(self, miner_id):
    progress_recorder = ProgressRecorder(self)
    miner = Miner.objects.get(id=miner_id)
    token = Token.objects.get(id=miner.tokenassociated_id)
    print(str(token.token))
    authentication = Github(str(token.token))
    connectionToDB = Connections()
    connectionToDB.openConnectionToDB()
    repo_count = 0
    print(str(miner.repo_list))

    repositories_list = miner.repo_list.split(' ')
    repositories_list.remove('')
    print(len(repositories_list))

    for repo in repositories_list:
        print(repo)
        if self.is_aborted():
            return 'Task aborted'

        REPO = Repositories.objects.get(reponame=repo)
        Repositories.objects.filter(pk=REPO.id).update(activitystatus="Mining")

        string = 'Mining repo ' + str(repo) + ' (' + str(repo_count) + '/' + str(len(repositories_list)) + ')'
        repo_count += 1
        progress_recorder.set_progress(repo_count, len(repositories_list), string)

        first_issue = last_issue = 0

        ISSUE_extrac = MinerClass(authentication, 1800, 5, repo)

        last_issue = ISSUE_extrac.getLastIssue()
        #print(str(last_issue))

        REPO = Repositories.objects.get(reponame=repo)
        Repositories.objects.filter(pk=REPO.id).update(firstissuenumber=int(first_issue))
        Repositories.objects.filter(pk=REPO.id).update(lastissuenumber=int(last_issue))

        # flags -> 2 Continue process
        #       -> 0 Process finished
        #       -> 1 Process error

        flag = False

        if (last_issue is not None):
            while (flag == False):

                VerificationClass(authentication, 1800, 5)
                if self.is_aborted():
                    connectionToDB.closeConnectionToDB()
                    return 'Task aborted'
                if (connectionToDB.verifyCollectionInDatabase(repo) == True):
                    try:
                        first_issue = connectionToDB.verifyLastIssueInCollection(repo)
                    except:
                        print('Error finding the first repo issue ' + str(repo))
                        flag = 1
                        exit(0)

                try:
                    VerificationClass(authentication, 1800, 5)
                    if self.is_aborted():
                        connectionToDB.closeConnectionToDB()
                        return 'Task aborted'

                    VerificationClass(authentication, 1800, 5)

                    if self.is_aborted():
                        connectionToDB.closeConnectionToDB()
                        return 'Task aborted'

                    while (first_issue <= last_issue):
                        #print('Entrando aqui!')
                        if self.is_aborted():
                            connectionToDB.closeConnectionToDB()
                            return 'Task aborted'

                        VerificationClass(authentication, 1800, 5)
                        issue = ISSUE_extrac.getIssue(first_issue)
                        if (issue is not None and issue.number is not None):
                            if (connectionToDB.findIssue(first_issue, repo) is None):
                                if self.is_aborted():
                                    return 'Task aborted'


                                issue_formatted = ISSUE_extrac.issue_mining(issue)
                                #string = str(first_issue)+'/'+str(last_issue) + ' issues of '+str(repo)+' in '+str(repo_count) + '/'+str(len(repositories_list)) + ' repositories'
                                #progress_recorder.set_progress(repo_count, len(repositories_list), string)

                                print(self.is_aborted())
                                if self.is_aborted():
                                    print('Task aborted')
                                    exit(0)
                                connectionToDB.saveJsonAsIssue(issue_formatted, repo)

                        first_issue += 1

                        REPO = Repositories.objects.get(reponame=repo)
                        Repositories.objects.filter(pk=REPO.id).update(firstissuenumber=int(first_issue))

                        print('First Issue '+str(first_issue))
                        print('Last Issue ' + str(last_issue))

                        if (first_issue == last_issue):
                            flag = True

                except requests.exceptions.ReadTimeout as aes:
                    warning_string = 'ReadTimeout error in event mining'
                    Miner.objects.filter(pk=miner_id).update(minerstatus=warning_string)
                except requests.exceptions.ConnectionError as aes:
                    warning_string = 'Connection error in event mining'
                    Miner.objects.filter(pk=miner_id).update(minerstatus=warning_string)
                except GithubException as d:
                    if (d.status == 403):
                        warning_string = 'Request limit achieved in event mining'
                        Miner.objects.filter(pk=miner_id).update(minerstatus=warning_string)

        repo_count += 1
        REPO = Repositories.objects.get(reponame=repo)
        Repositories.objects.filter(pk=REPO.id).update(activitystatus="Finished")

        #REPO = Repositories.objects.get(reponame=repo)
        #Repositories.objects.filter(pk=REPO.id).update(activitystatus="Finished")

    connectionToDB.closeConnectionToDB()
    sucess_string = 'Finished! ' + str(len(repositories_list)) + ' repositories mined.'
    Miner.objects.filter(pk=miner_id).update(minerstatus=sucess_string)

    return sucess_string
