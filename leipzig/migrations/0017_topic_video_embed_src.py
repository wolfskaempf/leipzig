# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leipzig', '0016_auto_20151016_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='video_embed_src',
            field=models.TextField(blank=True),
        ),
    ]
