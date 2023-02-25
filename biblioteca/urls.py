from django.contrib import admin
from django.urls import path
from biblioteca.views import index, review

urlpatterns = [
    path('', index, name='index'),
    path('review/<int:resenha_id>', review, name='review')
]