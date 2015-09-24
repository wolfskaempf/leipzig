# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leipzig', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image_link',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='introduction',
            field=models.TextField(default='no', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='media_link',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='video_embed_code',
            field=models.TextField(default='h', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='committee',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(default='h', max_length=50, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='spotify_link',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='video_link',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='songwish',
            name='spotify_link',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='songwish',
            name='video_link',
            field=models.URLField(null=True, blank=True),
        ),
    ]
