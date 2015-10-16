# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leipzig', '0010_house_image_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('acronym', models.CharField(max_length=10)),
                ('image_link', models.URLField(null=True, blank=True)),
                ('rationales', models.TextField()),
            ],
        ),
    ]
