# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 22:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leipzig', '0044_auto_20160516_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='navbarentry',
            name='blank',
            field=models.BooleanField(default=True),
        ),
    ]
