from django.contrib import admin 
from .models import Tarefa 
 
@admin.register(Tarefa) 
class TarefaAdmin(admin.ModelAdmin): 
    list_display = ['id', 'titulo', 'user', 'concluida', 'criada_em','descricao'] 
    list_filter = ['concluida', 'criada_em','descricao'] 
    search_fields = ['titulo', 'user__username']

# Register your models here.
