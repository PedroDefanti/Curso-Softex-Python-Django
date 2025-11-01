from Transposicao_de_Matriz import transpor
import pytest

def test_transposicao_de_matriz():
    matriz=[[78,89],
            [45,56]]
    assert transpor(matriz)==[[78,45],
                              [89,56]]

def test_tipagem():
    with pytest.raises(TypeError,match='invalido'):
        matriz=(12,45,'hghghghg',78,89)
        transpor(matriz)