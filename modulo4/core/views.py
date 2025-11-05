from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    #return HttpResponse("<h1>Olá, Mundo! Esta é minha primeira pagina Django!</h1>")
    context={
        'nome_usuario':'Junior',
        'tecnologias':['Python','Django','HTML','CSS']
    }
    return render(request,'home.html',context)

def call(request):
    return HttpResponse("<h1>Chamada por aqui.</h1>")