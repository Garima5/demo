# This file is not created by default. We create this to add to include function in the urls file of the project
from django.conf.urls import url 
from prm_firstapp import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^$', views.help,name='help'),
    #url(r'^$', views.help,name='help')
]