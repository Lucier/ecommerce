from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contato/$', views.contato, name='contato'),
    url(r'^produto/$', views.produto, name='produto'),
    url(r'^produtos/$', views.produtos_lista, name='produtos_lista'),
]