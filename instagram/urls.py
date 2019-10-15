from django.conf.urls import url,include
from . import views as main_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login

# Template URLS
app_name = 'instagram'

urlpatterns = [
    path('', main_views.index , name = 'index'),
    path('signup/', main_views.signup, name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name = 'login.html'),name='login'),
    path('logout/',auth_views.LoginView.as_view(template_name = 'logout.html'),name='logout'),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)