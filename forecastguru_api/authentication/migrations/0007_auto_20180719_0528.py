# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-19 05:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_auto_20180718_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Approved',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ['-name'],
                'verbose_name_plural': 'Approved',
            },
        ),
        migrations.CreateModel(
            name='Betting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bet_for', models.IntegerField(default=0)),
                ('bet_against', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-bet_for'],
                'verbose_name_plural': 'Points In Play',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('identifier', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-name'],
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='ForeCast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=1000)),
                ('tags', models.CharField(blank=True, max_length=1000, null=True)),
                ('expire', models.DateTimeField()),
                ('created', models.DateField(auto_now=True)),
                ('approved', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.Approved')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.Category')),
            ],
            options={
                'ordering': ['-category'],
                'verbose_name_plural': 'FORECAST',
            },
        ),
        migrations.CreateModel(
            name='Private',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ['-name'],
                'verbose_name_plural': 'Private',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['-name'],
                'verbose_name_plural': 'Status',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('image', models.URLField(blank=True, null=True)),
                ('identifier', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.Category')),
            ],
            options={
                'ordering': ['-name'],
                'verbose_name_plural': 'Sub-Category',
            },
        ),
        migrations.CreateModel(
            name='Verified',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ['-name'],
                'verbose_name_plural': 'Verified',
            },
        ),
        migrations.CreateModel(
            name='Winning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ['-name'],
                'verbose_name_plural': 'Winning',
            },
        ),
        migrations.AlterField(
            model_name='authentication',
            name='facebook_id',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='authentication',
            name='last_login',
            field=models.DateField(default=datetime.date(2018, 7, 19)),
        ),
        migrations.AddField(
            model_name='forecast',
            name='private',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.Private'),
        ),
        migrations.AddField(
            model_name='forecast',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.Status'),
        ),
        migrations.AddField(
            model_name='forecast',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.SubCategory'),
        ),
        migrations.AddField(
            model_name='forecast',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.Authentication'),
        ),
        migrations.AddField(
            model_name='forecast',
            name='verified',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.Verified'),
        ),
        migrations.AddField(
            model_name='forecast',
            name='won',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.Winning'),
        ),
        migrations.AddField(
            model_name='betting',
            name='forecast',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.ForeCast'),
        ),
        migrations.AddField(
            model_name='betting',
            name='users',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.Authentication'),
        ),
    ]
