# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        ('questionnaire', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='id',
        ),
        migrations.AddField(
            model_name='person',
            name='session',
            field=models.OneToOneField(primary_key=True, default=1, serialize=False, to='sessions.Session'),
            preserve_default=False,
        ),
    ]
