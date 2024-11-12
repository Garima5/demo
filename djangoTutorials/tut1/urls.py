from django.urls import path
from . import views

urlpatterns = [
    path('', views.loadTable, name='table'),
    #path('tables', views.loadTable, name='table'),
]