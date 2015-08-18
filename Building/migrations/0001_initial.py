# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name_ZH', models.CharField(max_length=50)),
                ('name_EN', models.CharField(max_length=50)),
                ('classroom_code', models.CharField(max_length=3)),
                ('lat', models.FloatField(default=0)),
                ('lon', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name_ZH', models.CharField(max_length=50)),
                ('name_EN', models.CharField(max_length=50)),
                ('lat', models.FloatField(default=0)),
                ('lon', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='building',
            name='campus',
            field=models.ForeignKey(related_name='building_campus', to='Building.Campus'),
        ),
    ]
