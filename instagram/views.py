from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import SignUpForm
import datetime as dt
# from .models import Image

# Create your home page views here.
# @login_required(login_url = 'login/')
def index(request):
    # images = Image.get_images()
    return render(request, 'index.html')

# Create sign up page views here
def signup(request):
    registered = False

    if request.method == "POST":
        registration_form = SignUpForm(data=request.POST)

        if registration_form.is_valid():
            # Grab user form and save to db
            user = registration_form.save()
            # Grab password hash it then save to db
            user.set_password(user.password)
            user.save()

            registered = True

        else: 
            print(registration_form.errors)
    else:
        registration_form = SignUpForm()
        # profile_form = UserProfileForm()

    return render(request, 'signup.html', {'registration_form':registration_form, 'registered':registered})

@login_required(login_url = 'login/')
def profile(request):

    return render(request, 'profile.html')

