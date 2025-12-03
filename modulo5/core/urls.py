from django.urls import path 
from .views import ListaTarefasAPIView 
# Namespace do app (útil para reverse()) 
app_name = 'core' 
urlpatterns = [ 
# /api/tarefas/ → ListaTarefasAPIView 
    path('tarefas/', ListaTarefasAPIView.as_view(), name='lista-tarefas'), 
]