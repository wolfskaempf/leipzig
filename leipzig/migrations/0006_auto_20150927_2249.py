# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leipzig', '0005_article_published_on'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='media_link',
            new_name='external_link',
        ),
    ]
