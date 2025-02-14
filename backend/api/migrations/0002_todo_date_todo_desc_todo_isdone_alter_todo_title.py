# Generated by Django 5.0.1 on 2024-07-15 19:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='todo',
            name='desc',
            field=models.CharField(default='default description', max_length=200),
        ),
        migrations.AddField(
            model_name='todo',
            name='isDone',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(default='task', max_length=50),
        ),
    ]
