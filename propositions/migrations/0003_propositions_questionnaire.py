# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-07 01:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0001_initial'),
        ('propositions', '0002_remove_propositions_propositionid'),
    ]

    operations = [
        migrations.AddField(
            model_name='propositions',
            name='questionnaire',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='question', to='questionnaire.Questionnaire'),
        ),
    ]