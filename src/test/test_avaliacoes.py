from modulos.avaliacoes import *
import os

def test_criarAvaliacaoSucesso():
    from modulos.musica import adicionarMusica, excluirMusica

    dicionarioAvaliacoes = {}
    adicionarMusica("src/test/musicas_teste/08 - Leslie Parrish - Remember Me.mp3")
        
    resultado = criarAvaliacao("Desconhecido", "08 - Leslie Parrish - Remember Me", 5, "Ótima música!", dicionarioAvaliacoes)
    assert resultado == {
        "codigo_retorno": 1,
        "mensagem": "Avaliação criada com sucesso",
        "avaliacao": {"nota": 5, "texto": "Ótima música!"}
    }, "Falha: Avaliação válida não foi criada corretamente."
    excluirMusica("Desconhecido", "08 - Leslie Parrish - Remember Me")
    assert len(dicionarioAvaliacoes) == 1, "Falha: Número de avaliações no dicionário está incorreto."

def test_criarAvaliacaoMusicaNaoEncontrada():
    dicionarioAvaliacoes = {}
    resultado = criarAvaliacao("Autor Inexistente", "Música Inexistente", 3, "Avaliação para música inexistente.", dicionarioAvaliacoes)
    assert resultado == {
        "codigo_retorno": 0,
        "mensagem": "Música não encontrada",
        "avaliacao": {}
    }, "Falha: Avaliação foi criada para música inexistente."
    assert len(dicionarioAvaliacoes) == 0, "Falha: Dicionário de avaliações foi alterado indevidamente."

def test_criarAvaliacaoJaExistente():
    from modulos.musica import adicionarMusica, excluirMusica

    dicionarioAvaliacoes = {("Desconhecido", "08 - Leslie Parrish - Remember Me"): {"nota": 5, "texto": "Ótima música!"}}
    adicionarMusica("src/test/musicas_teste/08 - Leslie Parrish - Remember Me.mp3")

    resultado = criarAvaliacao("Desconhecido", "08 - Leslie Parrish - Remember Me", 4, "Nova avaliação.", dicionarioAvaliacoes)
    excluirMusica("Desconhecido", "08 - Leslie Parrish - Remember Me")
    assert resultado == {
        "codigo_retorno": -1,
        "mensagem": "Avaliação já existente para esta música",
        "avaliacao": {}
    }, "Falha: Avaliação duplicada foi criada indevidamente."

def test_verificaAvaliacaoExistente():
    dicionarioAvaliacoes = {("Desconhecido", "Música Teste"): {"nota": 5, "texto": "Ótima música!"}}
    resultado = verificaAvaliacao("Desconhecido", "Música Teste", dicionarioAvaliacoes)
    assert resultado == {"codigo_retorno": 1, "mensagem": "Avaliação encontrada"}, "Falha: Avaliação existente não foi encontrada."

def test_verificaAvaliacaoInexistente():
    dicionarioAvaliacoes = {}
    resultado = verificaAvaliacao("Desconhecido", "Música Teste", dicionarioAvaliacoes)
    assert resultado == {"codigo_retorno": 0, "mensagem": "Avaliação inexistente"}, "Falha: Avaliação inexistente foi marcada como existente."

def test_excluirAvaliacaoSucesso():
    dicionarioAvaliacoes = {("Desconhecido", "Música Teste"): {"nota": 5, "texto": "Ótima música!"}}
    resultado = excluirAvaliacao("Desconhecido", "Música Teste", dicionarioAvaliacoes)
    assert resultado == {"codigo_retorno": 1, "mensagem": "Avaliação excluída com sucesso"}, "Falha: Avaliação existente não foi excluída corretamente."
    assert len(dicionarioAvaliacoes) == 0, "Falha: Dicionário de avaliações não foi atualizado corretamente após exclusão."

def test_excluirAvaliacaoInexistente():
    dicionarioAvaliacoes = {}
    resultado = excluirAvaliacao("Desconhecido", "Música Teste", dicionarioAvaliacoes)
    assert resultado == {"codigo_retorno": 0, "mensagem": "Avaliação inexistente"}, "Falha: Exclusão de avaliação inexistente retornou um resultado incorreto."

def test_atualizaAvaliacaoSucesso():
    dicionarioAvaliacoes = {("Desconhecido", "Música Teste"): {"nota": 5, "texto": "Ótima música!"}}
    resultado = atualizaAvaliacao("Desconhecido", "Música Teste", 4, "Atualização da avaliação.", dicionarioAvaliacoes)
    assert resultado == {"codigo_retorno": 1, "mensagem": "Avaliação atualizada com sucesso"}, "Falha: Avaliação existente não foi atualizada corretamente."
    assert dicionarioAvaliacoes[("Desconhecido", "Música Teste")] == {"nota": 4, "texto": "Atualização da avaliação."}, "Falha: Conteúdo da avaliação não foi atualizado corretamente."

