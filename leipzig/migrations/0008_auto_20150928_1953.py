# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leipzig', '0007_auto_20150927_2257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='video_embed_code',
            new_name='video_embed_src',
        ),
    ]
