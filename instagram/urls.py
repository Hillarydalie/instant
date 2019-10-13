from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

# Template URLS
app_name = 'instagram'

urlpatterns = [
    # url(r'^signup', views.signup, name='signup'),
    # url(r'^user_login/$', views.user_login, name='user_login'), 
    url('^$', views.home , name = 'home'),
    # url(r'^user_logout/$', views.user_logout, name='logout'),
    # url(r'special/', views.special, name='special'),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)