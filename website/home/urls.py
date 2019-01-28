from django.conf.urls import url,include
from . import views
from django.views.generic import ListView, DetailView
from home.models import Post

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Post.objects.all(),
                                template_name = 'home/index.html')),
    url(r'^search', views.search_view)
]
