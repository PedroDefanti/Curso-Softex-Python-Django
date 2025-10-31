from Rotacao_de_Lista import rotacao
import pytest

def test_rodar_lista():
    lista=[1,2,3,4,5,6,7,8,9]
    assert rotacao(lista,4)==[6,7,8,9,1,2,3,4,5]

def test_testar_valores():
    with pytest.raises(TypeError,match='Invalido'):
        rotacao(('jgfdngdh'),'h')