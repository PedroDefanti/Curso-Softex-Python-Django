from django.db import models 
from django.contrib.auth.models import User 
from django.core.exceptions import ValidationError
from django.utils import timezone
class Tarefa(models.Model): 
    
    prioridades_choice=[('baixa','Baixa'),('media','Media'),('alta','Alta')]

    user = models.ForeignKey( 
        User,  
        on_delete=models.CASCADE, 
        related_name='tarefas',  
        verbose_name='Usuário' 
    ) 

    titulo = models.CharField( 
        max_length=200, 
        verbose_name='Título' 
    ) 

    concluida = models.BooleanField( 
        default=False, 
        verbose_name='Concluída' 
    ) 

    criada_em = models.DateTimeField( 
        auto_now_add=True, 
        verbose_name='Criada em' 
    ) 
    
    descricao=models.TextField(blank=True,null=True)
    
    prioridade = models.CharField(
        max_length=10,
        choices=prioridades_choice,
        default='media'
    )
    
    prazo=models.DateField(null=True,blank=True)
    
    data_concuida=models.DateField(
        blank=True,
        null=True
    )

     
    
    class Meta: 
            verbose_name = 'Tarefa' 
            verbose_name_plural = 'Tarefas' 
            ordering = ['-criada_em']
            
    def __str__(self): 
                return f'{self.titulo}({'👌' if self.concluida else "❌" })'
            
            
   
        
            
            
            
                    
            
            