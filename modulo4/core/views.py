from django.shortcuts import render,redirect,get_object_or_404
from .models import Tarefa
from .models import Execucacao
from .forms import TarefaForm



# Create your views here.
def home(request):
    if request.method=='POST':
        form=TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=TarefaForm()
    todas_as_tarefas = Tarefa.objects.all()
    todas_as_execucoes = Execucacao.objects.all()
    #return HttpResponse("<h1>Olá, Mundo! Esta é minha primeira pagina Django!</h1>")
    context={
        'nome_usuario':'Junior',
        'tecnologias':['Python','Django','HTML','CSS'],
        'tarefas':todas_as_tarefas,
        'execuções': todas_as_execucoes,
        'form':form,
    }
    return render(request,'home.html',context)


def concluir_tarefa(request,pk):
    tarefa = get_object_or_404(Tarefa,pk=pk)
    if request.method == 'POST':
        tarefa.concluida = True
        tarefa.save()
    return redirect('home')


def deletar_tarefa(request,pk):
    tarefa = get_object_or_404(Tarefa,pk=pk)
    if request.method == 'POST':
        tarefa.delete()
    return redirect('home')

