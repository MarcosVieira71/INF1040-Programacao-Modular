from modulos.playlist import *
import os

def test_CriarPlaylistSucesso():
    dicionarioPlaylists = {}
    resultado = criarPlaylist("Minha Playlist", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 1, 'mensagem': 'Playlist criada com sucesso'}, "Falha: A playlist não foi criada com sucesso."

def test_CriarPlaylistExistente():
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    resultado = criarPlaylist("Minha Playlist", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Erro ao criar a playlist'}, "Falha: Não foi retornado erro para playlist existente."

def test_AdicionarMusicaValida():
    from modulos.musica import adicionarMusica, excluirMusica
    adicionarMusica("src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3")
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    resultado = adicionarMusicaNaPlaylist("Minha Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioPlaylists)
    excluirMusica("Desconhecido", "11 - Max Coveri - Running in the 90's")
    assert resultado == {'codigo_retorno': 1, 'mensagem': 'Música adicionada com sucesso'}, "Falha: Música válida não foi adicionada à playlist."

def test_AdicionarMusicaInexistente():
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    resultado = adicionarMusicaNaPlaylist("Minha Playlist", "Autor", "Musica Inexistente", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Música inexistente'}, "Falha: Não foi retornado erro para música inexistente."

def test_AdicionarMusicaPlaylistInexistente():
    dicionarioPlaylists = {}
    resultado = adicionarMusicaNaPlaylist("Playlist inexistente", "Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': -1, 'mensagem': "Playlist inexistente"}, "Falha: Não foi retornado erro para playlist inexistente."

def test_ExcluirMusicaExistente():
    from modulos.musica import adicionarMusica, excluirMusica
    dicionarioPlaylists = {}

    adicionarMusica("src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3")
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    adicionarMusicaNaPlaylist("Minha Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioPlaylists)
    resultado = excluirMusicaDaPlaylist("Minha Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioPlaylists)
    excluirMusica("Desconhecido", "11 - Max Coveri - Running in the 90's")
    assert resultado == {'codigo_retorno': 1, 'mensagem': 'Música removida da playlist'}, "Falha: Música existente não foi removida da playlist."

def test_ExcluirMusicaInexistente():
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    resultado = excluirMusicaDaPlaylist("Minha Playlist", "Autor", "Musica Inexistente", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Música inexistente'}, "Falha: Não foi retornado erro para música inexistente."

def test_ExcluirMusicaPlaylistInexistente():
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    adicionarMusicaNaPlaylist("Minha Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's")
    resultado = excluirMusicaDaPlaylist("Outra Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': -1, 'mensagem': 'Playlist inexistente'}, "Falha: Não foi retornado erro para playlist inexistente ao excluir música."

def test_VerificarMusicaExistente():
    from modulos.musica import adicionarMusica, excluirMusica
    dicionarioPlaylists = {}
    adicionarMusica("src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3")
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    adicionarMusicaNaPlaylist("Minha Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioPlaylists)
    resultado = verificarMusicaNaPlaylist("Minha Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioPlaylists)
    excluirMusica("Desconhecido", "11 - Max Coveri - Running in the 90's")
    assert resultado == {'codigo_retorno': 1, 'mensagem': 'Música existe na playlist'}, "Falha: Música existente não foi encontrada na playlist."

def test_VerificarMusicaInexistente():
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    resultado = verificarMusicaNaPlaylist("Minha Playlist", "Autor", "Musica Inexistente", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Música não existe na playlist'}, "Falha: Música inexistente foi marcada como existente."

def test_VerificarMusicaPlaylistInexistente():
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    adicionarMusicaNaPlaylist("Minha Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioPlaylists)
    resultado = verificarMusicaNaPlaylist("Outra Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': -1, 'mensagem': 'Playlist inexistente'}, "Falha: Não foi retornado erro para verificação em playlist inexistente."

def test_ExcluirPlaylistExistente():
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    resultado = excluirPlaylist("Minha Playlist", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 1, 'mensagem': 'Playlist excluída com sucesso'}, "Falha: Playlist existente não foi excluída com sucesso."

def test_ExcluirPlaylistInexistente():
    dicionarioPlaylists = {}
    resultado = excluirPlaylist("Playlist Inexistente", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Playlist inexistente'}, "Falha: Não foi retornado erro para exclusão de playlist inexistente."

def test_MudarNomePlaylistSucesso():
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    resultado = mudaNomePlaylist("Minha Playlist", "Novo Nome", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 1, 'mensagem': 'Nome da playlist alterado com sucesso'}, "Falha: Nome da playlist não foi alterado com sucesso."

def test_MudarNomePlaylistExistente():
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    resultado = mudaNomePlaylist("Minha Playlist", "Minha Playlist", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Erro ao alterar o nome da playlist'}, "Falha: Nome da playlist foi alterado indevidamente para um nome já existente."

def test_MudarNomePlaylistInexistente():
    dicionarioPlaylists = {}
    resultado = mudaNomePlaylist("Playlist inexistente", "Nome Qualquer", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': -1, 'mensagem': 'Playlist não existe'}, "Falha: Nome da playlist inexistente foi alterado."

def test_escreveJsonPlaylistSucesso():
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    adicionarMusicaNaPlaylist("Minha Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioPlaylists)
    resultado = escreveJsonPlaylists("test", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 1, 'mensagem': "Arquivo escrito com sucesso."}, "Falha: Arquivo JSON não foi escrito com sucesso."
    caminho_arquivo = "src/test/jsons/playlists.json"
    assert os.path.exists(caminho_arquivo), "Falha: Arquivo JSON não foi criado."
    os.remove(caminho_arquivo)
    assert not os.path.exists(caminho_arquivo), "Falha: Arquivo JSON não foi apagado após remoção."

def test_escreveJsonPlaylistFalha():
    resultado = escreveJsonPlaylists("test", None)
    assert resultado == {"codigo_retorno": 0, "mensagem": "Erro ao escrever o arquivo, dicionário inexistente."}, "Falha: Retorno esperado ao escrever dicionário inexistente não ocorreu."
    caminho_arquivo = "src/test/jsons/playlists.json"
    assert not os.path.exists(caminho_arquivo), "Falha: Arquivo JSON foi criado indevidamente."

def test_leJsonPlaylistSucesso():
    from modulos.musica import adicionarMusica, excluirMusica
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    
    adicionarMusica("src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3")
    adicionarMusicaNaPlaylist("Minha Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioPlaylists)
    
    escreveJsonPlaylists("test", dicionarioPlaylists)
    excluirPlaylist("Minha Playlist", dicionarioPlaylists)

    resultado = leJsonPlaylists("test", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 1, 'mensagem': "Músicas obtidas com sucesso do arquivo."}, "Falha: Músicas não foram obtidas com sucesso do arquivo JSON."
    assert verificarMusicaNaPlaylist("Minha Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioPlaylists)['codigo_retorno'] == 1, "Falha: Música existente não foi encontrada na playlist após leitura."
    caminho_arquivo = "src/test/jsons/playlists.json"
    os.remove(caminho_arquivo)
    excluirMusica("Desconhecido", "11 - Max Coveri - Running in the 90's")
    assert not os.path.exists(caminho_arquivo), "Falha: Arquivo JSON não foi apagado após leitura."

def test_leJsonPlaylistFalha():
    caminho_arquivo = "src/test/jsons/playlists.json"
    assert not os.path.exists(caminho_arquivo), "Falha: Arquivo JSON existente antes da execução do teste."
    resultado = leJsonPlaylists("test")
    assert resultado == {"codigo_retorno": 0, "mensagem": "Erro ao ler o arquivo"}, "Falha: Não foi retornado erro ao tentar ler um arquivo inexistente."

def test_obtemNomePlaylistsSucesso():
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    resultado = obterNomesPlaylists(dicionarioPlaylists)
    assert resultado["codigo_retorno"] == 1, "Falha: Código de retorno para obtenção de nomes das playlists não é o esperado."
    assert resultado["mensagem"] == "Nomes das playlists obtidos com sucesso.", "Falha: Mensagem de sucesso não foi retornada."
    assert len(resultado["nomes"]) == 1, "Falha: Número de nomes retornados é incorreto."

def test_obtemNomePlaylistsFalha():
    resultado = obterNomesPlaylists(None)
    assert resultado == {"codigo_retorno": 0, "nomes": None, "mensagem": "Falha ao obter nomes das playlists"}, "Falha: Retorno esperado para dicionário inexistente não ocorreu."

def test_obtemMusicasDePlaylistSucesso():
    from modulos.musica import adicionarMusica, excluirMusica
    adicionarMusica("src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3")
    
    nomePlaylist = "Playlist real"
    dicionarioPlaylists = {}
    criarPlaylist(nomePlaylist, dicionarioPlaylists)
    adicionarMusicaNaPlaylist("Playlist real", "Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioPlaylists)
    resultado = obtemMusicasDePlaylist("Playlist real", dicionarioPlaylists)
    excluirMusica("Desconhecido", "11 - Max Coveri - Running in the 90's")
    assert resultado == {"codigo_retorno": 1, "musicas": dicionarioPlaylists[nomePlaylist], "mensagem": "Músicas obtidas com sucesso"}, "Falha: Músicas não foram obtidas com sucesso da playlist."

def test_obtemMusicasDePlaylistFalha():
    dicionarioPlaylists = {}
    nomePlaylist = "Playlist inventada"
    resultado = obtemMusicasDePlaylist(nomePlaylist, dicionarioPlaylists)
    assert resultado == {"codigo_retorno": 0, "musicas": None, "mensagem": "Não foi possível obter as músicas da playlist"}, "Falha: Retorno esperado para playlist inexistente não ocorreu."
