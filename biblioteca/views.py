from django.shortcuts import render, get_object_or_404
from biblioteca.models import Resenha

def index(request):
    resenhas = Resenha.objects.order_by("-data_postagem",).filter(publicada=True)
    return render(request, 'biblioteca/index.html', {"cards": resenhas})

def review(request, resenha_id):
    resenha = get_object_or_404(Resenha, pk=resenha_id)
    return render(request, 'biblioteca/review.html', {"resenha":resenha})

def buscar(request):
    resenhas = Resenha.objects.order_by("-data_postagem",).filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar: 
            resenhas = resenhas.filter(titulo__icontains=nome_a_buscar)
    return render(request, 'biblioteca/buscar.html', {"cards": resenhas})