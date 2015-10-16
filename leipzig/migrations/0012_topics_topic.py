# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('leipzig', '0011_topics'),
    ]

    operations = [
        migrations.AddField(
            model_name='topics',
            name='topic',
            field=models.TextField(default=datetime.datetime(2015, 10, 16, 17, 30, 47, 755045, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
