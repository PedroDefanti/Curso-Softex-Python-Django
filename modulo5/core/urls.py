from django.urls import path 
from .views import ListaTarefasAPIView, ContagemTarefasAPIView, EstatisticasTarefasAPIView,DetalheTarefaAPIView
# Namespace do app (útil para reverse()) 
app_name = 'core' 
urlpatterns = [ 
# /api/tarefas/ → ListaTarefasAPIView 
    path('tarefas/', ListaTarefasAPIView.as_view(), name='lista-tarefas'),
    path('tarefas/contagem/',ContagemTarefasAPIView.as_view(),name='contagem-tarefas'),
    path('tarefas/estatisticas',EstatisticasTarefasAPIView.as_view(),name='estatisticas-tarefas'),
    path('tarefas/<int:pk>/',DetalheTarefaAPIView.as_view(),name='detalhe-tarefa'),
# ^^^^^^^^
# Captura o ID e passa para a view
]

