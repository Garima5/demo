from django.shortcuts import render
from templateapp.forms import UserProfileForm, UserForm

# Create your views here.
def index(request):
    return render(request,'templateapp/index.html')

def other(request):
    return render(request,'templateapp/other.html')

def relative(request):
    return render(request,'templateapp/relativeurl.html')

def base(request):
    return render(request,'templateapp/base.html')

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileForm(data= request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form()
            user.set_password(user.password) # hashing the password
            user.save()

            profile = profile_form.save(commit = False) 
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic'] #basically a disctionary of all files uploaded in the request, request.FILES is used to find the file

            profile.save()
            registered = True
        else:
            print (user_form.errors, profile_form.errors)
    else:
        # the request was not POST
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,'templateapp/register.html',
    {'user_form':user_form,'profile_form':profile_form, 'registered':registered})
            
