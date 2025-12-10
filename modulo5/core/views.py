from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tarefa
from .serializers import TarefaSerializer
from django.db import IntegrityError
import logging
from django.db.models import Count, Q
logger = logging.getLogger(__name__)
from django.shortcuts import get_object_or_404


class ListaTarefasAPIView(APIView):

    def get(self, request, format=None):
        tarefas = Tarefa.objects.all()
        serializer = TarefaSerializer(tarefas, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):

        
            serializer = TarefaSerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                logger.info(f"[INFO]: Tarefa criada: {serializer.data['id']}")
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )
            logger.warning(f"[WARNING]: Validação falhou: {serializer.errors}")
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            

class ContagemTarefasAPIView(APIView):
    
    def get(self,request):
        total=Tarefa.objects.count()
        concluidas=Tarefa.objects.filter(concluida=True).count()
        pendentes=total-concluidas
        
        return Response({
            'total':total,
            'concluidas':concluidas,
            'pendentes':pendentes
        })
        
class EstatisticasTarefasAPIView(APIView):

    def get(self, request, format=None):

        try:

            tarefas = Tarefa.objects.all()


            stats = tarefas.aggregate(
                total=Count('id'),
                concluidas=Count('id', filter=Q(concluida=True)),
                pendentes=Count('id', filter=Q(concluida=False)),
            )

            total = stats['total']
            concluidas = stats['concluidas']

            resultado = {
                'total': total,
                'concluidas': concluidas,
                'pendentes': stats['pendentes'],
                'taxa_conclusao': round(concluidas / total, 2) if total > 0 else 0
            }

            return Response(resultado, status=status.HTTP_200_OK)

        except Exception as e:
            logger.error(f"Erro ao gerar estatísticas: {str(e)}")
            return Response(
                {'error': 'Erro ao gerar estatísticas.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
            
            
            
class DetalheTarefaAPIView(APIView):
    def get_object(self, pk):
        """
        Busca a tarefa pelo ID e retorna 404 se não encontrada.
        """
        return get_object_or_404(Tarefa, pk=pk)

    # ...
    
    def get(self, request, pk, format=None):
        # ^^
        # Parâmetro capturado da URL
        tarefas=self.get_object(pk)
        serializer=TarefaSerializer(tarefas)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
    def put(self, request, pk, format=None):
        """
        Atualiza tarefa completamente (substituição total).
        Exige que TODOS os campos editáveis sejam enviados.
        """
        # 1. BUSCAR: Obter o objeto existente
        tarefa = self.get_object(pk)
        # 2. SERIALIZAR: Passar objeto antigo E novos dados
        serializer = TarefaSerializer(tarefa, data=request.data)
        # ^^^^^ ^^^^^^^^^^^^^^^^
        # | Nova versão
        # Versão atual
        # 3. VALIDAR: Checar se JSON está completo e válido
        if serializer.is_valid():
        # 4. SALVAR: Atualizar no banco
            serializer.save()
        # 5. RESPONDER: Retornar objeto atualizado
            return Response(serializer.data, status=status.HTTP_200_OK)
        # ERRO: Retornar erros de validação
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):
        """
        Atualiza tarefa completamente (substituição total).
        Exige que PARCIAL os campos editáveis sejam enviados.
        """
        # 1. BUSCAR: Obter o objeto existente
        tarefa = self.get_object(pk)
        # 2. SERIALIZAR: Passar objeto antigo E novos dados
        serializer = TarefaSerializer(tarefa, data=request.data,partial=True)
        # ^^^^^ ^^^^^^^^^^^^^^^^
        # | Nova versão
        # Versão atual
        # 3. VALIDAR: Checar se JSON está completo e válido
        if serializer.is_valid():
        # 4. SALVAR: Atualizar no banco
            serializer.save()
        # 5. RESPONDER: Retornar objeto atualizado
            return Response(serializer.data, status=status.HTTP_200_OK)
        # ERRO: Retornar erros de validação
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Remove um recurso específico.
        """
        # 1. BUSCAR: Obter o objeto (trata 404 se não existir)
        tarefa = self.get_object(pk)
        # 2. DELETAR
        tarefa.delete()
        # 3. RESPONDER: 204 No Content (sucesso sem corpo de resposta)
        return Response(status=status.HTTP_204_NO_CONTENT)

