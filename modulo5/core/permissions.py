from rest_framework import permissions


class Gerente(permissions.BasePermission):

    def permissão(self, request, view):

        if not request.user or not request.user.is_authenticated:
            return False

        return request.user.groups.filter(name='Gerente').exists()

class Admin(permissions.BasePermission):

    
    def permisao(self, request, view):

        return request.user and request.user.is_authenticated
    
    def permisao_do_user(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.user == request.user


class Chefe(permissions.BasePermission):

    def tem_permissao(self, request, view, obj):
        return obj.user == request.user