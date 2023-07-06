from unicodedata import name
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('user/<id>', views.view_user, name = 'view_user'),
    path('takeScreenshot', views.takeScreenshot, name='takeScreenshot')
]