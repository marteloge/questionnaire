# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0015_password_time_used'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='password',
            name='time_used',
        ),
        migrations.AddField(
            model_name='password',
            name='time',
            field=models.IntegerField(default=0, max_length=40),
            preserve_default=True,
        ),
    ]
