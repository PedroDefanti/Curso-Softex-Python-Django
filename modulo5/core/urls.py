from django.urls import path 
from .views import (
    ListaTarefasAPIView, 
    ContagemTarefasAPIView, 
    EstatisticasTarefasAPIView,
    DetalheTarefaAPIView,
    DuplicarTarefaAPIView,
    ConcluirTodasTarefasAPIView,
    Sair,
    TarefaListaCriarAPIView,
    TarefaDetalhesAPIView,
    Regitrar_view,

    MinhaView,
    Mudar_senha,
    Ver_user
)


app_name = 'core' 

urlpatterns = [ 
    # Endpoints de tarefas
    path('tarefas/', TarefaListaCriarAPIView.as_view(), name='tarefas-list'),
    path('tarefas/<int:pk>/', TarefaDetalhesAPIView.as_view(), name='tarefas-detail'),
    path('tarefas/contagem/', ContagemTarefasAPIView.as_view(), name='contagem-tarefas'),
    path('tarefas/estatisticas/', EstatisticasTarefasAPIView.as_view(), name='estatisticas-tarefas'),
    path('tarefas/<int:pk>/duplicar/', DuplicarTarefaAPIView.as_view(), name='duplicar-tarefa'),
    path('tarefas/concluir-todas/', ConcluirTodasTarefasAPIView.as_view(), name='concluir-todas'),

    path('registro/', Regitrar_view.as_view(), name='registro'),
    path('sair/', Sair.as_view(), name='sair'),
    

    path('minha/', MinhaView.as_view(), name='user-me'),
 
    path('mudar_senha/',Mudar_senha.as_view(), name='mudar senah'),

    path('ver/', Ver_user.as_view(), name='ver senha'),
]