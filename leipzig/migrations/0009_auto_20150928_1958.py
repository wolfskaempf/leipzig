# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leipzig', '0008_auto_20150928_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='introduction',
            field=models.TextField(),
        ),
    ]
