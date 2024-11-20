from modulos.playlist import *
from modulos.musica import verificaMusica

def test_CriarPlaylistSucesso():
    dicionarioPlaylists = {}
    resultado = criarPlaylist("Minha Playlist", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 1, 'mensagem': 'Playlist criada com sucesso'}

def test_CriarPlaylistExistente():
    dicionarioPlaylists = {}
    resultado = criarPlaylist("Minha Playlist", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Erro ao criar a playlist'}

def test_AdicionarMusicaValida():
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    musica_existe = verificaMusica("Desconhecido", "11 - Max Coveri - Running in the 90's")
    resultado = adicionarMusicaNaPlaylist("Minha Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 1, 'mensagem': 'Música adicionada na playlist'}
    assert musica_existe == {'codigo_retorno': 1, 'mensagem': 'Música adicionada com sucesso'}

def test_AdicionarMusicaInexistente():
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    musica_existe = verificaMusica("Autor", "Musica Inexistente")
    resultado = adicionarMusicaNaPlaylist("Minha Playlist", "Autor", "Musica Inexistente", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Música inexistente'}
    assert musica_existe == {'codigo_retorno': 0, 'mensagem': 'Música não existe no dicionário'}

def test_AdicionarMusicaPlaylistInexistente():
    dicionarioPlaylists = {}
    verificaMusica("Desconhecido", "11 - Max Coveri - Running in the 90's")
    resultado = adicionarMusicaNaPlaylist("Playlist inexistente", "Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': -1, 'mensagem': "Playlist inexistente"}

def test_ExcluirMusicaExistente():
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    adicionarMusicaNaPlaylist("Minha Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's")
    resultado = excluirMusicaDaPlaylist("Minha Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's",dicionarioPlaylists)
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
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    adicionarMusicaNaPlaylist("Minha Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioPlaylists)
    resultado = verificarMusicaNaPlaylist("Minha Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioPlaylists)
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