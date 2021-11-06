"""prm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from prm_firstapp import views
from templateapp import views as tv
from django.conf.urls import include
urlpatterns = [
    url(r'^$',views.index, name='index'), #  Mapping the application's view to this url
    #url(r'^prm_firstapp/',include('prm_firstapp.urls') ),
    url(r'^help/',include('prm_firstapp.urls') ), #multiple urls uner same app - this syntax is wrong
    path('admin/', admin.site.urls),
    url(r'^formpage/',views.formPage,name='form_name'),
    url(r'^modelformpage/',views.modelformPage,name='modelform'),
    url(r'^templateindex/', tv.index,name ='app2index'), # calling index of the second app
    url(r'^templateapp/',include('templateapp.urls')) # calling all urls from templateapp - it is saying that if we go to domain.com/templateapp/ then go to these urls
]
