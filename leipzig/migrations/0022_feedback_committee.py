# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leipzig', '0021_auto_20151021_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='committee',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
