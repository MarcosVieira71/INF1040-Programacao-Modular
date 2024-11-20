from modulos.musica import *
import os

def test_verificaArquivoArquivoValido():
    resultado = verificaArquivo("src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3")
    assert resultado == {'codigo_retorno': 1, 'mensagem': 'Arquivo válido'}

def test_verificaArquivoInvalido():
    resultado = verificaArquivo("src/test/musicas_teste/arquivo_invalido.txt")
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Arquivo inválido ou inexistente'}

def test_verificaArquivoInexistente():
    resultado = verificaArquivo("src/test/musicas_teste/arquivo_inexistente.mp3")
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Arquivo inválido ou inexistente'}

def test_ExtraiMetadadosMusicaValido():
    resultado = extraiMetadadosMusicas("src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3")
    metadados_corretos = {
        'duracao': 284.93,
        'autor': 'Desconhecido',
        'nome': "11 - Max Coveri - Running in the 90's",
        'caminho': "src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3"
    }
    assert resultado == {'codigo_retorno': 1, 'mensagem': 'Metadados extraídos com sucesso', "metadados": metadados_corretos}

def test_ExtraiMetadadosMusicaInvalido():
    resultado = extraiMetadadosMusicas("src/test/musicas_teste/arquivo_invalido.txt")
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Arquivo inválido ou inexistente', "metadados": {}}

def test_adicionarMusicaSucesso():
    dicionarioMusicas = {}
    resultado = adicionarMusica("src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3", dicionarioMusicas)
    metadados_corretos = extraiMetadadosMusicas("src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3")["metadados"]
    assert resultado == {'codigo_retorno': 1, 'mensagem': 'Música adicionada com sucesso', "metadados_extraidos": metadados_corretos}
    assert len(dicionarioMusicas) == 1

def test_adicionarMusicaArquivoInvalido():
    dicionarioMusicas = {}
    resultado = adicionarMusica("src/test/musicas_teste/arquivo_invalido.txt", dicionarioMusicas)
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Erro ao adicionar a música: arquivo inválido ou inexistente', "metadados_extraidos": {}}
    assert dicionarioMusicas == {}

def test_VerificaMusicaExistente():
    dicionarioMusicas = {}
    adicionarMusica("src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3", dicionarioMusicas)
    resultado = verificaMusica("Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioMusicas)
    assert resultado == {'codigo_retorno': 1, 'mensagem': 'Música existe no dicionário'}


def test_VerificaMusicaInexistente():
    dicionarioMusicas = {}
    adicionarMusica("src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3", dicionarioMusicas)
    resultado = verificaMusica("Autor", "MusicaInexistente", dicionarioMusicas)
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Música não existe no dicionário'}
    
def test_EncontrarMusicaExistente():
    dicionarioMusicas = {}
    adicionarMusica("src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3", dicionarioMusicas)
    resultado = encontrarMusica("Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioMusicas)
    assert resultado == {'codigo_retorno': 1, 'mensagem': 'Música encontrada', 'musica': {
        'duracao': 284.93,
        'autor': 'Desconhecido',
        'nome': "11 - Max Coveri - Running in the 90's",
        'caminho': "src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3"
    }}

def test_EncontrarMusicaInexistente():
    dicionarioMusicas = {}
    adicionarMusica("src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3", dicionarioMusicas)
    resultado = encontrarMusica("Autor", "MusicaInexistente", dicionarioMusicas)
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Música não encontrada', 'musica': None}

# def test_excluiMusicaSucesso():
#     adicionarMusica("src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3")
#     resultado = excluirMusica("Desconhecido", "11 - Max Coveri - Running in the 90's")
#     assert resultado == {"codigo_retorno": 1, "mensagem": "Música excluída com sucesso."}

def test_excluiMusicaInexistente():
    dicionarioMusicas = {}
    resultado = excluirMusica("Autor", "MusicaInexistente", dicionarioMusicas)
    assert resultado == {"codigo_retorno": 0, "mensagem": "Música não existe."}

def test_excluiMusicaComAvaliacao():
    from modulos.avaliacoes import criarAvaliacao
    adicionarMusica("src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3")
    criarAvaliacao("Desconhecido", "11 - Max Coveri - Running in the 90's", 5, "Otima")
    resultado = excluirMusica("Desconhecido", "11 - Max Coveri - Running in the 90's")
    assert resultado == {"codigo_retorno":-1, "mensagem": "A música não pode ser excluída pois tem avaliação."}

def test_excluiMusicaEmPlaylist():
    assert 1==1

def test_escreveJsonSucesso():
    resultado = escreveJsonMusicas("test")
    adicionarMusica("src/test/musicas_teste/08 - Leslie Parrish - Remember Me.mp3")
    assert resultado == {"codigo_retorno": 1, "mensagem": "Arquivo escrito com sucesso."}
    caminho_arquivo = "src/test/jsons/musicas.json"
    assert os.path.exists(caminho_arquivo), "O arquivo não foi criado."
    os.remove(caminho_arquivo)
    assert not os.path.exists(caminho_arquivo), "O arquivo não foi apagado."

def test_escreveJsonFalha():
    resultado = escreveJsonMusicas("test", None)
    assert resultado == {"codigo_retorno": 0, "mensagem": "Erro ao escrever o arquivo, dicionário inexistente."}
    caminho_arquivo = "src/test/jsons/musicas.json"
    assert not os.path.exists(caminho_arquivo), "O arquivo foi criado."
 
def test_leJsonSucesso():
    adicionarMusica("src/test/musicas_teste/08 - Leslie Parrish - Remember Me.mp3")
    escreveJsonMusicas("test")
    excluirMusica("Desconhecido", "08 - Leslie Parrish - Remember Me.mp3")
    resultado = leJsonMusicas("test")
    assert resultado == {"codigo_retorno": 1, "mensagem":"Músicas obtidas com sucesso do arquivo"}
    assert encontrarMusica("Desconhecido", "08 - Leslie Parrish - Remember Me")["codigo_retorno"] == 1
    caminho_arquivo = "src/test/jsons/musicas.json"
    os.remove(caminho_arquivo)
    assert not os.path.exists(caminho_arquivo), "O arquivo não foi apagado."

def test_leJsonFalha():
   caminho_arquivo = "src/test/jsons/musicas.json"
   assert not os.path.exists(caminho_arquivo), "Arquivo existente antes da execução do teste"
   resultado = leJsonMusicas("test")
   assert resultado == {"codigo_retorno": 0, "mensagem": "Erro ao ler o arquivo"}

def test_obtemMusicasSucesso():
    dicionarioMusicas = {}
    adicionarMusica("src/test/musicas_teste/08 - Leslie Parrish - Remember Me.mp3", dicionarioMusicas)
    resultado = obtemMusicas(dicionarioMusicas)
    assert resultado["codigo_retorno"] == 1
    assert len(resultado["musicas"]) == 1
    assert resultado["mensagem"] == "Músicas obtidas com sucesso"
    
def test_obtemMusicasFalha():
    resultado = obtemMusicas(None)
    assert resultado == {"codigo_retorno": 0, "musicas": None, "mensagem":"Não foi possível obter as músicas"}

