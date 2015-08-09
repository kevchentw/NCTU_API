# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='busschedule',
            name='semester',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='busschedule',
            name='vacation',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='busschedule',
            name='weekend',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='busschedule',
            name='workday',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='busroute',
            name='description_EN',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='busroute',
            name='description_ZH',
            field=models.TextField(blank=True, default=''),
        ),
    ]
