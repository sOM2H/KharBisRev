# -- coding: utf-8 --
from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from embed_video.fields import EmbedVideoField
from django.utils import timezone




class Category(models.Model):
    
    name = models.CharField(u'Название',max_length=100)
    
    slug = models.SlugField(u'Ссылка')
    
    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'

class CategoryOtrasli(models.Model):
    
    name = models.CharField(u'Название',max_length=100)
    
    slug = models.SlugField(u'Ссылка')
    
    def __unicode__(self):
        return self.name

    #def get_absolute_url(self):
        #return reverse('category_detail', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'


def generate_filename(instance, filename):
    filename = instance.slug + '.jpg'
    return "{0}/{1}".format(instance.slug, filename)


class Article(models.Model):
    category = models.ForeignKey(Category,verbose_name=u"Категория",on_delete=models.CASCADE)
    title = models.CharField(u'Заголовок',max_length=120)
    slug = models.SlugField(u'Ссылка')
    image = models.ImageField(u'Фотография',upload_to=generate_filename)
    content = models.TextField(u'Контент')
    author = models.TextField(u'Автор',default='')
    like = models.PositiveIntegerField(u'Лайки',default=0)
    users_reaction = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=u'Кто отреагировал на пост', blank=True)
    created = models.DateTimeField(default=timezone.now)
     
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'category': self.category.slug, 'slug': self.slug})
    
    class Meta:
        verbose_name = u'Пост'
        verbose_name_plural = u'Посты'

class ArticleOtrasli(models.Model):
    category = models.ForeignKey(CategoryOtrasli, verbose_name=u"Категория",on_delete=models.CASCADE)
    title = models.CharField(u'Заголовок',max_length=120)
    slug = models.SlugField(u'Ссылка')
    image = models.ImageField(u'Фотография',upload_to=generate_filename)
    content = models.TextField(u'Контент')
    author = models.TextField(u'Автор',default='')
    like = models.PositiveIntegerField(u'Лайки',default=0)
    users_reaction = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=u'Кто отреагировал на пост', blank=True)
    created = models.DateTimeField(default=timezone.now)


class UserAccount(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=u'Пользователь', on_delete=models.CASCADE)
    email = models.EmailField(u'Эмейл')
    favorite_articles = models.ManyToManyField(Article, verbose_name=u'Любимые статьи', blank=True)

    def __unicode__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('account_view', kwargs={'user': self.user.username})
    
    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'



class Raiting(models.Model):
    title = models.CharField(u'Заголовок',max_length=200)
    slug = models.SlugField(u'Ссылка',default='')
    content = models.TextField(u'Контент')
    author = models.TextField(u'Автор',default='')
    like = models.PositiveIntegerField(u'Лайки',default=0)
    image = models.ImageField(u'Фотография',upload_to=generate_filename, default='')
    created = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = u'Рейтинг'
        verbose_name_plural = u'Рейтинги'
    
    def get_absolute_url(self):
        return reverse('raiting_detail', kwargs={'slug': self.slug})


class Event(models.Model):
    title = models.CharField(u'Заголовок',max_length=120, default='')
    slug = models.SlugField(u'Ссылка', default='')
    day = models.DateField(u'День события', help_text=u'День события')
    start_time = models.TimeField(u'Начало', help_text=u'Начало')
    end_time = models.TimeField(u'Конец', help_text=u'Конец')
    place = models.CharField(u'Место',max_length=120, default='')
    image = models.ImageField(u'Фотография',upload_to=generate_filename, default='')
    notes = models.TextField(u'Заметки', help_text=u'Заметки', blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)

    
    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Событие'
        verbose_name_plural = u'События'

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'slug': self.slug})


class VideoDownloading(models.Model):
    title = models.CharField(u'Заголовок',max_length=120, default='')
    url = models.CharField(u'Ссылка', max_length=200, help_text=u'Вводить только URL-страницы', default='')
    notes = models.TextField(u'Заметки', help_text=u'Заметки', blank=True, null=True)
    video = EmbedVideoField(u'Загрузить видео', blank=True, help_text=u'Заходим на страницу видео-Поделиться-Встроить-Копируем link, содержащий строку embeded')
    created = models.DateTimeField(default=timezone.now)


    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Видеообзор'
        verbose_name_plural = u'Видеообзоры'
