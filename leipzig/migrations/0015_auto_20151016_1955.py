# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('leipzig', '0014_auto_20151016_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='author',
            field=models.CharField(default=datetime.datetime(2015, 10, 16, 17, 55, 15, 300854, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='author_country',
            field=models.CharField(default=datetime.datetime(2015, 10, 16, 17, 55, 23, 127990, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
