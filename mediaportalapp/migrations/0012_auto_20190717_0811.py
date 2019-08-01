# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-17 08:11
from __future__ import unicode_literals

from django.db import migrations, models
import mediaportalapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('mediaportalapp', '0011_auto_20190717_0755'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image_1',
            field=models.ImageField(default=b'', upload_to=mediaportalapp.models.generate_filename, verbose_name='\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f \u0442\u0440\u0435\u0442\u044c\u044f'),
        ),
        migrations.AddField(
            model_name='article',
            name='image_2',
            field=models.ImageField(default=b'', upload_to=mediaportalapp.models.generate_filename, verbose_name='\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f \u0447\u0435\u0442\u0432\u0435\u0440\u0442\u0430\u044f'),
        ),
        migrations.AddField(
            model_name='article',
            name='image_3',
            field=models.ImageField(default=b'', upload_to=mediaportalapp.models.generate_filename, verbose_name='\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f \u043f\u044f\u0442\u0430\u044f'),
        ),
        migrations.AddField(
            model_name='event',
            name='image_1',
            field=models.ImageField(default=b'', upload_to=mediaportalapp.models.generate_filename, verbose_name='\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f \u0442\u0440\u0435\u0442\u044c\u044f'),
        ),
        migrations.AddField(
            model_name='event',
            name='image_2',
            field=models.ImageField(default=b'', upload_to=mediaportalapp.models.generate_filename, verbose_name='\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f \u0447\u0435\u0442\u0432\u0435\u0440\u0442\u0430\u044f'),
        ),
        migrations.AddField(
            model_name='event',
            name='image_3',
            field=models.ImageField(default=b'', upload_to=mediaportalapp.models.generate_filename, verbose_name='\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f \u043f\u044f\u0442\u0430\u044f'),
        ),
        migrations.AddField(
            model_name='raiting',
            name='image_1',
            field=models.ImageField(default=b'', upload_to=mediaportalapp.models.generate_filename, verbose_name='\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f \u0442\u0440\u0435\u0442\u044c\u044f'),
        ),
        migrations.AddField(
            model_name='raiting',
            name='image_2',
            field=models.ImageField(default=b'', upload_to=mediaportalapp.models.generate_filename, verbose_name='\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f \u0447\u0435\u0442\u0432\u0435\u0440\u0442\u0430\u044f'),
        ),
        migrations.AddField(
            model_name='raiting',
            name='image_3',
            field=models.ImageField(default=b'', upload_to=mediaportalapp.models.generate_filename, verbose_name='\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f \u043f\u044f\u0442\u0430\u044f'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image_main',
            field=models.ImageField(default=b'', upload_to=mediaportalapp.models.generate_filename, verbose_name='\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f \u0433\u043b\u0430\u0432\u043d\u0430\u044f'),
        ),
        migrations.AlterField(
            model_name='event',
            name='image_main',
            field=models.ImageField(default=b'', upload_to=mediaportalapp.models.generate_filename, verbose_name='\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f \u0433\u043b\u0430\u0432\u043d\u0430\u044f'),
        ),
        migrations.AlterField(
            model_name='raiting',
            name='image_main',
            field=models.ImageField(default=b'', upload_to=mediaportalapp.models.generate_filename, verbose_name='\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f \u0433\u043b\u0430\u0432\u043d\u0430\u044f'),
        ),
    ]
