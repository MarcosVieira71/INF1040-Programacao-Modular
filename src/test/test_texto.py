import os
from modulos.texto import geraTxtAvaliacoes

def test_geraTxtAvaliacoes_tipoCodificacaoInvalido():
    lista_strings = ["Avaliação 1: Muito bom!", "Avaliação 2: Excelente trabalho."]
    tipo_codificacao = "INVALIDO"  
    relatorios_dir = "src/relatorios"
    caminho_utf8 = os.path.join(relatorios_dir, "avaliacoes_utf8.txt")
    caminho_utf32 = os.path.join(relatorios_dir, "avaliacoes_utf32.txt")

    resultado = geraTxtAvaliacoes(lista_strings, tipo_codificacao)

    assert resultado == {"codigo_retorno": 0, "mensagem": "Tipo de codificação inválido"}
    
