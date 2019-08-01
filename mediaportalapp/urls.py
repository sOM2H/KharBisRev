# -- coding: utf-8 --
from django.conf.urls import url
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout
from .views import (RegistrationView,
                    RaitingListView,
                    UserReactionView,
                    CategoryListView,
                    CategoryDetailView,
                    DisplayArticlesByCategoryView,
                    ArticleDetailView,
                    DynamicArticleImageView,
                    LoginView,
                    RaitingDetailView,
                    SearchView,
                    EventListView,
                    EventDetailView,
                    VideoDownloadingView)

urlpatterns = [
    url(r'^$', CategoryListView.as_view(), name='base_view'),
    
    url(r'^category/(?P<slug>[-\w]+)/$', CategoryDetailView.as_view(), name='category_detail'),
    
    url(r'^(?P<category>[-\w]+)/(?P<slug>[-\w]+)/$', ArticleDetailView.as_view(), name='article_detail'),
        
    url(r'^show_article_image/$', DynamicArticleImageView.as_view(), name = 'article_image'),
    
    url(r'^display_articles_by_category/$', DisplayArticlesByCategoryView.as_view(), name = 'articles_by_category'),
    
    url(r'^user_reaction/$', UserReactionView.as_view(),name='user_reaction'),
    
    url(r'^registration/$', RegistrationView.as_view(), name='registration'),
    
    url(r'^login/$', LoginView.as_view(), name='login'),
    
    url(r'^raitings/$', RaitingListView.as_view(), name='raitings_list'),
    
    url(r'/raitings/(?P<slug>[-\w]+)/$', RaitingDetailView.as_view(), name='raiting_detail'),
    
    url(r'^calendar/$', EventListView.as_view(), name='events_view'),
    
    url(r'/calendar/(?P<slug>[-\w]+)/$', EventDetailView.as_view(), name='event_detail'),
    
    url(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('base_view')), name='logout_view'),
    
    url(r'^search/$', SearchView.as_view(), name='search_view'),
    
    url(r'^videooverview/$', VideoDownloadingView.as_view(), name='video_view'),
]