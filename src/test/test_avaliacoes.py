from modulos.avaliacoes import *

def test_criarAvaliacaoSucesso():
    from modulos.musica import adicionarMusica, excluirMusica
    dicionarioAvaliacoes = {}
    adicionarMusica("src/test/musicas_teste/08 - Leslie Parrish - Remember Me.mp3")
        
    resultado = criarAvaliacao("Desconhecido", "08 - Leslie Parrish - Remember Me", 5, "Ótima música!", dicionarioAvaliacoes)
    assert resultado == {
        "codigo_retorno": 1,
        "mensagem": "Avaliação criada com sucesso",
        "avaliacao": {"nota": 5, "texto": "Ótima música!"}
    }
    excluirMusica("Desconhecido", "08 - Leslie Parrish - Remember Me")
    assert len(dicionarioAvaliacoes) == 1

def test_criarAvaliacaoMusicaNaoEncontrada():
    dicionarioAvaliacoes = {}
    resultado = criarAvaliacao("Autor Inexistente", "Música Inexistente", 3, "Avaliação para música inexistente.", dicionarioAvaliacoes)
    assert resultado == {
        "codigo_retorno": 0,
        "mensagem": "Música não encontrada",
        "avaliacao": {}
    }
    assert len(dicionarioAvaliacoes) == 0

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
    }

def test_verificaAvaliacaoExistente():
    dicionarioAvaliacoes = {("Desconhecido", "Música Teste"): {"nota": 5, "texto": "Ótima música!"}}
    resultado = verificaAvaliacao("Desconhecido", "Música Teste", dicionarioAvaliacoes)
    assert resultado == {"codigo_retorno": 1, "mensagem": "Avaliação encontrada"}

def test_verificaAvaliacaoInexistente():
    dicionarioAvaliacoes = {}
    resultado = verificaAvaliacao("Desconhecido", "Música Teste", dicionarioAvaliacoes)
    assert resultado == {"codigo_retorno": 0, "mensagem": "Avaliação inexistente"}

def test_excluirAvaliacaoSucesso():
    dicionarioAvaliacoes = {("Desconhecido", "Música Teste"): {"nota": 5, "texto": "Ótima música!"}}
    resultado = excluirAvaliacao("Desconhecido", "Música Teste", dicionarioAvaliacoes)
    assert resultado == {"codigo_retorno": 1, "mensagem": "Avaliação excluída com sucesso"}
    assert len(dicionarioAvaliacoes) == 0

def test_excluirAvaliacaoInexistente():
    dicionarioAvaliacoes = {}
    resultado = excluirAvaliacao("Desconhecido", "Música Teste", dicionarioAvaliacoes)
    assert resultado == {"codigo_retorno": 0, "mensagem": "Avaliação inexistente"}

def test_atualizaAvaliacaoSucesso():
    dicionarioAvaliacoes = {("Desconhecido", "Música Teste"): {"nota": 5, "texto": "Ótima música!"}}
    resultado = atualizaAvaliacao("Desconhecido", "Música Teste", 4, "Atualização da avaliação.", dicionarioAvaliacoes)
    assert resultado == {"codigo_retorno": 1, "mensagem": "Avaliação atualizada com sucesso"}
    assert dicionarioAvaliacoes[("Desconhecido", "Música Teste")] == {"nota": 4, "texto": "Atualização da avaliação."}

def test_atualizaAvaliacaoInexistente():
    dicionarioAvaliacoes = {}
    resultado = atualizaAvaliacao("Desconhecido", "Música Teste", 4, "Atualização da avaliação.", dicionarioAvaliacoes)
    assert resultado == {"codigo_retorno": 0, "mensagem": "Avaliação inexistente"}

def test_geraStringAvaliacaoSucesso():
    dicionarioAvaliacoes = {("Desconhecido", "Música Teste"): {"nota": 5, "texto": "Ótima música!"}}
    resultado = geraStringAvaliacao("Desconhecido", "Música Teste", dicionarioAvaliacoes)
    assert resultado == {
        "codigo_retorno": 1,
        "stringAvaliacao": "Avaliação do Música Teste do artista Desconhecido\n\n Ótima música! \n\n Nota: 5 estrelas"
    }

def test_geraStringAvaliacaoInexistente():
    dicionarioAvaliacoes = {}
    resultado = geraStringAvaliacao("Desconhecido", "Música Teste", dicionarioAvaliacoes)
    assert resultado == {
        "codigo_retorno": 0,
        "stringAvaliacao": "Erro: Avaliação não encontrada."
    }

