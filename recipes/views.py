from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(response):
    return render(response, 'recipes/home.html')

def contato(response):
    return HttpResponse('Essa é a pagina CONTATO')


def sobre(response):
    return HttpResponse('Essa é a pagina do SOBRE')
