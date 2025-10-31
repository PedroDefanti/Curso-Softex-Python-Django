from Intersecao_de_Listas import receber
import pytest

def test_listas(mocker):
    resultado=[1,2,3,
               4,2,1]
    mock=mocker.patch('random.randint',side_effect=resultado)
    l01=[mock(1,5) for _ in range(3)]
    l02=[mock(1,5) for _ in range(3)]
    
    assert receber(l01,l02)==[1,2]
    
    
def test_elemento_um():
    with pytest.raises(TypeError,match='Não passou uma lista'):
        receber('fdfffff',[1,2])