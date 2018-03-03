# Generated by Django 2.0.2 on 2018-03-02 11:25

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0005_auto_20180204_2014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='globaldata',
            name='trialsLeft',
        ),
        migrations.AddField(
            model_name='participants',
            name='trialsLeft',
            field=models.CharField(default=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52), max_length=200, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participants',
            name='trialsPassed',
            field=models.CharField(default=[], max_length=200, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')]),
            preserve_default=False,
        ),
    ]
