from fatiamento_Circular import fatiamento
import pytest

def test_de_fatiamneto():
    lista=[1,2,3,4,5,6,7,8,9]
    inicio=3
    final=7
    assert fatiamento(lista,inicio,final)==[4,5,6,7]

def test_de_tipagem():
    lista=(1,2,3,4,5,6,7,8,9)
    inicio=3
    final=7
    with pytest.raises(TypeError,match='Tipagem errada'):
         fatiamento(lista,inicio,final)
         
def test_de_valores():
    lista=[1,2,3,4,5,6,7,8,9]
    inicio='aaaaaa'
    final=7
    with pytest.raises(ValueError,match='Valor errado'):
         fatiamento(lista,inicio,final)