from django.conf.urls import url,include
from . import views
from django.views.generic import ListView, DetailView
from home.models import Post

urlpatterns = [
    url(r'^$', views.home_page),
    url(r'^search$', views.search_view)
]
