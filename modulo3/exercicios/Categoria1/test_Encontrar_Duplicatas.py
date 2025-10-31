from Encontrar_Duplicatas import encontrar_dupli
import pytest

def test_contagem():
    contador=[2,5,2,5,4,4,'uva','banana','casa','casa','fone','casa']
    assert encontrar_dupli(contador)==[(2,2),(5,2),(4,2),('casa',3)]

def test_tipagem():
    with pytest.raises(TypeError,match='Tipo invalido'):
        encontrar_dupli((1,2,4,57,8,8,'uva'))