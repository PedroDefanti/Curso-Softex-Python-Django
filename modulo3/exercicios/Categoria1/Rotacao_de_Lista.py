def rotacao(lista:list,nun:int)->list[int]:
    if isinstance(lista,list) and isinstance(nun,int):
        inicio=lista[:-nun]
        fim=lista[-nun:]
        nova_lista=fim+inicio
        return nova_lista
    else:
        raise TypeError('Invalido')

