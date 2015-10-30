# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leipzig', '0027_auto_20151030_1632'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oftheday',
            old_name='link',
            new_name='image_link',
        ),
    ]
