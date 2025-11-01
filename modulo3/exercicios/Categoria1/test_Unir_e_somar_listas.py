from unir_e_somar_listas import nova_lista_num
import pytest

def test_unir_e_somar():
    l1=[1,2,3,7,7,8]
    l2=[4,5,6]
    nova_lista_num(l1,l2)==[5,7,9]

def test_valores():
    l1=[1,2,'aaaa']
    l2=[4,5,6]
    with pytest.raises(ValueError,match='Valor inválido'):
        nova_lista_num(l1,l2)

def test_tipagem():
    l1=(4,5,6)
    l2=(4,5,6)
    with pytest.raises(TypeError,match='Tipo inválido'):
        nova_lista_num(l1,l2)