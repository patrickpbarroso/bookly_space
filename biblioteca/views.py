from django.shortcuts import render

def index(request):
    return render(request, 'biblioteca/index.html')

def review(request):
    return render(request, 'biblioteca/review.html')