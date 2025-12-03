
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import status 
from .models import Tarefa 
from .serializers import TarefaSerializer 
 
class ListaTarefasAPIView(APIView): 
    """ 
    View para listar todas as tarefas (GET). 
     
    Endpoints: 
        GET /api/tarefas/ - Lista todas as tarefas 
    """ 
     
    def get(self, request, format=None): 
        """ 
        Retorna lista de todas as tarefas do banco. 
         
        Returns: 
            Response: JSON com lista de tarefas e status 200 
        """ 
        # 1. BUSCAR: ORM do Django busca todos os registros 
        tarefas = Tarefa.objects.all() 
         
        # 2. SERIALIZAR: Converter objetos Python → JSON 
        # many=True: indica que é uma lista de objetos 
        serializer = TarefaSerializer(tarefas, many=True) 
         
        # 3. RESPONDER: Retornar JSON com status HTTP 
        return Response(serializer.data, status=status.HTTP_200_OK)