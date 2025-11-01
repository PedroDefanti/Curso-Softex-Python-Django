def nova_lista_num(lista1:list,lista2:list)->list[int]:
    if not isinstance(lista1,list) and not isinstance(lista2,list):
        raise TypeError('Tipo inválido')
    tamanho_max=max(len(lista1),len(lista2))
    nova_lista=[]
    for i in range(tamanho_max):
        try:
            valor_lista1=lista1[i]
            valor_lista2=lista2[i]
            if not isinstance(valor_lista1,(int,float)) or not isinstance(valor_lista2,(int,float)):
                raise ValueError('Valor inválido')
            nova_lista.append(valor_lista1+valor_lista2)
        except IndexError:
            if i>len(lista1):
                nova_lista=nova_lista+lista2[i:]
            else:
                nova_lista=nova_lista+lista1[i:]

    return nova_lista
l1=[1,2,3,4]
l2=[4,5,6]
a=nova_lista_num(l1,l2)
print(a)