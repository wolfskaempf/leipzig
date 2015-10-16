# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leipzig', '0012_topics_topic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topics',
            old_name='acronym',
            new_name='committee_acronym',
        ),
        migrations.RenameField(
            model_name='topics',
            old_name='name',
            new_name='committee_name',
        ),
    ]
