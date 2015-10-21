# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('leipzig', '0022_feedback_committee'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 21, 15, 33, 8, 10824, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
