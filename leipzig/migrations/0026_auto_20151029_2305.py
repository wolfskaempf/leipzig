# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leipzig', '0025_auto_20151029_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='cite',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
