# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-19 05:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_auto_20180719_0530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forecast',
            name='verified',
        ),
        migrations.DeleteModel(
            name='Verified',
        ),
    ]
