# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leipzig', '0031_article_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('button_text', models.CharField(max_length=100)),
                ('link', models.URLField()),
                ('article', models.ForeignKey(to='leipzig.Article')),
            ],
        ),
    ]
