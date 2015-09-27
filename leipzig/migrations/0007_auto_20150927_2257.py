# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leipzig', '0006_auto_20150927_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published_on',
            field=models.DateTimeField(),
        ),
    ]
