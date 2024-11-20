from modulos.avaliacoes import *
import os

def test_criarAvaliacaoSucesso():
    from modulos.musica import adicionarMusica

    dicionarioAvaliacoes = {}
    adicionarMusica("src/test/musicas_teste/08 - Leslie Parrish - Remember Me.mp3")
        
    resultado = criarAvaliacao("Desconhecido", "08 - Leslie Parrish - Remember Me", 5, "Ótima música!", dicionarioAvaliacoes)
    assert resultado == {
        "codigo_retorno": 1,
        "mensagem": "Avaliação criada com sucesso",
        "avaliacao": {"nota": 5, "texto": "Ótima música!"}
    }
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
    from modulos.musica import adicionarMusica

    dicionarioAvaliacoes = {("Desconhecido", "08 - Leslie Parrish - Remember Me"): {"nota": 5, "texto": "Ótima música!"}}
    adicionarMusica("src/test/musicas_teste/08 - Leslie Parrish - Remember Me.mp3")

    resultado = criarAvaliacao("Desconhecido", "08 - Leslie Parrish - Remember Me", 4, "Nova avaliação.", dicionarioAvaliacoes)
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

def test_escreveJsonSucesso():
    from modulos.musica import adicionarMusica

    adicionarMusica("src/test/musicas_teste/08 - Leslie Parrish - Remember Me.mp3")
    criarAvaliacao("Desconhecido", "08 - Leslie Parrish - Remember Me", 5, "Ótima Música!")

    resultado = escreveJsonAvaliacoes("test")
    assert resultado == {"codigo_retorno": 1, "mensagem": "Arquivo escrito com sucesso"}
    caminho_arquivo = "src/test/jsons/avaliacoes.json"
    assert os.path.exists(caminho_arquivo), "O arquivo não foi criado."
    os.remove(caminho_arquivo)
    assert not os.path.exists(caminho_arquivo), "O arquivo não foi apagado."

def test_escreveJsonFalha():
    resultado = escreveJsonAvaliacoes("test", None)
    assert resultado == {"codigo_retorno": 0, "mensagem": "Erro ao escrever o arquivo, dicionário inexistente."}
    caminho_arquivo = "src/test/jsons/avaliacoes.json"
    assert not os.path.exists(caminho_arquivo), "O arquivo foi criado."
 
def test_leJsonSucesso():
    from modulos.musica import adicionarMusica

    adicionarMusica("src/test/musicas_teste/08 - Leslie Parrish - Remember Me.mp3")
    criarAvaliacao("Desconhecido", "08 - Leslie Parrish - Remember Me", 5, "Ótima Música!")
    escreveJsonAvaliacoes("test")
    excluirAvaliacao("Desconhecido", "08 - Leslie Parrish - Remember Me.mp3")

    resultado = leJsonAvaliacoes("test")
    print(resultado)
    assert resultado == {"codigo_retorno": 1, "mensagem":"Avaliações obtidas com sucesso"}
    assert geraStringAvaliacao("Desconhecido", "08 - Leslie Parrish - Remember Me")["codigo_retorno"] == 1
    caminho_arquivo = "src/test/jsons/avaliacoes.json"
    os.remove(caminho_arquivo)
    assert not os.path.exists(caminho_arquivo), "O arquivo não foi apagado."

def test_leJsonFalha():
   caminho_arquivo = "src/test/jsons/avaliacoes.json"
   assert not os.path.exists(caminho_arquivo), "Arquivo existente antes da execução do teste"
   resultado = leJsonAvaliacoes("test")
   assert resultado == {"codigo_retorno": 0, "mensagem": "Erro ao ler o arquivo"}
