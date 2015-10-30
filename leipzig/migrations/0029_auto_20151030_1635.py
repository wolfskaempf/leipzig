# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leipzig', '0028_auto_20151030_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='oftheday',
            name='external_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='oftheday',
            name='object_type',
            field=models.CharField(default=b'Photo', max_length=10),
        ),
    ]
