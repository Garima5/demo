from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def members(request):
    return HttpResponse("Hello world!")

def loadTable(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())