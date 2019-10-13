from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.urls import reverse
# from .forms import SignUpForm
import datetime as dt
# from .models import Image

# Create your home page views here.
def home(request):
    # images = Image.get_images()
    return render(request, 'index.html')