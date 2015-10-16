# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leipzig', '0017_topic_video_embed_src'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='team',
            field=models.CharField(default='MT', max_length=b'2', choices=[(b'OT', b'Organising Team'), (b'MT', b'Media Team')]),
            preserve_default=False,
        ),
    ]
