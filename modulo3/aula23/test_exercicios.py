from exercicios import criacao,contar_letras


def test_criacao():
    assert criacao([1,2,3,4,5],[5,4,8,9])=={1,2,3,4,5,8,9}

def test_contar():
    assert contar_letras('banana')==  'A frase banana contém: CONSOANTES: 3 VOGAIS: 3'
