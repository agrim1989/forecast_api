# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-23 07:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0016_auto_20180723_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authentication',
            name='facebook_id',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]