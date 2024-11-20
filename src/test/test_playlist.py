from modulos.playlist import *
from modulos.musica import verificaMusica

def test_CriarPlaylistSucesso():
    dicionarioPlaylists = {}
    resultado = criarPlaylist("Minha Playlist", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 1, 'mensagem': 'Playlist criada com sucesso'}

def test_CriarPlaylistExistente():
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    resultado = criarPlaylist("Minha Playlist", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Erro ao criar a playlist'}

def test_AdicionarMusicaValida():
    from modulos.musica import adicionarMusica, excluirMusica
    adicionarMusica("src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3")
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    resultado = adicionarMusicaNaPlaylist("Minha Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioPlaylists)
    excluirMusica("Desconhecido", "11 - Max Coveri - Running in the 90's")
    assert resultado == {'codigo_retorno': 1, 'mensagem': 'Música adicionada com sucesso'}
    

def test_AdicionarMusicaInexistente():
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    resultado = adicionarMusicaNaPlaylist("Minha Playlist", "Autor", "Musica Inexistente", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Música inexistente'}

def test_AdicionarMusicaPlaylistInexistente():
    dicionarioPlaylists = {}
    verificaMusica("Desconhecido", "11 - Max Coveri - Running in the 90's")
    resultado = adicionarMusicaNaPlaylist("Playlist inexistente", "Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': -1, 'mensagem': "Playlist inexistente"}

def test_ExcluirMusicaExistente():
    from modulos.musica import adicionarMusica, excluirMusica
    dicionarioPlaylists = {}

    adicionarMusica("src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3")
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    adicionarMusicaNaPlaylist("Minha Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioPlaylists)
    resultado = excluirMusicaDaPlaylist("Minha Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's",dicionarioPlaylists)
    excluirMusica("Desconhecido", "11 - Max Coveri - Running in the 90's")
    assert resultado == {'codigo_retorno': 1, 'mensagem': 'Música removida da playlist'}

def test_ExcluirMusicaInexistente():
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    resultado = excluirMusicaDaPlaylist("Minha Playlist", "Autor", "Musica Inexistente", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Música inexistente'}

def test_ExcluirMusicaPlaylistInexistente():
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    adicionarMusicaNaPlaylist("Minha Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's")
    resultado = excluirMusicaDaPlaylist("Outra Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's",dicionarioPlaylists)
    assert resultado == {'codigo_retorno': -1, 'mensagem': 'Playlist inexistente'}

def test_VerificarMusicaExistente():
    from modulos.musica import adicionarMusica, excluirMusica
    dicionarioPlaylists = {}
    adicionarMusica("src/test/musicas_teste/11 - Max Coveri - Running in the 90's.mp3")
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    adicionarMusicaNaPlaylist("Minha Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioPlaylists)
    resultado = verificarMusicaNaPlaylist("Minha Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioPlaylists)
    excluirMusica("Desconhecido", "11 - Max Coveri - Running in the 90's")
    assert resultado == {'codigo_retorno': 1, 'mensagem': 'Música existe na playlist'}

def test_VerificarMusicaInexistente():
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    resultado = verificarMusicaNaPlaylist("Minha Playlist", "Autor", "Musica Inexistente", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Música não existe na playlist'}

def test_VerificarMusicaPlaylistInexistente():
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    adicionarMusicaNaPlaylist("Minha Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioPlaylists)
    resultado = verificarMusicaNaPlaylist("Outra Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': -1, 'mensagem': 'Playlist inexistente'}

def test_ExcluirPlaylistExistente():
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    resultado = excluirPlaylist("Minha Playlist", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 1, 'mensagem': 'Playlist excluída com sucesso'}

def test_ExcluirPlaylistInexistente():
    dicionarioPlaylists = {}
    resultado = excluirPlaylist("Playlist Inexistente", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Playlist inexistente'}

def test_MudarNomePlaylistSucesso():
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    resultado = mudaNomePlaylist("Minha Playlist", "Novo Nome", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 1, 'mensagem': 'Nome da playlist alterado com sucesso'}

def test_MudarNomePlaylistExistente():
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    resultado = mudaNomePlaylist("Minha Playlist", "Minha Playlist", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Erro ao alterar o nome da playlist'}

def test_MudarNomePlaylistInexistente():
    dicionarioPlaylists = {}
    resultado = mudaNomePlaylist("Playlist inexistente", "Nome Qualquer", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': -1, 'mensagem': 'Playlist não existe'}

def test_escreveJsonPlaylistSucesso():
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    adicionarMusicaNaPlaylist("Minha Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioPlaylists)
    resultado = escreveJsonPlaylists("test", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 1, 'mensagem': "Arquivo escrito com sucesso."}
    caminho_arquivo = "src/test/jsons/playlists.json"
    assert os.path.exists(caminho_arquivo), "O arquivo não foi criado."
    os.remove(caminho_arquivo)
    assert not os.path.exists(caminho_arquivo), "O arquivo não foi apagado."

def test_escreveJsonPlaylistFalha():
    resultado = escreveJsonPlaylists("test", None)
    assert resultado == {"codigo_retorno": 0, "mensagem": "Erro ao escrever o arquivo, dicionário inexistente."}
    caminho_arquivo = "src/test/jsons/playlists.json"
    assert not os.path.exists(caminho_arquivo), "O arquivo foi criado."

def test_leJsonPlaylistSucesso():
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    adicionarMusicaNaPlaylist("Minha Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioPlaylists)
    escreveJsonPlaylists("test", dicionarioPlaylists)
    excluirPlaylist("Minha Playlist", dicionarioPlaylists)
    resultado = leJsonPlaylists("test", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 1, 'mensagem': "Músicas obtidas com sucesso do arquivo."}
    assert verificarMusicaNaPlaylist("Minha Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioPlaylists)['codigo_retorno'] == 1
    caminho_arquivo = "src/test/jsons/playlists.json"
    os.remove(caminho_arquivo)
    assert not os.path.exists(caminho_arquivo), "O arquivo não foi apagado."

def test_leJsonPlaylistFalha():
    caminho_arquivo = "src/test/jsons/playlists.json"
    assert not os.path.exists(caminho_arquivo), "Arquivo existente antes da execução do teste"
    resultado = leJsonPlaylists("test")
    assert resultado == {"codigo_retorno": 0, "mensagem": "Erro ao ler o arquivo"}

def test_obtemPlaylistsSucesso():
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    resultado = obterNomesPlaylists(dicionarioPlaylists)
    assert resultado["codigo_retorno"] == 1
    assert resultado["mensagem"] == "Nomes das playlists obtidos com sucesso."
    assert len(resultado["nomes"]) == 1

def test_obtemPlaylistsFalha():
    resultado = obterNomesPlaylists(None)
    assert resultado == {"codigo_retorno": 0, "nomes": None, "mensagem": "Falha ao obter nomes das playlists"}