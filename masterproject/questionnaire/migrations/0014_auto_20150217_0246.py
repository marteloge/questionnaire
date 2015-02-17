# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0013_auto_20150216_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='finger',
            field=models.CharField(default=0, max_length=1, choices=[(b'0', b'default'), (b'F', b'Forefinger'), (b'T', b'Thumb')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='handsize',
            field=models.CharField(default=0, max_length=2, choices=[(b'0', b'default'), (b'S', b'Small'), (b'M', b'Medium'), (b'L', b'Large'), (b'XL', b'XtraLarge')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='reading',
            field=models.CharField(default=0, max_length=2, choices=[(b'0', b'default'), (b'L', b'Left'), (b'R', b'Right'), (b'T', b'Top')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='screensize',
            field=models.CharField(default=0, max_length=2, choices=[(b'0', b'default'), (b'S', b'Small'), (b'M', b'Medium'), (b'L', b'Large')]),
            preserve_default=True,
        ),
    ]
