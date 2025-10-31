def encontrar_dupli(lista:list)->list[tuple]:
    if not isinstance(lista,list):
        raise TypeError('Tipo invalido')
    else:
        lista_ndupli=[]
        lista_dupli=[]
        lista_dupli_e_contador=[]
        for i in lista:
            if i in lista_ndupli:
                lista_dupli.append(i)
                
            else:
                lista_ndupli.append(i)
        for i in lista_dupli:
            if i in lista_dupli_e_contador:
                None
            else:
                lista_dupli_e_contador.append(i)
                
                count=lista_dupli.count(i)
                
                x=(i,(count+1))
                lista_dupli_e_contador.append(x)
        for i in lista_dupli_e_contador:
            if not isinstance(i,tuple):
                lista_dupli_e_contador.remove(i)
    
    

    return lista_dupli_e_contador

lista=[1,2,3,4,2,4,4,'abacate','uva','uva','uva',4,2,'maça']

x=encontrar_dupli(lista)
print(x)
            
