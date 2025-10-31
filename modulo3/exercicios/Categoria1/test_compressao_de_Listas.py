from compressao_de_Lista import lista_de_numeros

import pytest

def test_Listagem_de_numeros():
    lista_teste=['abacate','folha',78,4512,56,True,False]
    assert lista_de_numeros(lista_teste)==[78,4512,56]

def test_verificar_tipagem():
    with pytest.raises(TypeError,match='Tipo Inválido'):
        lista_de_numeros({78,4511212,245,'gjofbh'})