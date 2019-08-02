from django.views.generic.list import MultipleObjectMixin

from .models import Category,  Article


class CategoryAndArticlesListMixin(MultipleObjectMixin):
    
    """Return mix data include objects from Category and Article models"""

    def get_context_data(self, *args, **kwargs):
        context = {}
        context['categories'] = Category.objects.all()
        context['tab_articles'] = Article.objects.all()
        
        return context

