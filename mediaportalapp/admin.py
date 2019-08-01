# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Category, Article, UserAccount, Raiting, Event, VideoDownloading

import datetime

import calendar

from django.core.urlresolvers import reverse




 
 


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ['category', 'title', 'content', 'created']

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ['title', 'day', 'place', 'created']


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

class RaitingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ['title', 'content', 'author', 'created']

class VidoDownloadingAdmin(admin.ModelAdmin):
    list_display = ['title', 'notes', 'created']



admin.site.register(Category, CategoryAdmin)

admin.site.register(Article, ArticleAdmin)

admin.site.register(UserAccount)

admin.site.register(Raiting, RaitingAdmin)

admin.site.register(Event, EventAdmin)

admin.site.register(VideoDownloading)

