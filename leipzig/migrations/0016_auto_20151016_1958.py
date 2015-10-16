# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leipzig', '0015_auto_20151016_1955'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='rationales',
            new_name='rationale',
        ),
    ]
