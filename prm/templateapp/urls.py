from django.conf.urls import url 
from templateapp import views

# for template tagging - set a global name called app_name
app_name = 'templateapp' # this is going to allow us to use template tagging. tells Django to look under this app and find the urls
urlpatterns = [
    url(r'^relative/', views.relative, name = 'relative'),
    url(r'^other/', views.other, name = 'other'),
    url(r'^register/', views.register, name = 'register'),


]
