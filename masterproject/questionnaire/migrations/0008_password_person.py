# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0007_remove_password_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='password',
            name='person',
            field=models.ForeignKey(default=1, to='questionnaire.Person'),
            preserve_default=False,
        ),
    ]
