from django.db import models
from django.contrib.auth.models import User
import datetime as dt

# This is the profile models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='profilepicture/', null=True, blank=True)
    bio = models.TextField()

    def __str__(self):
        return self.user.username
        
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def update_profile(cls, id, bio):
        update = Image.objects.filter(id=id).update(bio=bio)
        return update

    @classmethod
    def search_profile(cls, search_term):
        profile = cls.objects.filter(user__username__icontains=search_term)
        return profile

# This is the tag model
class Tag(models.Model):
    tag = models.CharField(max_length=30)

    def __str__(self):
        return self.tag

    def save_tag(self):
        self.save()

    def delete_tag(self):
        self.delete()

class Location(models.Model):
    location = models.CharField(max_length=60)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()