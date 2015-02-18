# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0016_auto_20150217_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='finger',
            field=models.CharField(default=0, max_length=1, choices=[(b'0', b'default'), (b'F', b'Forefinger'), (b'T', b'Thumb'), (b'O', b'Other')]),
            preserve_default=True,
        ),
    ]
