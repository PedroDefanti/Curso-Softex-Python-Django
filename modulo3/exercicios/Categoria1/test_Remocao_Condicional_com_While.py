from Remocao_Condicional_com_While import sem_a

import pytest

def test_remocao():
    verificar=['abacate','abelha','indio','fone']
    assert sem_a(verificar)==['indio','fone']
    
def test_erro_de_tipo():
    with pytest.raises(TypeError,match='Erro'):
        sem_a(('abacate','abelha','indio','fone'))