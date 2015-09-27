# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('leipzig', '0004_auto_20150927_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='published_on',
            field=models.DateField(default=datetime.datetime(2015, 9, 27, 20, 11, 47, 276576, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