def test_atualizaAvaliacaoInexistente():
    dicionarioAvaliacoes = {}
    resultado = atualizaAvaliacao("Desconhecido", "Música Teste", 4, "Atualização da avaliação.", dicionarioAvaliacoes)
    assert resultado == {"codigo_retorno": 0, "mensagem": "Avaliação inexistente"}, "Falha: Atualização de avaliação inexistente retornou um resultado incorreto."

def test_geraStringAvaliacaoSucesso():
    dicionarioAvaliacoes = {("Desconhecido", "Música Teste"): {"nota": 5, "texto": "Ótima música!"}}
    resultado = geraStringAvaliacao("Desconhecido", "Música Teste", dicionarioAvaliacoes)
    assert resultado == {
        "codigo_retorno": 1,
        "stringAvaliacao": "Avaliação do Música Teste do artista Desconhecido\n\n Ótima música! \n\n Nota: 5 estrelas"
    }, "Falha: String da avaliação não foi gerada corretamente para uma avaliação existente."

def test_geraStringAvaliacaoInexistente():
    dicionarioAvaliacoes = {}
    resultado = geraStringAvaliacao("Desconhecido", "Música Teste", dicionarioAvaliacoes)
    assert resultado == {
        "codigo_retorno": 0,
        "stringAvaliacao": "Erro: Avaliação não encontrada."
    }, "Falha: Avaliação inexistente não retornou a string de erro esperada."

def test_escreveJsonSucesso():
    from modulos.musica import adicionarMusica, excluirMusica

    adicionarMusica("src/test/musicas_teste/08 - Leslie Parrish - Remember Me.mp3")
    criarAvaliacao("Desconhecido", "08 - Leslie Parrish - Remember Me", 5, "Ótima Música!")

    resultado = escreveJsonAvaliacoes("test")
    assert resultado == {"codigo_retorno": 1, "mensagem": "Arquivo escrito com sucesso"}, "Falha: Arquivo JSON de avaliações não foi escrito com sucesso."
    caminho_arquivo = "src/test/jsons/avaliacoes.json"
    assert os.path.exists(caminho_arquivo), "Falha: Arquivo JSON de avaliações não foi criado."
    os.remove(caminho_arquivo)
    excluirAvaliacao("Desconhecido", "08 - Leslie Parrish - Remember Me")
    excluirMusica("Desconhecido", "08 - Leslie Parrish - Remember Me")
    assert not os.path.exists(caminho_arquivo), "Falha: Arquivo JSON de avaliações não foi apagado após remoção."

def test_escreveJsonFalha():
    resultado = escreveJsonAvaliacoes("test", None)
    assert resultado == {"codigo_retorno": 0, "mensagem": "Erro ao escrever o arquivo, dicionário inexistente."}, "Falha: Retorno esperado para dicionário inexistente não ocorreu."
    caminho_arquivo = "src/test/jsons/avaliacoes.json"
    assert not os.path.exists(caminho_arquivo), "Falha: Arquivo JSON foi criado indevidamente."

def test_leJsonSucesso():
    from modulos.musica import adicionarMusica, excluirMusica
    dicionarioAvaliacoes = {}
    adicionarMusica("src/test/musicas_teste/08 - Leslie Parrish - Remember Me.mp3")
    criarAvaliacao("Desconhecido", "08 - Leslie Parrish - Remember Me", 5, "Ótima Música!")
    escreveJsonAvaliacoes("test")
    excluirAvaliacao("Desconhecido", "08 - Leslie Parrish - Remember Me")
    excluirMusica("Desconhecido", "08 - Leslie Parrish - Remember Me")

    resultado = leJsonAvaliacoes("test", dicionarioAvaliacoes)
    assert resultado == {"codigo_retorno": 1, "mensagem": "Avaliações obtidas com sucesso"}, "Falha: Avaliações não foram obtidas corretamente do arquivo JSON."
    assert geraStringAvaliacao("Desconhecido", "08 - Leslie Parrish - Remember Me", dicionarioAvaliacoes)["codigo_retorno"] == 1, "Falha: Avaliação existente não foi encontrada após leitura do JSON."
    caminho_arquivo = "src/test/jsons/avaliacoes.json"
    os.remove(caminho_arquivo)
    assert not os.path.exists(caminho_arquivo), "Falha: Arquivo JSON de avaliações não foi apagado após leitura."

def test_leJsonFalha():
    caminho_arquivo = "src/test/jsons/avaliacoes.json"
    assert not os.path.exists(caminho_arquivo), "Falha: Arquivo JSON de avaliações existente antes da execução do teste."
    resultado = leJsonAvaliacoes("test")
    assert resultado == {"codigo_retorno": 0, "mensagem": "Erro ao ler o arquivo"}, "Falha: Retorno esperado para leitura de arquivo inexistente não ocorreu."
