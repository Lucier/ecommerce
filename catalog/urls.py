# coding=utf-8

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.produtos_lista, name='produtos_lista'),
    url(r'^(?P<slug>[\w_-]+)/$', views.category, name='category'),
]
