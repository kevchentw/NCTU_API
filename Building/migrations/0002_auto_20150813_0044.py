# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Building', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='classroom_code',
            field=models.CharField(max_length=5),
        ),
    ]
