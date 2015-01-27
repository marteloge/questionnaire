# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0008_password_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='experience',
            field=models.CharField(default=0, max_length=1, choices=[(b'Y', b'Yes'), (b'N', b'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='finger',
            field=models.CharField(default=0, max_length=1, choices=[(b'F', b'Forefinger'), (b'T', b'Thumb')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(default=0, max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='handedness',
            field=models.CharField(default=0, max_length=1, choices=[(b'L', b'Left'), (b'R', b'Right')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='handsize',
            field=models.CharField(default=0, max_length=2, choices=[(b'S', b'Small'), (b'M', b'Medium'), (b'L', b'Large'), (b'XL', b'XtraLarge')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='mobileOS',
            field=models.CharField(default=0, max_length=20, choices=[(b'android', b'Anroid'), (b'ios', b'iOS'), (b'windows', b'Windows'), (b'blackberry', b'Blackberry'), (b'no_android', b'No Android'), (b'no_ios', b'No iOS'), (b'no_windows', b'No Windows'), (b'blackberry', b'No Blackberry'), (b'unknown_android', b'Unknown Android'), (b'unknown_ios', b'Unknown iOS'), (b'unknown_windows', b'Unknown Windows'), (b'unknown_blackberry', b'Unknown Blackberry'), (b'other', b'Other')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='reading',
            field=models.CharField(default=0, max_length=2, choices=[(b'L', b'Left'), (b'R', b'Right'), (b'T', b'Top')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='screenlock',
            field=models.CharField(default=0, max_length=20, choices=[(b'pattern', b'pattern'), (b'fingerprint', b'fingerprint'), (b'PIN', b'PIN'), (b'slide', b'slide'), (b'other', b'other')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='screensize',
            field=models.CharField(default=0, max_length=2, choices=[(b'S', b'Small'), (b'M', b'Medium'), (b'L', b'Large')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='use_screenlock',
            field=models.CharField(default=0, max_length=1, choices=[(b'Y', b'Yes'), (b'N', b'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='used_ALP',
            field=models.CharField(default=0, max_length=1, choices=[(b'Y', b'Yes'), (b'N', b'No')]),
            preserve_default=True,
        ),
    ]
