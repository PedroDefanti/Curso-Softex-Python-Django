import random

def receber(lista1:list,lista2:list):
    if isinstance(lista1,list) and isinstance(lista2,list):
        l1=set(lista1)
        l2=set(lista2)
        uniao=l1.intersection(l2)
        return list(uniao)
    else:
        raise TypeError('Não passou uma lista')


