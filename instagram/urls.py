from django.conf.urls import url,include
from . import views as main_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login
# from .views import ImageCreateView

# Template URLS
app_name = 'instagram'

urlpatterns = [
    path('', main_views.index , name = 'index'),
    path('signup/', main_views.signup, name='signup'),
    path('post/new/', main_views.uploadimage, name = "newpost"),
    path('profile/', main_views.profile, name="profile"),
    path('update/',main_views.update_profile,name='update'),
    re_path(r'^search/$',main_views.searchprofile,name='search'),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)