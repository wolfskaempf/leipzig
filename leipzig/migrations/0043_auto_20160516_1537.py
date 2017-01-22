# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-16 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leipzig', '0042_auto_20160508_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image_link',
        ),
        migrations.RemoveField(
            model_name='featureditem',
            name='image_link',
        ),
        migrations.RemoveField(
            model_name='teammember',
            name='image_link',
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to=b'article_pictures/'),
        ),
        migrations.AddField(
            model_name='featureditem',
            name='image',
            field=models.ImageField(blank=True, upload_to=b'featured_pictures/'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='image',
            field=models.ImageField(blank=True, upload_to=b'article_pictures/'),
        ),
    ]