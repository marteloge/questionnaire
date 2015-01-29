# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0009_auto_20150127_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='actual_screenheight',
            field=models.IntegerField(default=0, max_length=4),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='actual_screenwidth',
            field=models.IntegerField(default=0, max_length=4),
            preserve_default=True,
        ),
    ]
