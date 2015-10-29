# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leipzig', '0023_feedback_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
    ]
