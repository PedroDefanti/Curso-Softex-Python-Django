from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Tarefa
from .serializers import TarefaSerializer, ConcluirTodasSerializer,UserRegistrationSerializer
from django.db import IntegrityError
import logging
from django.db.models import Count, Q
logger = logging.getLogger(__name__)
from django.shortcuts import get_object_or_404
from django.utils.timezone import now
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .permissions import IsGerente




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
        return get_object_or_404(Tarefa, pk=pk)
    def get(self, request, pk, format=None):

        tarefas=self.get_object(pk)
        serializer=TarefaSerializer(tarefas)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
    def put(self, request, pk, format=None):
        tarefa = self.get_object(pk)
        if tarefa.prioridade == 'alta' and request.data.get('concluida') and not tarefa.concluida:
            pass

        serializer = TarefaSerializer(tarefa, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):
        tarefa = self.get_object(pk)

        if tarefa.prioridade == 'alta' and request.data.get('concluida') and not tarefa.concluida:
            return Response(
                {
                    'error': 'Tarefas de alta prioridade só podem ser concluídas via PUT (atualização completa).',
                    'detail': 'Use o método PUT com todos os campos para concluir esta tarefa.'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = TarefaSerializer(tarefa, data=request.data, partial=True)
        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        tarefa = self.get_object(pk)

        tarefa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DuplicarTarefaAPIView(APIView):
    
    def post(self, request, pk, format=None):

        tarefa_original = get_object_or_404(Tarefa, pk=pk)

        dados_duplicados = {
            'user': tarefa_original.user.id,
            'titulo': f"{tarefa_original.titulo} (Cópia)",
            'descricao': tarefa_original.descricao,
            'prioridade': tarefa_original.prioridade,
            'prazo': tarefa_original.prazo,
            'concluida': False, 

        }

        serializer = TarefaSerializer(data=dados_duplicados)
        
        if serializer.is_valid():

            nova_tarefa = serializer.save()
            logger.info(f"[INFO]: Tarefa {pk} duplicada com sucesso. Nova tarefa ID: {nova_tarefa.id}")
            
            return Response(
                {
                    'mensagem': 'Tarefa duplicada com sucesso.',
                    'original_id': tarefa_original.id,
                    'nova_tarefa': serializer.data
                },
                status=status.HTTP_201_CREATED
            )

        logger.warning(f"[WARNING]: Erro ao duplicar tarefa {pk}: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConcluirTodasTarefasAPIView(APIView):
    
    def patch(self, request, format=None):

        filtros = {}
        prioridade = request.data.get('prioridade') or request.query_params.get('prioridade')
        user_id = request.data.get('user') or request.query_params.get('user')
        queryset = Tarefa.objects.filter(concluida=False)

        if prioridade:
            if prioridade.lower() not in ['baixa', 'media', 'alta']:
                return Response(
                    {'error': 'Prioridade inválida. Use: baixa, media ou alta.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            queryset = queryset.filter(prioridade=prioridade.lower())
        
        if user_id:
            try:
                user_id = int(user_id)
                queryset = queryset.filter(user_id=user_id)
            except ValueError:
                return Response(
                    {'error': 'ID de usuário inválido.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        total_tarefas = queryset.count()
        
        if total_tarefas == 0:
            return Response(
                {
                    'mensagem': 'Nenhuma tarefa pendente encontrada com os filtros aplicados.',
                    'tarefas_atualizadas': 0
                },
                status=status.HTTP_200_OK
            )

        data_hoje = now().date()
        tarefas_atualizadas = queryset.update(
            concluida=True,
            data_concuida=data_hoje
        )
        
        logger.info(f"[INFO]: {tarefas_atualizadas} tarefas concluídas em lote.")

        return Response(
            {
                'mensagem': 'Tarefas concluídas com sucesso.',
                'tarefas_atualizadas': tarefas_atualizadas,
                'data_conclusao': data_hoje,
                'filtros_aplicados': {
                    'prioridade': prioridade,
                    'user_id': user_id
                }
            },
            status=status.HTTP_200_OK
        )
        
class MinhaView(APIView):
# Adicionando a permissão
    permission_classes = [IsAuthenticated]
    def get(self, request):
    # Se chegou aqui, request.user é SEMPRE um objeto User logado
        print(f"Usuário autenticado: {request.user.username}")
        return Response(f'Usuario Autenticado:{request.user.username}',status=status.HTTP_200_OK)
# ...

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist() # Adiciona o token à lista negra
            
            return Response({"detail": "Logout realizado com sucesso."},status=status.HTTP_205_RESET_CONTENT,)
        except Exception: # Captura exceções como token_not_valid
            return Response(
            {"detail": "Token inválido."},
            status=status.HTTP_400_BAD_REQUEST)

class TarefaListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticated] # Exige Token válido
    def get_queryset(self):
        """
        Sobrescreve o comportamento padrão para retornar APENAS
        os dados pertencentes ao usuário logado.
        """
        # 1. Recupera o usuário validado pelo JWT
        user = self.request.user
        # 2. Retorna o filtro. O Django fará o WHERE user_id = X no banco.
        return Tarefa.objects.filter(user=user)
    def perform_create(self, serializer):
        # Garante que a tarefa criada seja vinculada ao usuário logado
        serializer.save(user=self.request.user)
        
class TarefaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        """
        Garante que operações de detalhe (GET, PUT, DELETE por ID)
        só encontrem o objeto se ele pertencer ao usuário.
        """
        user = self.request.user
        return Tarefa.objects.filter(user=user)

class RegisterView(generics.CreateAPIView):
    """
    Endpoint para cadastro de novos usuários.
    Acesso: Público (Qualquer um pode criar conta).
    """
    queryset = User.objects.all()
    permission_classes = [AllowAny] # Sobrescreve o padrão global
    serializer_class = UserRegistrationSerializer

class TarefaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TarefaSerializer
    # Removemos a linha estática 'permission_classes' para usar o método dinâmico
    def get_queryset(self):
        return Tarefa.objects.filter(user=self.request.user)
    def get_permissions(self):
        """
        Instancia e retorna a lista de permissões que esta view requer,
        dependendo do método HTTP da requisição.
        """
        if self.request.method == 'DELETE':
        # Para deletar: Precisa estar logado E ser Gerente
        # A ordem importa: primeiro checa login, depois o grupo
            return [IsAuthenticated(), IsGerente()]
        # Para GET, PUT, PATCH: Basta estar logado (e ser dono, garantido pelo queryset)
        return [IsAuthenticated()]

