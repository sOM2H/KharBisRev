# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-02 15:28
from __future__ import unicode_literals

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mediaportalapp', '0018_auto_20190727_0322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articleotrasli',
            name='category',
        ),
        migrations.RemoveField(
            model_name='articleotrasli',
            name='users_reaction',
        ),
        migrations.AlterField(
            model_name='videodownloading',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, help_text='\u0417\u0430\u0445\u043e\u0434\u0438\u043c \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0443 \u0432\u0438\u0434\u0435\u043e-\u041f\u043e\u0434\u0435\u043b\u0438\u0442\u044c\u0441\u044f-\u0412\u0441\u0442\u0440\u043e\u0438\u0442\u044c-\u041a\u043e\u043f\u0438\u0440\u0443\u0435\u043c link, \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u0449\u0438\u0439 \u0441\u0442\u0440\u043e\u043a\u0443 embeded', verbose_name='\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0432\u0438\u0434\u0435\u043e'),
        ),
        migrations.DeleteModel(
            name='ArticleOtrasli',
        ),
        migrations.DeleteModel(
            name='CategoryOtrasli',
        ),
    ]
