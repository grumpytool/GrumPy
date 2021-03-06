# Generated by Django 3.1.3 on 2020-11-22 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Miner', '0014_auto_20201122_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='amountOfEvent',
        ),
        migrations.RemoveField(
            model_name='event',
            name='eventname',
        ),
        migrations.AddField(
            model_name='event',
            name='amountOfEvent_1',
            field=models.IntegerField(default=1, verbose_name='1 Event amount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='amountOfEvent_2',
            field=models.IntegerField(default=1, verbose_name='2 Second Event amount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='amountOfEvent_3',
            field=models.IntegerField(default=1, verbose_name='3 Second Event amount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='amountOfEvent_4',
            field=models.IntegerField(default=1, verbose_name='4 Event amount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='amountOfEvent_5',
            field=models.IntegerField(default=1, verbose_name='5 Event amount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='eventname_1',
            field=models.CharField(default=1, max_length=10000, verbose_name='1 Event Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='eventname_2',
            field=models.CharField(default=1, max_length=10000, verbose_name='2 Event Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='eventname_3',
            field=models.CharField(default=1, max_length=10000, verbose_name='3 Event Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='eventname_4',
            field=models.CharField(default=1, max_length=10000, verbose_name='4 Event Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='eventname_5',
            field=models.CharField(default=1, max_length=10000, verbose_name='5 Event Name'),
            preserve_default=False,
        ),
    ]
