# -- coding: utf-8 --
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from .mixin import CategoryAndArticlesListMixin, CategoryAndEventListMixin
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Article, Category, UserAccount, Raiting, Event, VideoDownloading
from django.http import JsonResponse
from django.views import View
from .forms import RegistrationForm, LoginForm
from django.db.models import Q
from datetime import datetime, timedelta
from calendar import HTMLCalendar



User = get_user_model()


class ArticleListView(ListView):

    model = Article

    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleListView, self).get_context_data(*args, **kwargs)
        context['articles'] = self.model.objects.filter().order_by('-created')

        return context


class CategoryListView(ListView, CategoryAndArticlesListMixin):

    model = Category

    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryListView, self).get_context_data(*args, **kwargs)
        context['categories'] = self.model.objects.all()
        context['articles'] = Article.objects.all()[:4]
        context['article'] = Article.objects.get(id=5)
        context['articles_all'] = Article.objects.all()[:10]
        return context


class CategoryDetailView(DetailView, CategoryAndArticlesListMixin):
    
    model = Category
    
    template_name = 'category_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(*args, **kwargs)
        context['category'] = self.get_object()
        context['articles_from_category'] = self.get_object().article_set.all()
        return context

class ArticleDetailView(DetailView, CategoryAndArticlesListMixin):
    
    model = Article
    
    template_name = 'article_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context['article'] = self.get_object()
        return context

def dynamic_article_image(request):
    article_id = request.GET.get('article_id')
    article = Article.objects.get(id=article_id)
    data = {
        'article_image': article.image.url
    }
    return JsonResponse(data)


class DynamicArticleImageView(View):
    def get(self, *args, **kwargs):
        article_id = self.request.GET.get('article_id')
        article = Article.objects.get(id=article_id)
        data = {
        'article_image': article.image.url
        }
        return JsonResponse(data)


class DisplayArticlesByCategoryView(View):
    
    template = 'index.html'
    
    def get(self,request, *args, **kwargs):
        category_slug = self.request.GET.get('category_slug')
        articles = list(Article.objects.filter(category=Category.objects.get(slug=category_slug)).values('title', 'image', 'slug'))
        data = {
            'articles':articles
        }
        return JsonResponse(data)


class UserReactionView(View):

    template_name = 'article_detail.html'
    
    def get(self, request, *args, **kwargs):
        article_id = self.request.GET.get('article_id')
        article = Article.objects.get(id=article_id)
        like = self.request.GET.get('like')
        if like and (request.user not in article.users_reaction.all()):
            article.like += 1
            article.users_reaction.add(request.user)
            article.save()
        data = {
            'like': article.like
        }
        return JsonResponse(data)


class RegistrationView(View):
    
    template_name = 'registration.html'
    
    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        context = {
            'form': form
        }
        return render(self.request, self.template_name, context)
    
    def post(self, request,*args, **kwargs):
    
        form = RegistrationForm(request.POST or None)
    
        if form.is_valid():
            new_user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            new_user.set_password(password)
            password_check = form.cleaned_data['password_check']
            email = form.cleaned_data['email']
            new_user.save()
            UserAccount.objects.create(user=User.objects.get(username=new_user.username),
                                                            email=new_user.email)
            return HttpResponseRedirect('/')
    
        context = {
            'form': form
        }
    
        return render(self.request, self.template_name, context)


class LoginView(View):
    
    template_name = 'login.html'
    
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        context = {
            'form': form
        }
        return render(self.request, self.template_name, context)
    
    def post(self, request,*args, **kwargs):
    
        form = LoginForm(request.POST or None)
    
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(self.request, user)
                return HttpResponseRedirect('/')
    
        context = {
            'form': form
        }
    
        return render(self.request, self.template_name, context)


class RaitingListView(ListView):
    
    model = Raiting
    
    template_name = 'raiting_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(RaitingListView, self).get_context_data(*args, **kwargs)
        context['raitings'] = self.model.objects.filter().order_by('-created')

        return context



class RaitingDetailView(DetailView):
    
    model = Raiting
    
    template_name = 'raiting_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(RaitingDetailView, self).get_context_data(*args, **kwargs)
        return context


class SearchView(View):
    template_name = 'search.html'

    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        founded_articles = Article.objects.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)
        )
        founded_events = Event.objects.filter(
            Q(title__icontains=query)|
            Q(notes__icontains=query)
        )
        context = {
            'founded_articles': founded_articles, 
            'founded_events': founded_events
        }
        return render(self.request, self.template_name, context)



class EventListView(ListView):
    
    model = Event
    
    template_name = 'event_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(EventListView, self).get_context_data(*args, **kwargs)
        context['events'] = self.model.objects.filter().order_by('-created')

        return context

class EventDetailView(DetailView):
    
    model = Event

    template_name = 'event_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(EventDetailView, self).get_context_data(*args, **kwargs)
        return context




class VideoDownloadingView(ListView):

    model = VideoDownloading
    
    template_name = 'videooverview.html'

    def get_context_data(self, *args, **kwargs):
        context = super(VideoDownloadingView, self).get_context_data(*args, **kwargs)
        context['videos'] = self.model.objects.filter().order_by('-created')

        return context



