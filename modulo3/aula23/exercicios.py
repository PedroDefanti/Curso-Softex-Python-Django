#Interseção de Listas
def criacao(l1,l2):
    nova_lista1=set(l1)
    nova_lista2=set(l2)
    uniao=nova_lista1.union(nova_lista2)
    return uniao

x=criacao([1,2,3,4,5],[5,4,8,9])
print(x)



    

# def verificacao( lado_A,lado_B,lado_C):
#        if not lado_A.isdigit() or not lado_B.isdigit() or not lado_C.isdigit():
#            print('Você não digitou o número de maneira correta.Tente novamente.')
#        else:
#             lado_a=abs(int(lado_A))
#             lado_b=abs(int(lado_B))
#             lado_c=abs(int(lado_C))
#             if lado_a<=0 or  lado_b <=0 or  lado_c<=0:
#                 print('Todos os números 0 ou menores que ele não são permitidos.')
#             else:
#                 print('Os números são capazes de ser tornar um triângulo') if  lado_a<lado_b + lado_c and lado_b< lado_a + lado_c and lado_c< lado_a + lado_b and  lado_a>lado_b - lado_c and lado_b> lado_a - lado_c and lado_c> lado_a - lado_b else print('Os números não são capazes de ser tornar um triângulo')


def contar_letras(frase):
        vogais='aeiou'
        cont_consoantes=0
        cont_vogais=0
        frase_sem_espacos=frase.lower().replace(' ','')
        for i in frase_sem_espacos:
            if i in vogais:
                cont_vogais+=1
            else:
                cont_consoantes+=1
        return f'A frase {frase} contém:\n CONSOANTES: {cont_consoantes}\n VOGAIS: {cont_vogais}'

x=contar_letras('banana')
print(x)

