from django.shortcuts import render
from .models import Tarefa
from .models import Execucacao



# Create your views here.
def home(request):
    todas_as_tarefas = Tarefa.objects.all()
    todas_as_execucoes = Execucacao.objects.all()
    #return HttpResponse("<h1>Olá, Mundo! Esta é minha primeira pagina Django!</h1>")
    context={
        'nome_usuario':'Junior',
        'tecnologias':['Python','Django','HTML','CSS'],
        'tarefas':todas_as_tarefas,
        'execuções': todas_as_execucoes
    }
    return render(request,'home.html',context)

