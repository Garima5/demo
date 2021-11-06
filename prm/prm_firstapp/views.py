import re
from django import forms
from django.db import reset_queries
from django.shortcuts import render
from django.http import HttpResponse
#from prm import prm_firstapp
from prm_firstapp.models import Salary
from prm_firstapp import forms
from prm_firstapp.forms import NewUserForm
#from prm_firstapp.forms import employeeForm

# Create your views here.
def index(request):
    #return HttpResponse('<em>Welcome to Premier Rubber Mills</em>')
    salary_rec = Salary.objects.order_by('beltA')
    data_dic = {'insert_table': salary_rec}
    my_dict = {'insert_me':'Hello I am from views.py !'}
    return render(request, 'prm_firstapp/index.html', context = data_dic)

# the help page view:
def help(request):
    #return HttpResponse('<em>Welcome to Premier Rubber Mills</em>')
    salary_rec = Salary.objects.order_by('beltB')  # order_by is similar to mysql order by
    data_dic = {'insert_table': salary_rec}
    my_dict = {'insert_me':'Hello I am from views.py !'}
    return render(request, 'prm_firstapp/help.html', context = data_dic)

def formPage(request):
    # make an instance of the form
    """
    very basic view - not doing anything with data posted
    form = forms.employeeForm() 
    return render(request, 'prm_firstapp/formPage.html', {'key_form':form}) 
    """
    form = forms.employeeForm()
    if request.method == 'POST':
        form = forms.employeeForm(request.POST)
        if form.is_valid():
            # do something
            # grab the data and print it out
            print ("VALIDATION SUCCESSFUL")
            print("Name: "+form.cleaned_data['name'])
            print("BeltA: "+ str(form.cleaned_data['belt_A']))
            print("BeltB: "+ str(form.cleaned_data['belt_B']))
            print("BeltC: "+ str(form.cleaned_data['belt_C']))
    return render(request, 'prm_firstapp/formPage.html',{'key_form':form})
    

"""
def help(request):
    helpdict = {'help_key':'help page'}
    return render(request, 'prm_firstapp/help.html', context = helpdict)
"""
# view for the model form page
def modelformPage(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit="true")
            return index(request)
        else:
            print ("Invalid form")
    return render(request, 'prm_firstapp/modelform.html', {'form':form})