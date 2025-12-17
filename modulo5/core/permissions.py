from rest_framework import permissions
class IsGerente(permissions.BasePermission):
    """
    Permissão customizada que concede acesso apenas se o usuário
    pertencer ao grupo 'Gerente'.
    """
    def has_permission(self, request, view):
        # 1. Verificação de Sanidade: Usuário deve estar logado
        if not request.user or not request.user.is_authenticated:
            return False
        # 2. Verificação de Grupo: Checa se 'Gerente' está na lista de grupos
        return request.user.groups.filter(name='Gerente').exists()
