# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-09 00:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Libry', '0006_auto_20151209_0356'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='want2read',
            field=models.ManyToManyField(to='Libry.Writing'),
        ),
    ]
