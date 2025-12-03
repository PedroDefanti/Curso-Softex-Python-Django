from django.db import models 
from django.contrib.auth.models import User 
 
class Tarefa(models.Model): 
    """ 
    Model para representar uma tarefa de usuário. 
     
    Cada tarefa tem: 
    - Um dono (user) 
    - Um título 
    - Um status de conclusão 
    - Data de criação automática 
    """ 
     
    # ForeignKey: Relacionamento Many-to-One 
    # Cada Tarefa pertence a UM usuário 
    # Um usuário pode ter VÁRIAS tarefas 
    # on_delete=CASCADE: Se o usuário for deletado, suas tarefas também são 
    user = models.ForeignKey( 
        User,  
        on_delete=models.CASCADE, 
        related_name='tarefas',  # Permite user.tarefas.all() 
        verbose_name='Usuário' 
    ) 
     
    # CharField: Campo de texto com limite 
    titulo = models.CharField( 
        max_length=200, 
        verbose_name='Título' 
    ) 
     
    # BooleanField: Campo verdadeiro/falso 
    concluida = models.BooleanField( 
        default=False, 
        verbose_name='Concluída' 
    ) 
     
    # DateTimeField: Data e hora 
    # auto_now_add=True: Preenche automaticamente na criação 
    criada_em = models.DateTimeField( 
        auto_now_add=True, 
        verbose_name='Criada em' 
    ) 
    
    descricao=models.TextField(blank=True,null=True)
     
    
    class Meta: 
            verbose_name = 'Tarefa' 
            verbose_name_plural = 'Tarefas' 
            ordering = ['-criada_em']  # Mais recentes primeiro 
        
            def __str__(self): 
                return f'{self.titulo}({'👌' if self.concluida else "❌" })'