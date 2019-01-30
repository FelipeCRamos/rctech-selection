from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.home_page),
    url(r'^search$', views.search_view)
]
