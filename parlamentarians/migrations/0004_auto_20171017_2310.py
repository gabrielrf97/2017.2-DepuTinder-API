# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 23:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parlamentarians', '0003_auto_20171013_0127'),
    ]

    operations = [
        migrations.AddField(
            model_name='parlamentarians',
            name='parlamentaryPhotoPath',
            field=models.CharField(default='https://i.imgur.com/ylkRU02.png', max_length=500),
        ),
        migrations.AlterField(
            model_name='parlamentarians',
            name='parlamentaryPoliticalParty',
            field=models.CharField(max_length=6),
        ),
    ]
