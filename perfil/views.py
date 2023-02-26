from django.shortcuts import render, get_object_or_404
from biblioteca.models import Resenha

def profile(request):
    return render(request, 'perfil/profile.html')

