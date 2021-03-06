# Generated by Django 3.1.3 on 2020-11-22 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Miner', '0004_miner_repo_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labelname', models.CharField(max_length=10000, verbose_name='Label Name')),
                ('amount', models.IntegerField(verbose_name='Label Amount')),
                ('reponame', models.CharField(max_length=10000, verbose_name='Repo name')),
                ('associatedRepo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Miner.repositories')),
            ],
        ),
        migrations.CreateModel(
            name='IssuePerYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField(verbose_name='Year')),
                ('amountofissues', models.IntegerField(verbose_name='Issue Amount')),
                ('reponame', models.CharField(max_length=10000, verbose_name='Repo name')),
                ('associatedRepo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Miner.repositories')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventname', models.CharField(max_length=10000, verbose_name='Event Name')),
                ('amountOfEvent', models.IntegerField(verbose_name='Event amount')),
                ('reponame', models.CharField(max_length=10000, verbose_name='Repo name')),
                ('associatedRepo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Miner.repositories')),
            ],
        ),
    ]
