# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0002_auto_20150110_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='session',
        ),
        migrations.AddField(
            model_name='person',
            name='session_id',
            field=models.CharField(default=1, max_length=40, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
