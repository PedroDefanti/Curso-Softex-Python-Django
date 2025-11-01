def fatiamento(lista:list,inicio:int,final:int):
    if not isinstance(lista,list):
        raise TypeError('Tipagem errada')
    elif not isinstance(inicio,int) or not isinstance(final,int):
        raise ValueError('Valor errado')
    if inicio>final:
        novo_inicio=final
        novo_final=inicio
        return lista[novo_inicio:novo_final]
    
    return lista[inicio:final]

