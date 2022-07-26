
from django import urls
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

from django.views.static import serve
from django.urls import re_path as url
# from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('employee/', include('employee.urls')),
    path('contactus/', include('contact.urls')),
    path('aboutus/', include('about.urls')),
    path('authentication/', include('authentication.urls')),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)