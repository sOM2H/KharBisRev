from django.views.generic.list import MultipleObjectMixin
from .models import Category, Article, Event

class CategoryAndArticlesListMixin(MultipleObjectMixin):
    
    def get_context_data(self, *args, **kwargs):
        context = {}
        context['categories'] = Category.objects.all()
        context['tab_articles'] = Article.objects.all()
        
        return context


class CategoryAndEventListMixin(MultipleObjectMixin):


    def get_context_data(self, *args, **kwargs):
        context = {}
        context['categories'] = Category.objects.all()
        context['event'] = Event.objects.all()
        
        return context