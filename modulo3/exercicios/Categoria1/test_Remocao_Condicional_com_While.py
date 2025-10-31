from Remocao_Condicional_com_While import sem_a

import pytest

def test_remocao():
    verificar=['abacate','abelha','indio','fone']
    assert sem_a(verificar)==['indio','fone']