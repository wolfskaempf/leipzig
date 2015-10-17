# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('leipzig', '0019_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 17, 13, 20, 23, 990229, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
