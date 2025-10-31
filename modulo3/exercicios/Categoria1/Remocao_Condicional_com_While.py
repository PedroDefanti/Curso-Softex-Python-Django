def sem_a(lista):
    indice=0

    while len(lista)>indice:

        for i in lista:
            
            if 'a' in i:
                lista.remove(i)
            else:
                indice+=1
    return lista
lista=['a','casa','é','bonita','banana','mouse','filme']

a=sem_a(lista)
print(a)
