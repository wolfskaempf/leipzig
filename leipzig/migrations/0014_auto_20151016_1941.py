# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leipzig', '0013_auto_20151016_1934'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('committee_name', models.CharField(max_length=100)),
                ('committee_acronym', models.CharField(max_length=10)),
                ('topic', models.TextField()),
                ('image_link', models.URLField(null=True, blank=True)),
                ('rationales', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Topics',
        ),
    ]
