# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-19 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediaportalapp', '0016_auto_20190719_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='place',
            field=models.CharField(default=b'', max_length=120, verbose_name='\u041c\u0435\u0441\u0442\u043e'),
        ),
    ]