# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0014_auto_20150217_0246'),
    ]

    operations = [
        migrations.AddField(
            model_name='password',
            name='time_used',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
