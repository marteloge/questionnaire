# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0004_auto_20150112_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='handedness',
            field=models.CharField(default=0, max_length=1),
            preserve_default=True,
        ),
    ]
