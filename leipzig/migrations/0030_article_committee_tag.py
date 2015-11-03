# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leipzig', '0029_auto_20151030_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='committee_tag',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
