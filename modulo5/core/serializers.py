from rest_framework import serializers
from .models import Tarefa
from django.utils import timezone
from django.utils.timezone import now
from django.contrib.auth.models import User,Group


class TarefaSerializer(serializers.ModelSerializer):
    titulo = serializers.CharField(
        max_length=200,
        error_messages={
            'required': 'O título é obrigatório.',
            'blank': 'O título não pode ser vazio.',
            'max_length': 'O título não pode ter mais de 200 caracteres.'
            }
        )
    user = serializers.StringRelatedField(read_only=True)

    
    
    
    
    class Meta:
        model = Tarefa
        fields = '__all__'
        read_only_fields = ['id', 'user', 'criada_em']
        
        
        
    
        

    def validate_titulo(self, value):

        value = value.strip()
        if not value:
            raise serializers.ValidationError(
                "O título não pode ser vazio ou conter apenas espaços."
            )
        if len(value) < 3:
            raise serializers.ValidationError(
                "O título deve ter pelo menos 3 caracteres."
            )
        if value.isdigit():
            raise serializers.ValidationError(
                "O título não pode conter apenas números."
            )

        
        return value
    
    def validate_prioridade(self, value):

        value = value.strip().lower()
        prioridade = ["baixa", "media", "alta"]

        
        if value not in prioridade:
            raise serializers.ValidationError(
                "Apenas prioridades com o titulo: baixa, media ou alta "
            )
        return value
        
    def validate_prazo(self, value):

        if value and value < now().date():
            raise serializers.ValidationError(
                "O prazo não pode ser no passado."
            )
        return value

    def validate(self, data):
        concluida = data.get('concluida', False)
        prazo = data.get('prazo')
       
        if not concluida and not prazo:
                raise serializers.ValidationError({
                    'prazo': 'O prazo é obrigatório para tarefas não concluídas.'
                })
        


        return data

    def update(self, instance, validated_data):
 
        concluida = validated_data.get('concluida', instance.concluida)

        if concluida and not instance.data_concuida:
            validated_data['data_concuida'] = now().date()

        if not concluida and instance.data_concuida:
            validated_data['data_concuida'] = None
        
        return super().update(instance, validated_data)
    
    def create(self, validated_data):

        concluida = validated_data.get('concluida', False)
        if concluida and 'data_concuida' not in validated_data:
            validated_data['data_concuida'] = now().date()
        
        return super().create(validated_data)

class ConcluirTodasSerializer(serializers.Serializer):
    prioridade = serializers.ChoiceField(
        choices=['baixa', 'media', 'alta'],
        required=False,
        help_text='Filtrar por prioridade específica'
    )
    user = serializers.IntegerField(
        required=False,
        help_text='Filtrar por ID do usuário'
    )
    

class UserRegistrationSerializer(serializers.ModelSerializer):
    # Definimos 'write_only=True' para que a senha seja aceita no cadastro (POST),
    # mas NUNCA seja devolvida na resposta (Response JSON).
    password = serializers.CharField(
    write_only=True,
    required=True,
    style={'input_type': 'password'}
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    def create(self, validated_data):
# 1. Cria o usuário com segurança
        password = validated_data.pop('password')
        user = User.objects.create_user(
        username=validated_data['username'],
        email=validated_data.get('email', ''),
        password=password
        )
        # 2. Lógica de Atribuição de Cargo (Role)
        try:
            # Busca o grupo 'Comum'
            grupo_comum = Group.objects.get(name='Comum')
            # Adiciona o usuário ao grupo
            user.groups.add(grupo_comum)
        except Group.DoesNotExist:
            # Fallback: Se o grupo não existir, o usuário é criado sem grupo.
            # Em produção, deveríamos logar um erro aqui.
            pass
        return user
