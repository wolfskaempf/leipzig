# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leipzig', '0032_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app_title', models.CharField(default=b'Leipzig 2015', max_length=25)),
                ('app_colour', models.CharField(default=b'purple', max_length=50)),
            ],
        ),
    ]
