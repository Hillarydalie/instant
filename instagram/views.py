from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse,Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import SignUpForm, CreateComment,ImageUpload,UserUpdateProfile,UserUpdate
import datetime as dt
from .models import Image, Comment, Profile

# Create your home page views here.
@login_required
def index(request):
    comment_form = CreateComment(data=request.POST)
    upload_form = ImageUpload()
    image = Image.objects.all()
    comments = Comment.objects.all()
    return render(request, 'index.html', {"image":image, "comments":comments, 'comment_form':comment_form})

# Create sign up page views here
def signup(request):
    registered = False

    if request.method == "POST":
        registration_form = SignUpForm(data=request.POST)

        if registration_form.is_valid():
            # Grab user form and save to db
            registration_form.save()
            return redirect('/')
            # Grab password hash it then save to db
            user.set_password(user.password)
            user.save()

            registered = True

        else: 
            print(registration_form.errors)
    else:
        registration_form = SignUpForm()

    return render(request, 'signup.html', {'registration_form':registration_form}, {"registered":registered})

@login_required
def profile(request):
    current_user = request.user
    images = Image.objects.filter(id = current_user.id).all()
    return render(request, 'profile.html', {"images":images})

@login_required
def uploadimage(request):
    upload_form = ImageUpload()

    if request.method == "POST":
        upload_form = ImageUpload(request.POST,request.FILES)

        if upload_form.is_valid():
            # Grab user form and save to db
            image = upload_form.save(commit = False)
            image.user = request.user
            image.save()
            return redirect('/')
    else:
        upload_form = ImageUpload()
        # profile_form = UserProfileForm()

    return render(request, 'instagram/image_form.html', {"upload_form":upload_form}, )

@login_required
def commenton(request):
    comment_form = CreateComment()

    if request.method == 'POST':
        if comment_form.is_valid():
            comment = comment_form.save(commit = False)
            comment.profile = request.user
            comment.save()

    return render(request, 'index.html')

@login_required
def update_profile(request):
  if request.method == 'POST':
    user_form = UserUpdateProfile(request.POST,instance=request.user)
    profile_form = UserUpdate(request.POST,request.FILES,instance=request.user.profile)
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      messages.success(request,'Your Profile account has been updated successfully')
      return redirect('/profile')
  else:
    user_form = UserUpdateProfile(instance=request.user)
    profile_form = UserUpdate(instance=request.user.profile) 
  params = {
    'user_form':user_form,
    'profile_form':profile_form
  }
  return render(request,'user/update_profile.html',params)


@login_required
def searchprofile(request):
  if 'search_user' in request.GET and request.GET["search_user"]:
    name = request.GET.get('search_user')
    result_user = Profile.search_profiles(name)
    images = Image.search_images(name)
    return render(request,'searchbar.html',{"users":the_users,"images":images})
  else:
    return render(request,'searchbar.html')