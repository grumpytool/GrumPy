from django.db import models


class Token(models.Model):
    tokenname = models.CharField('Name', max_length=100, unique=True)
    token = models.CharField('Token', max_length=100)

    def __str__(self):
        return self.tokenname


class Miner(models.Model):
    minername = models.CharField('Name', max_length=100, unique=True)  # Miner Name
    repoamount = models.IntegerField('Repo amount')  # Repo amount of listed repo
    minedamount = models.IntegerField('Mined Repo Amount')  # Mined amount
    minerstatus = models.CharField('Status', max_length=100)  # Miner task status
    minertaskid = models.CharField('Task id', max_length=100)  # Asynchronous task id
    tokenassociated = models.ForeignKey(Token, on_delete=models.CASCADE)
    repo_list = models.TextField('Repositories list')
    statisticstaskid = models.CharField('Task id', max_length=100)  # Asynchronous task id

    def __str__(self):
        return self.minername


class Repositories(models.Model):
    reponame = models.CharField('Name', max_length=100)  # Repo Name
    activitystatus = models.CharField('Status', max_length=100)  # Activity status - Waiting, mining, mined
    currentminingissue = models.IntegerField('Current mining issue', null=True)  # Current mined issue
    lastissuenumber = models.IntegerField('Final issue', null=True)  # Last issue value
    firstissuenumber = models.IntegerField('First issue', null=True)  # First issue value
    associatedMiner = models.CharField('Miner name', max_length=10000,)
    associatedStatisticWorker = models.CharField('Task id', max_length=10000, null=True)
    openIssues = models.IntegerField('Open issue', null=True)
    closedIssues = models.IntegerField('Closed issue', null=True)
    amountOpenComments = models.IntegerField('Open issue comments', null=True)
    amountClosedComments = models.IntegerField('Closed issue comments', null=True)
    amountOpenReactions = models.IntegerField('Open issue reactions', null=True)
    amountClosedReactions = models.IntegerField('Closed issue reactions', null=True)
    amountMinedIssues = models.IntegerField('Closed issue reactions', null=True)

    def __str__(self):
        return self.reponame

class Label(models.Model):
    labelname = models.CharField('Label Name', max_length=10000) # Label name
    amount = models.IntegerField('Label Amount') # Amount
    reponame = models.CharField('Repo name', max_length=10000) # Repository name
    associatedRepo = models.ForeignKey(Repositories, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.labelname

class IssuePerYear(models.Model):
    year = models.DateField('Year') # Year
    amountofissues = models.IntegerField('Issue Amount') # Amount of issues
    reponame = models.CharField('Repo name', max_length=10000)  # Repository name
    associatedRepo = models.ForeignKey(Repositories, on_delete=models.CASCADE, null=True) # Repository fk

    def __str__(self):
        return self.year

class Event(models.Model):
    eventname_1 = models.CharField('1 Event Name', max_length=10000) # Event name
    amountOfEvent_1 = models.IntegerField('1 Event amount')

    eventname_2 = models.CharField('2 Event Name', max_length=10000)  # Event name
    amountOfEvent_2 = models.IntegerField('2 Second Event amount')

    eventname_3 = models.CharField('3 Event Name', max_length=10000)  # Event name
    amountOfEvent_3 = models.IntegerField('3 Second Event amount')

    eventname_4 = models.CharField('4 Event Name', max_length=10000)  # Event name
    amountOfEvent_4 = models.IntegerField('4 Event amount')

    eventname_5 = models.CharField('5 Event Name', max_length=10000)  # Event name
    amountOfEvent_5 = models.IntegerField('5 Event amount')


    reponame = models.CharField('Repo name', max_length=10000)  # Repository name
    associatedRepo = models.ForeignKey(Repositories, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.eventname

class Reactions(models.Model):

    like = models.IntegerField('Like')
    heart = models.IntegerField('Heart')
    hooray = models.IntegerField('Horray')
    confused = models.IntegerField('Confused')
    deslike = models.IntegerField('Deslike')
    laught = models.IntegerField('Laught')
    rocket = models.IntegerField('Rocket')
    eyes = models.IntegerField('Eyes')

    reponame = models.CharField('Repo name', max_length=10000)

    def __str__(self):
        return self.reponame+' reactions'