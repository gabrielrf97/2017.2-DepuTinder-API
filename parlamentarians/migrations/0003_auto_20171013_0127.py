# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 01:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parlamentarians', '0002_auto_20171011_2031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parlamentarians',
            old_name='nome',
            new_name='parlamentaryName',
        ),
        migrations.RenameField(
            model_name='parlamentarians',
            old_name='partido',
            new_name='parlamentaryPoliticalParty',
        ),
        migrations.RenameField(
            model_name='parlamentarians',
            old_name='uf',
            new_name='parlamentaryUF',
        ),
    ]
