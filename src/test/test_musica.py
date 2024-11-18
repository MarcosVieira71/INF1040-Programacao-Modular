from modulos.musica import *

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
