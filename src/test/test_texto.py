import os

def test_geraTxtAvaliacoes_tipoCodificacaoInvalido():
    from modulos.texto import geraTxtAvaliacoes
    lista_strings = ["Avaliação 1: Muito bom!", "Avaliação 2: Excelente trabalho."]
    tipo_codificacao = "INVALIDO"  
    resultado = geraTxtAvaliacoes(lista_strings, tipo_codificacao)
    assert resultado == {"codigo_retorno": -1, "mensagem": "Tipo de codificação inválido"}, "Falha: Retorno esperado para tipo de codificação inválido não ocorreu."
    
def test_geraTxtAvaliacoes_utf8():
    from modulos.texto import geraTxtAvaliacoes
    lista_strings = ["Avaliação 1: Muito bom!", "Avaliação 2: Excelente trabalho."]
    tipo_codificacao = "UTF-8"
    relatorios_dir = "src/relatorios"
    caminho_utf8 = os.path.join(relatorios_dir, "avaliacoes_utf8.txt")
    caminho_utf32 = os.path.join(relatorios_dir, "avaliacoes_utf32.txt")

    resultado = geraTxtAvaliacoes(lista_strings, tipo_codificacao)
    assert resultado == {"codigo_retorno": 1, "mensagem": "Relatório de avaliações gerado com sucesso"}, "Falha: Retorno esperado para geração UTF-8 não ocorreu."
    assert os.path.isfile(caminho_utf8), "Falha: Arquivo UTF-8 não foi gerado."
    assert not os.path.isfile(caminho_utf32), "Falha: Arquivo UTF-32 foi gerado indevidamente."
    
    os.remove(caminho_utf8)

def test_geraTxtAvaliacoes_utf32():
    from modulos.texto import geraTxtAvaliacoes
    lista_strings = ["Avaliação 1: Muito bom!", "Avaliação 2: Excelente trabalho."]
    tipo_codificacao = "UTF-32"
    relatorios_dir = "src/relatorios"
    caminho_utf8 = os.path.join(relatorios_dir, "avaliacoes_utf8.txt")
    caminho_utf32 = os.path.join(relatorios_dir, "avaliacoes_utf32.txt")

    resultado = geraTxtAvaliacoes(lista_strings, tipo_codificacao)

    assert resultado == {"codigo_retorno": 1, "mensagem": "Relatório de avaliações gerado com sucesso"}, "Falha: Retorno esperado para geração UTF-32 não ocorreu."
    assert os.path.isfile(caminho_utf32), "Falha: Arquivo UTF-32 não foi gerado."
    assert not os.path.isfile(caminho_utf8), "Falha: Arquivo UTF-8 foi gerado indevidamente."

    os.remove(caminho_utf32)

def test_geraTxtAvaliacoes_lista_vazia():
    from modulos.texto import geraTxtAvaliacoes
    lista_strings = []
    tipo_codificacao = "UTF-8"
    relatorios_dir = "src/relatorios"
    caminho_utf8 = os.path.join(relatorios_dir, "avaliacoes_utf8.txt")
    caminho_utf32 = os.path.join(relatorios_dir, "avaliacoes_utf32.txt")

    resultado = geraTxtAvaliacoes(lista_strings, tipo_codificacao)

    assert resultado == {"codigo_retorno": 1, "mensagem": "Relatório de avaliações gerado com sucesso"}, "Falha: Retorno esperado para lista vazia não ocorreu."
    assert os.path.isfile(caminho_utf8), "Falha: Arquivo UTF-8 não foi gerado para lista vazia."
    assert not os.path.isfile(caminho_utf32), "Falha: Arquivo UTF-32 foi gerado indevidamente para lista vazia."
    os.remove(caminho_utf8)
