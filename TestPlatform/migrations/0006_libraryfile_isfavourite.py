# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-06 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestPlatform', '0005_libraryfile_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='libraryfile',
            name='isfavourite',
            field=models.IntegerField(default=0, verbose_name='是否本人上传'),
            preserve_default=False,
        ),
    ]