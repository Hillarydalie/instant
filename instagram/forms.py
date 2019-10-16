from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Image, Comment, Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Email Required!')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class CreateComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

class ImageUpload(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image','image_name','image_caption']

# class ImageUpload(CreateView):

#     class Meta:
#         model = Image
#         fields = ['profile', 'user_profile', 'likes']
#         exclude = ['user']

# class UpdateProfile(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['bio', 'profile_picture']

