from django.urls import path 
from .views import ListaTarefasAPIView, ContagemTarefasAPIView, EstatisticasTarefasAPIView,DetalheTarefaAPIView,DuplicarTarefaAPIView,ConcluirTodasTarefasAPIView,LogoutView
# Namespace do app (útil para reverse()) 
app_name = 'core' 
urlpatterns = [ 
# /api/tarefas/ → ListaTarefasAPIView 
    path('tarefas/', ListaTarefasAPIView.as_view(), name='lista-tarefas'),
    path('tarefas/contagem/',ContagemTarefasAPIView.as_view(),name='contagem-tarefas'),
    path('tarefas/estatisticas',EstatisticasTarefasAPIView.as_view(),name='estatisticas-tarefas'),
    path('tarefas/<int:pk>/',DetalheTarefaAPIView.as_view(),name='detalhe-tarefa'),
    path('tarefas/<int:pk>/duplicar/', DuplicarTarefaAPIView.as_view(), name='duplicar-tarefa'),
    path('tarefas/concluir-todas/', ConcluirTodasTarefasAPIView.as_view(), name='concluir-todas'),
    path('logout/', LogoutView.as_view(), name='logout'), # ← Novo endpoint


]

