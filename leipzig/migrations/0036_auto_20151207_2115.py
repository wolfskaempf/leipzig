# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-07 20:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leipzig', '0035_auto_20151207_2101'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OfTheDay',
            new_name='FeaturedItem',
        ),
    ]
