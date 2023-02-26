from django.shortcuts import render, get_object_or_404
from biblioteca.models import Resenha

def index(request):
    resenhas = Resenha.objects.order_by("-data_postagem",).filter(publicada=True)
    return render(request, 'biblioteca/index.html', {"cards": resenhas})

def review(request, resenha_id):
    resenha = get_object_or_404(Resenha, pk=resenha_id)
    return render(request, 'biblioteca/review.html', {"resenha":resenha})