# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusProvider',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name_ZH', models.CharField(max_length=50)),
                ('name_EN', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BusRoute',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name_ZH', models.CharField(max_length=50)),
                ('name_EN', models.CharField(max_length=50)),
                ('description_ZH', models.TextField(default='')),
                ('description_EN', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BusSchedule',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('time', models.TimeField()),
                ('description_ZH', models.TextField(default='')),
                ('description_EN', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('route', models.ForeignKey(related_name='schedule_route', to='Bus.BusRoute')),
            ],
        ),
        migrations.CreateModel(
            name='BusStop',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name_ZH', models.CharField(max_length=50)),
                ('name_EN', models.CharField(max_length=50)),
                ('description_ZH', models.TextField(default='')),
                ('description_EN', models.TextField(default='')),
                ('lat', models.FloatField(default=0)),
                ('lon', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='busschedule',
            name='stop',
            field=models.ForeignKey(related_name='schedule_stop', to='Bus.BusStop'),
        ),
        migrations.AddField(
            model_name='busroute',
            name='departure',
            field=models.ForeignKey(related_name='route_departure', to='Bus.BusStop'),
        ),
        migrations.AddField(
            model_name='busroute',
            name='destination',
            field=models.ForeignKey(related_name='route_destination', to='Bus.BusStop'),
        ),
        migrations.AddField(
            model_name='busroute',
            name='provider',
            field=models.ForeignKey(related_name='route_provider', to='Bus.BusProvider'),
        ),
    ]
