
def transpor(lista:list)-> list[int]:
    if isinstance(lista,list):
        mn=[]
        for i in range(len(lista[0])):
            nova_linha=[]
            
            for j in range(len(lista)):
                elemento=lista[j][i]
                nova_linha.append(elemento)
            mn.append(nova_linha)
        return mn
    else:
        raise TypeError('invalido')

lista = [
    [10, 20, 30, 40,78,89,45,56],
    [50, 60, 70, 80,12,32,21,65],
    [90, 10, 20, 30,54,98,87,52],
    [96, 63, 85, 52,74,41,14,47]
]

a=transpor(lista)
for i in a:
    print(i)