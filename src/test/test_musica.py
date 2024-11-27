from modulos.musica import *
import os

def test_verificaArquivoArquivoValido():
    resultado = verificaArquivo("src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3")
    assert resultado == {'codigo_retorno': 1, 'mensagem': 'Arquivo válido'}, "Falha: Arquivo válido não foi reconhecido como tal."

def test_verificaArquivoInvalido():
    resultado = verificaArquivo("src/test/musicas_teste/arquivo_invalido.txt")
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Arquivo inválido ou inexistente'}, "Falha: Arquivo inválido não foi identificado corretamente."

def test_verificaArquivoInexistente():
    resultado = verificaArquivo("src/test/musicas_teste/arquivo_inexistente.mp3")
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Arquivo inválido ou inexistente'}, "Falha: Arquivo inexistente não foi identificado corretamente."

def test_ExtraiMetadadosMusicaValido():
    resultado = extraiMetadadosMusicas("src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3")
    metadados_corretos = {
        'duracao': 284.93,
        'autor': 'Desconhecido',
        'nome': "11 - Max Coveri - Running in the 90's",
        'caminho': "src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3"
    }
    assert resultado == {'codigo_retorno': 1, 'mensagem': 'Metadados extraídos com sucesso', "metadados": metadados_corretos}, "Falha: Metadados não foram extraídos corretamente de um arquivo válido."

def test_ExtraiMetadadosMusicaInvalido():
    resultado = extraiMetadadosMusicas("src/test/musicas_teste/arquivo_invalido.txt")
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Arquivo inválido ou inexistente', "metadados": {}}, "Falha: Arquivo inválido retornou metadados incorretos."

def test_adicionarMusicaSucesso():
    dicionarioMusicas = {}
    resultado = adicionarMusica("src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3", dicionarioMusicas)
    metadados_corretos = extraiMetadadosMusicas("src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3")["metadados"]
    assert resultado == {'codigo_retorno': 1, 'mensagem': 'Música adicionada com sucesso', "metadados_extraidos": metadados_corretos}, "Falha: Música válida não foi adicionada corretamente."
    assert len(dicionarioMusicas) == 1, "Falha: O número de músicas no dicionário é incorreto após adição."

def test_adicionarMusicaArquivoInvalido():
    dicionarioMusicas = {}
    resultado = adicionarMusica("src/test/musicas_teste/arquivo_invalido.txt", dicionarioMusicas)
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Erro ao adicionar a música: arquivo inválido ou inexistente', "metadados_extraidos": {}}, "Falha: Arquivo inválido foi adicionado incorretamente."
    assert dicionarioMusicas == {}, "Falha: Dicionário de músicas foi alterado indevidamente."

def test_adicionarMusicaExistente():
    adicionarMusica("src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3")
    resultado = adicionarMusica("src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3")
    excluirMusica("Desconhecido", "11 - Max Coveri - Running in the 90's")
    assert resultado == {"codigo_retorno": -1, "mensagem": "Música já existente.", "metadados_extraidos": {}}, "Falha: Música duplicada foi adicionada incorretamente."

