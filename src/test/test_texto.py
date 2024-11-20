import os
from modulos.texto import geraTxtAvaliacoes

def test_geraTxtAvaliacoes_tipoCodificacaoInvalido():
    lista_strings = ["Avaliação 1: Muito bom!", "Avaliação 2: Excelente trabalho."]
    tipo_codificacao = "INVALIDO"  
    relatorios_dir = "src/relatorios"
    caminho_utf8 = os.path.join(relatorios_dir, "avaliacoes_utf8.txt")
    caminho_utf32 = os.path.join(relatorios_dir, "avaliacoes_utf32.txt")

    resultado = geraTxtAvaliacoes(lista_strings, tipo_codificacao)

    assert resultado == {"codigo_retorno": -1, "mensagem": "Tipo de codificação inválido"}
#AINDA COM ERRO  
def test_geraTxtAvaliacoes_utf8():
    lista_strings = ["Avaliação 1: Muito bom!", "Avaliação 2: Excelente trabalho."]
    tipo_codificacao = "UTF-8"
    relatorios_dir = "src/relatorios"
    caminho_utf8 = os.path.join(relatorios_dir, "avaliacoes_utf8.txt")
    caminho_utf32 = os.path.join(relatorios_dir, "avaliacoes_utf32.txt")

    resultado = geraTxtAvaliacoes(lista_strings, tipo_codificacao)
    assert resultado == {"codigo_retorno": 1, "mensagem": "Relatório de avaliações gerado com sucesso"}
    assert os.path.isfile(caminho_utf8)  
    assert not os.path.isfile(caminho_utf32)  
    
    os.remove(caminho_utf8)

def test_geraTxtAvaliacoes_utf32():
    lista_strings = ["Avaliação 1: Muito bom!", "Avaliação 2: Excelente trabalho."]
    tipo_codificacao = "UTF-32"
    relatorios_dir = "src/relatorios"
    caminho_utf8 = os.path.join(relatorios_dir, "avaliacoes_utf8.txt")
    caminho_utf32 = os.path.join(relatorios_dir, "avaliacoes_utf32.txt")

    resultado = geraTxtAvaliacoes(lista_strings, tipo_codificacao)

    assert resultado == {"codigo_retorno": 1, "mensagem": "Relatório de avaliações gerado com sucesso"}
    assert os.path.isfile(caminho_utf32) 
    assert not os.path.isfile(caminho_utf8)  

    os.remove(caminho_utf32)

def test_geraTxtAvaliacoes_lista_vazia():
    lista_strings = []
    tipo_codificacao = "UTF-8"
    relatorios_dir = "src/relatorios"
    caminho_utf8 = os.path.join(relatorios_dir, "avaliacoes_utf8.txt")
    caminho_utf32 = os.path.join(relatorios_dir, "avaliacoes_utf32.txt")

    resultado = geraTxtAvaliacoes(lista_strings, tipo_codificacao)

    assert resultado == {"codigo_retorno": 1, "mensagem": "Relatório de avaliações gerado com sucesso"}
    assert os.path.isfile(caminho_utf8)  
    assert not os.path.isfile(caminho_utf32)  
    os.remove(caminho_utf8)