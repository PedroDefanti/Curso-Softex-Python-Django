from django.urls import path 
from .views import (ListaTarefasAPIView, 
                    ContagemTarefasAPIView, 
                    EstatisticasTarefasAPIView,
                    DetalheTarefaAPIView,
                    DuplicarTarefaAPIView,
                    ConcluirTodasTarefasAPIView,LogoutView,
                    TarefaListCreateAPIView,
                    TarefaRetrieveUpdateDestroyAPIView,
                    RegisterView)
# Namespace do app (útil para reverse()) 
app_name = 'core' 
urlpatterns = [ 

    path('tarefas/', TarefaListCreateAPIView.as_view(), name='tarefas-list'),
    path('tarefas/<int:pk>/', TarefaRetrieveUpdateDestroyAPIView.as_view(), name='tarefas-detail'),

    path('tarefas/contagem/', ContagemTarefasAPIView.as_view(), name='contagem-tarefas'),
    path('tarefas/estatisticas/', EstatisticasTarefasAPIView.as_view(), name='estatisticas-tarefas'),
    path('tarefas/<int:pk>/duplicar/', DuplicarTarefaAPIView.as_view(), name='duplicar-tarefa'),
    path('tarefas/concluir-todas/', ConcluirTodasTarefasAPIView.as_view(), name='concluir-todas'),

    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
