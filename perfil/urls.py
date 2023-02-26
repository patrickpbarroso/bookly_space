from django.contrib import admin
from django.urls import path
from perfil.views import profile

urlpatterns = [
    path('profile', profile, name='profile')
]