from django.contrib import admin
from . models import Tarefa

# Register your models here.


class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'user', 'concluida', 'criada_em')
    list_filter = ('concluida', 'user', 'criada_em')
    search_fields=('titulo','user__username')
    fieldsets=(
        ('Informações Principais',{
            'fields':('user','titulo')
        }),
        ('Status da Tarefa',{
            'fields':('concluida','criada_em')
        })
    )
    readonly_fields=('criada_em',)
admin.site.register(Tarefa, TarefaAdmin)

# Register your models here.


