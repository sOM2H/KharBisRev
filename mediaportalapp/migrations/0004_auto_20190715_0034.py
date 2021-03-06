# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-15 00:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediaportalapp', '0003_auto_20190714_2219'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Scheduling', 'verbose_name_plural': 'Scheduling'},
        ),
        migrations.RemoveField(
            model_name='event',
            name='description',
        ),
        migrations.RemoveField(
            model_name='event',
            name='title',
        ),
        migrations.AddField(
            model_name='event',
            name='notes',
            field=models.TextField(blank=True, help_text='Textual Notes', null=True, verbose_name='Textual Notes'),
        ),
        migrations.AlterField(
            model_name='event',
            name='day',
            field=models.DateField(help_text='Day of the event', verbose_name='Day of the event'),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(help_text='Final time', verbose_name='Final time'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(help_text='Starting time', verbose_name='Starting time'),
        ),
    ]
