from django.contrib import admin
from django.urls import path
from biblioteca.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
]