from modulos.playlist import *
from modulos.musica import verificaMusica

def testarCriarPlaylistSucesso():
    dicionarioPlaylists = {}
    resultado = criarPlaylist("Minha Playlist", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 1, 'mensagem': 'Playlist criada com sucesso'}

def testarCriarPlaylistExistente():
    dicionarioPlaylists = {}
    resultado = criarPlaylist("Minha Playlist", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Erro ao criar a playlist'}

def testarAdicionarMusicaValida():
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    musica_existe = verificaMusica("Desconhecido", "11 - Max Coveri - Running in the 90's")
    resultado = adicionarMusicaNaPlaylist("Minha Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 1, 'mensagem': 'Música adicionada na playlist'}
    assert musica_existe == {'codigo_retorno': 1, 'mensagem': 'Música existe no dicionário'}

def testarAdicionarMusicaInexistente():
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    musica_existe = verificaMusica("Autor", "Musica Inexistente")
    resultado = adicionarMusicaNaPlaylist("Minha Playlist", "Autor", "Musica Inexistente", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Música inexistente'}
    assert musica_existe == {'codigo_retorno': 0, 'mensagem': 'Música não existe no dicionário'}

def testarAdicionarMusicaPlaylistInexistente():
    dicionarioPlaylists = {}
    verificaMusica("Desconhecido", "11 - Max Coveri - Running in the 90's")
    resultado = adicionarMusicaNaPlaylist("Playlist inexistente", "Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': -1, 'mensagem': "Playlist inexistente"}

def testarExcluirMusicaExistente():
    dicionarioPlaylists = {}
    adicionarMusicaNaPlaylist("Minha Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's")
    resultado = excluirMusicaDaPlaylist("Minha Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's",dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 1, 'mensagem': 'Música removida da playlist'}

def testarExcluirMusicaInexistente():
    dicionarioPlaylists = {}
    resultado = excluirMusicaDaPlaylist("Minha Playlist", "Autor", "Musica Inexistente", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Música ou playlist inexistente'}

def testarVerificarMusicaExistente():
    dicionarioPlaylists = {}
    adicionarMusicaNaPlaylist("Minha Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioPlaylists)
    resultado = verificarMusicaNaPlaylist("Minha Playlist", "Desconhecido", "11 - Max Coveri - Running in the 90's", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 1, 'mensagem': 'Música existe na playlist'}

def testarVerificarMusicaInexistente():
    dicionarioPlaylists = {}
    resultado = verificarMusicaNaPlaylist("Minha Playlist", "Autor", "Musica Inexistente", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Música não existe na playlist'}

def testarExcluirPlaylistExistente():
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    resultado = excluirPlaylist("Minha Playlist", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 1, 'mensagem': 'Playlist excluída com sucesso'}

def testarExcluirPlaylistInexistente():
    dicionarioPlaylists = {}
    resultado = excluirPlaylist("Playlist Inexistente", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Playlist inexistente'}

def testarMudarNomePlaylistSucesso():
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    resultado = mudaNomePlaylist("Minha Playlist", "Novo Nome", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 1, 'mensagem': 'Nome da playlist alterado com sucesso'}

def testarMudarNomePlaylistExistente():
    dicionarioPlaylists = {}
    criarPlaylist("Minha Playlist", dicionarioPlaylists)
    resultado = mudaNomePlaylist("Minha Playlist", "Minha Playlist", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Erro ao alterar o nome da playlist'}

def testarMudarNomePlaylistInexistente():
    dicionarioPlaylists = {}
    resultado = mudaNomePlaylist("Playlist inexistente", "Nome Qualquer", dicionarioPlaylists)
    assert resultado == {'codigo_retorno': -1, 'mensagem': 'Playlist não existe'}