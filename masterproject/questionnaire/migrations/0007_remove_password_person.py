# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0006_person_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='password',
            name='person',
        ),
    ]
