def lista_de_numeros(lista:list)->list[int]:
    if isinstance(lista,list):
        lista_num=[]
        for i in lista:
            if isinstance(i,int) and not isinstance(i,bool):
                lista_num.append(i)
        return lista_num
    else:
        raise TypeError('Tipo Inválido')
    
