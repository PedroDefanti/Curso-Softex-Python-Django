from rest_framework import serializers
from .models import Tarefa
from django.utils import timezone
from django.utils.timezone import now

class TarefaSerializer(serializers.ModelSerializer):
    titulo = serializers.CharField(
        max_length=200,
        error_messages={
            'required': 'O título é obrigatório.',
            'blank': 'O título não pode ser vazio.',
            'max_length': 'O título não pode ter mais de 200 caracteres.'
            }
        )
    
    
    
    
    class Meta:
        model = Tarefa
        fields = ['id','user','titulo','descricao','concluida','prioridade','prazo','criada_em','data_concuida']
        read_only_fields = ['id', 'criada_em']
        
        
        
    
        

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
                    'prazo': 'O prazo é obrigatório para  concluídas.'
                })
        


        return data
    
    
    def validate_concluida(self,data):
        concluida = data.get('concluida', False)
        if concluida:
            data_concuida=data.get(data['data_concuida'].today())
    
    
    
    
    