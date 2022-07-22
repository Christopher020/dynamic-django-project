from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee),
    path('about/', views.about),
    path('profile/', views.profile, name='profile'),
]
