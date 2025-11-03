from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1> Olá, Mundo! </h1>')

def frase(request):
    return HttpResponse('<h1> Nova frase <b> aaaaaaa </b>')

