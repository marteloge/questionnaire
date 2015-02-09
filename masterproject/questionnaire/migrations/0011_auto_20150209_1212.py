# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0010_auto_20150129_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='screenlock',
            field=models.CharField(default=0, max_length=20, choices=[(b'pattern', b'pattern'), (b'fingerprint', b'fingerprint'), (b'PIN', b'PIN'), (b'slide', b'slide'), (b'other', b'other'), (b'password', b'password')]),
            preserve_default=True,
        ),
    ]
