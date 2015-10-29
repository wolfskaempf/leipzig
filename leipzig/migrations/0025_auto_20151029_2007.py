# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leipzig', '0024_house_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='cite',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='house',
            name='quote',
            field=models.TextField(null=True, blank=True),
        ),
    ]
