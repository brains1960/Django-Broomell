# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-13 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.IntegerField(default=0)),
                ('unit', models.CharField(max_length=5)),
                ('trialsLeft', models.CommaSeparatedIntegerField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField(default=0)),
                ('normal', models.IntegerField(default=0)),
                ('confidence', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Trial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idNo', models.IntegerField(default=0)),
                ('week', models.IntegerField(default=0)),
                ('dates', models.CommaSeparatedIntegerField(max_length=200)),
                ('highs', models.CommaSeparatedIntegerField(max_length=200)),
                ('lows', models.CommaSeparatedIntegerField(max_length=200)),
                ('colour', models.CharField(max_length=8)),
            ],
        ),
    ]