def test_VerificaMusicaExistente():
    dicionarioMusicas = {}
    adicionarMusica("src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3", dicionarioMusicas)
    resultado = verificaMusica("Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioMusicas)
    assert resultado == {'codigo_retorno': 1, 'mensagem': 'Música existe no dicionário'}, "Falha: Música existente não foi encontrada no dicionário."

def test_VerificaMusicaInexistente():
    dicionarioMusicas = {}
    adicionarMusica("src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3", dicionarioMusicas)
    resultado = verificaMusica("Autor", "MusicaInexistente", dicionarioMusicas)
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Música não existe no dicionário'}, "Falha: Música inexistente foi encontrada indevidamente no dicionário."

def test_EncontrarMusicaExistente():
    dicionarioMusicas = {}
    adicionarMusica("src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3", dicionarioMusicas)
    resultado = encontrarMusica("Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioMusicas)
    assert resultado == {'codigo_retorno': 1, 'mensagem': 'Música encontrada', 'musica': {
        'duracao': 284.93,
        'autor': 'Desconhecido',
        'nome': "11 - Max Coveri - Running in the 90's",
        'caminho': "src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3"
    }}, "Falha: Música existente não foi encontrada corretamente."

def test_EncontrarMusicaInexistente():
    dicionarioMusicas = {}
    adicionarMusica("src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3", dicionarioMusicas)
    resultado = encontrarMusica("Autor", "MusicaInexistente", dicionarioMusicas)
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Música não encontrada', 'musica': None}, "Falha: Música inexistente foi encontrada indevidamente."

def test_excluiMusicaSucesso():
    adicionarMusica("src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3")
    resultado = excluirMusica("Desconhecido", "11 - Max Coveri - Running in the 90's")
    assert resultado == {"codigo_retorno": 1, "mensagem": "Música excluída com sucesso."}, "Falha: Música existente não foi excluída corretamente."

def test_excluiMusicaInexistente():
    dicionarioMusicas = {}
    resultado = excluirMusica("Autor", "MusicaInexistente", dicionarioMusicas)
    assert resultado == {"codigo_retorno": 0, "mensagem": "Música não existe."}, "Falha: Exclusão de música inexistente retornou um resultado incorreto."

def test_excluiMusicaComAvaliacao():
    from modulos.avaliacoes import criarAvaliacao, excluirAvaliacao
    adicionarMusica("src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3")
    criarAvaliacao("Desconhecido", "11 - Max Coveri - Running in the 90's", 5, "Otima")
    resultado = excluirMusica("Desconhecido", "11 - Max Coveri - Running in the 90's")
    assert resultado == {"codigo_retorno":-1, "mensagem": "A música não pode ser excluída pois tem avaliação."}, "Falha: Música com avaliação foi excluída indevidamente."
    excluirAvaliacao("Desconhecido","11 - Max Coveri - Running in the 90's")
    excluirMusica("Desconhecido", "11 - Max Coveri - Running in the 90's")

def test_excluiMusicaEmPlaylist():
    from modulos.playlist import criarPlaylist, adicionarMusicaNaPlaylist, excluirPlaylist
    adicionarMusica("src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3")
    criarPlaylist("Playlist Nova")

    adicionarMusicaNaPlaylist("Playlist Nova", "Desconhecido", "11 - Max Coveri - Running in the 90's")
    resultado = excluirMusica("Desconhecido", "11 - Max Coveri - Running in the 90's")
    excluirPlaylist("Playlist Nova")
    excluirMusica("Desconhecido", "11 - Max Coveri - Running in the 90's")
    assert resultado == {"codigo_retorno": -2, "mensagem": "A música não pode ser excluída pois está em uma playlist."}, "Falha: Música em playlist foi excluída indevidamente."

def test_escreveJsonSucesso():
    dicionarioMusicas = {}
    adicionarMusica("src/test/musicas_teste/08 - Leslie Parrish - Remember Me.mp3", dicionarioMusicas)
    resultado = escreveJsonMusicas("test", dicionarioMusicas)
    assert resultado == {"codigo_retorno": 1, "mensagem": "Arquivo escrito com sucesso."}, "Falha: Arquivo JSON não foi escrito com sucesso."
    caminho_arquivo = "src/test/jsons/musicas.json"
    assert os.path.exists(caminho_arquivo), "Falha: Arquivo JSON não foi criado."
    os.remove(caminho_arquivo)
    assert not os.path.exists(caminho_arquivo), "Falha: Arquivo JSON não foi apagado após remoção."

def test_leJsonSucesso():
    dicionarioMusicas = {}
    adicionarMusica("src/test/musicas_teste/08 - Leslie Parrish - Remember Me.mp3", dicionarioMusicas)
    escreveJsonMusicas("test", dicionarioMusicas)
    excluirMusica("Desconhecido", "08 - Leslie Parrish - Remember Me.mp3", dicionarioMusicas)
    resultado = leJsonMusicas("test", dicionarioMusicas)
    assert resultado == {"codigo_retorno": 1, "mensagem": "Músicas obtidas com sucesso do arquivo"}, "Falha: Músicas não foram obtidas corretamente do arquivo JSON."
    assert encontrarMusica("Desconhecido", "08 - Leslie Parrish - Remember Me", dicionarioMusicas)["codigo_retorno"] == 1, "Falha: Música existente não foi encontrada após leitura do JSON."
    caminho_arquivo = "src/test/jsons/musicas.json"
    os.remove(caminho_arquivo)
    assert not os.path.exists(caminho_arquivo), "Falha: Arquivo JSON não foi apagado após leitura."

def test_leJsonFalha():
    caminho_arquivo = "src/test/jsons/musicas.json"
    assert not os.path.exists(caminho_arquivo), "Falha: Arquivo JSON existente antes da execução do teste."
    resultado = leJsonMusicas("test")
    assert resultado == {"codigo_retorno": 0, "mensagem": "Erro ao ler o arquivo"}, "Falha: Não foi retornado erro ao tentar ler um arquivo inexistente."

def test_obtemMusicasSucesso():
    dicionarioMusicas = {}
    adicionarMusica("src/test/musicas_teste/08 - Leslie Parrish - Remember Me.mp3", dicionarioMusicas)
    resultado = obtemMusicas(dicionarioMusicas)
    assert resultado["codigo_retorno"] == 1, "Falha: Código de retorno para obtenção de músicas não é o esperado."
    assert len(resultado["musicas"]) == 1, "Falha: Número de músicas obtidas é incorreto."
    assert resultado["mensagem"] == "Músicas obtidas com sucesso", "Falha: Mensagem de sucesso não foi retornada."

def test_obtemMusicasFalha():
    resultado = obtemMusicas(None)
    assert resultado == {"codigo_retorno": 0, "musicas": None, "mensagem": "Não foi possível obter as músicas"}, "Falha: Retorno esperado para dicionário inexistente não ocorreu."
