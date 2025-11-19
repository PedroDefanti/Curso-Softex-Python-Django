from django.db import models
from django.contrib.auth.models import User
class Tarefa(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    concluida = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.titulo


class Execucacao(models.Model):
    nome = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    hora = models.DateTimeField(auto_now_add=True)
    resolvida = models.BooleanField(default=False)
    def __str__(self):
        return self.nome