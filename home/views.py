from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def curiosidades(request):
    return render(request, 'curiosidades.html')

def contato(request):
    return render(request, 'contato.html')
