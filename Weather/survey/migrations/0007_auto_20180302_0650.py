# Generated by Django 2.0.2 on 2018-03-02 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_auto_20180302_0625'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trial',
            old_name='dates',
            new_name='temps',
        ),
        migrations.RemoveField(
            model_name='trial',
            name='highs',
        ),
        migrations.RemoveField(
            model_name='trial',
            name='lows',
        ),
    ]
