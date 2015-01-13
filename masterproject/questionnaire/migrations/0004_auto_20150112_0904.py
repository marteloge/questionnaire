# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0003_auto_20150110_1809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='screen_lock',
            new_name='screenlock',
        ),
        migrations.AddField(
            model_name='person',
            name='use_screenlock',
            field=models.CharField(default=0, max_length=1),
            preserve_default=True,
        ),
    ]
