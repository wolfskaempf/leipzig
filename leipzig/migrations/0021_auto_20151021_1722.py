# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leipzig', '0020_comment_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='author',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='author_country',
        ),
    ]
