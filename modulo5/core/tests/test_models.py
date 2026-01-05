

from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from django.db import IntegrityError
from core.models import Tarefa

class TarefaModelTest(TestCase):
    def setUp(self):
    
        self.user = User.objects.create_user(
        username='testuser',
        password='testpass123'
)
        
    def test_criacao_tarefa_sucesso(self):
        """Testa se uma tarefa é criada corretamente com os campos padrão."""
        tarefa = Tarefa.objects.create(
        user=self.user,
        titulo='Tarefa de Teste',
        concluida=False
)
        self.assertEqual(tarefa.titulo, 'Tarefa de Teste')
        self.assertFalse(tarefa.concluida)
        self.assertEqual(tarefa.user, self.user)
        # Verifica se o auto_now_add funcionou
        self.assertIsNotNone(tarefa.criada_em)
# Assertions (Verificações)
    def test_str_representation(self):
        """
        Testa o método __str__.
        Importante pois é como o objeto aparece no Admin do Django.
        """
        tarefa = Tarefa.objects.create(
        user=self.user,
        titulo='Estudar Testes',
        concluida=True
        )
        # Supondo que seu __str__ seja: f"{self.titulo} ({'✓' if self.concluida else '✗'})"
        esperado = 'Estudar Testes (✓)'
        self.assertEqual(str(tarefa), esperado)

    def test_user_eh_obrigatorio(self):
        """Testa a integridade do banco: user não pode ser null."""
        with self.assertRaises(IntegrityError):
            Tarefa.objects.create(
            titulo='Sem dono',
            concluida=False
            # user ausente propositalmente
            )