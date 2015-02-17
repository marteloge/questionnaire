# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0012_auto_20150211_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='pattern_order',
            field=models.IntegerField(default=0, max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='finger',
            field=models.CharField(default=0, max_length=1, choices=[(b'default', b'0'), (b'Forefinger', b'F'), (b'Thumb', b'T')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='handsize',
            field=models.CharField(default=0, max_length=2, choices=[(b'default', b'0'), (b'Small', b'S'), (b'Medium', b'M'), (b'Large', b'L'), (b'XtraLarge', b'XL')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='reading',
            field=models.CharField(default=0, max_length=2, choices=[(b'default', b'0'), (b'L', b'Left'), (b'R', b'Right'), (b'T', b'Top')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='screensize',
            field=models.CharField(default=0, max_length=2, choices=[(b'default', b'0'), (b'Small', b'S'), (b'Medium', b'M'), (b'Large', b'L')]),
            preserve_default=True,
        ),
    ]
