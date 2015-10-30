# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leipzig', '0026_auto_20151029_2305'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Photo',
            new_name='OfTheDay',
        ),
    ]
