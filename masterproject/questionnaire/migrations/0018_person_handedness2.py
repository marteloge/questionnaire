# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0017_auto_20150218_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='handedness2',
            field=models.CharField(default=0, max_length=1, choices=[(b'0', b'default'), (b'L', b'Left'), (b'R', b'Right')]),
            preserve_default=True,
        ),
    ]
