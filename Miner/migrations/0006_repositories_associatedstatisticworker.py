# Generated by Django 3.1.3 on 2020-11-22 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Miner', '0005_event_issueperyear_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='repositories',
            name='associatedStatisticWorker',
            field=models.CharField(default=1, max_length=10000, verbose_name='Task id'),
            preserve_default=False,
        ),
    ]
