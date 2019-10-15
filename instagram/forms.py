from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ListView

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Email Required!')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

# class ImageUpload(CreateView):
