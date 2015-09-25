# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('leipzig', '0002_auto_20150924_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='update',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 24, 14, 34, 34, 979167, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
