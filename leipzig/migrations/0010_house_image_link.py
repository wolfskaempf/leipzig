# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leipzig', '0009_auto_20150928_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='image_link',
            field=models.URLField(null=True, blank=True),
        ),
    ]
