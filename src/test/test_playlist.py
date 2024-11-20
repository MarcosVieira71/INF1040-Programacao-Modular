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