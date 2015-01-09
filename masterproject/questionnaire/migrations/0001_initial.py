# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Password',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password_type', models.CharField(default=0, max_length=1)),
                ('sequence', models.CharField(default=0, max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('handsize', models.CharField(default=0, max_length=2)),
                ('screensize', models.CharField(default=0, max_length=2)),
                ('finger', models.CharField(default=0, max_length=1)),
                ('reading', models.CharField(default=0, max_length=2)),
                ('gender', models.CharField(default=0, max_length=1)),
                ('nationality', models.CharField(default=0, max_length=40)),
                ('used_ALP', models.CharField(default=0, max_length=1)),
                ('screen_lock', models.CharField(default=0, max_length=20)),
                ('mobileOS', models.CharField(default=0, max_length=20)),
                ('experience', models.CharField(default=0, max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='password',
            name='person',
            field=models.ForeignKey(to='questionnaire.Person'),
            preserve_default=True,
        ),
    ]
