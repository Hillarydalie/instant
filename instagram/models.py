from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.dispatch import receiver
from django.db.models.signals import post_save

# This is the profile model here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profilepicture/', blank=True, default='default.png')
    bio = models.CharField(max_length=140)

    def __str__(self):
        return self.user.username


    @receiver(post_save, sender = User) 
    def create_profile(instance,sender,created, **kwargs):
        if created:
            Profile.objects.create(user = instance)

    @receiver(post_save, sender= User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

    @property
    def all_comments(self):
        return self.comments.all()

    # @property
    # def my_followers(self):
    #     return self.followers.count()

    # @property
    # def me_following(self):
    #     return self._all_following()

    @classmethod
    def search_profiles(cls,search_term):
        profiles = cls.objects.filter(user__username__icontains = search_term).all()
        return profiles

class Image(models.Model):
    image = models.ImageField(upload_to="image/")
    image_name = models.CharField(max_length = 100, blank=True)
    image_caption = models.TextField()
    published_date = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name= 'likes', blank=True)

    @classmethod
    def save_image(self):
        self.save()

    @classmethod
    def delete_image(self):
        self.delete()

    # @classmethod
    # def get_images_id(cls, image_id):
    #     images = cls.objects.get(id=image_id)
    #     return get_send_file_max_age()
    # def total_likes(self):
    #     self.likes.count()

class Comment(models.Model):
    comment = models.CharField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.profile

