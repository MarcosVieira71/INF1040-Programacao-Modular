import modulos.avaliacoes as avaliacoes
import modulos.musica as musica
from modulos.auxiliarJson import *

dicionarioPlaylists = {}

def criarPlaylist(nomePlaylist:str, dicionarioPlaylists = dicionarioPlaylists):
    if nomePlaylist in dicionarioPlaylists:
        resultado = {
        "codigo_retorno": 0,
        "mensagem": "Erro ao criar a playlist"
        }
    else:
        resultado = {
        "codigo_retorno": 1,
        "mensagem": "Playlist criada com sucesso"
        }
        dicionarioPlaylists[nomePlaylist] = []
    return resultado

def adicionarMusicaNaPlaylist(nomePlaylist:str, nomeAutor:str, nomeMusica:str, dicionarioPlaylists = dicionarioPlaylists):
    return 0

def excluirMusicaDaPlaylist(nomePlaylist:str, nomeAutor:str, nomeMusica:str, dicionarioPlaylists = dicionarioPlaylists):
    return 0

def verificarMusicaNaPlaylist(nomePlaylist:str, nomeAutor:str, nomeMusica:str, dicionarioPlaylists = dicionarioPlaylists):
    return 0

def excluirPlaylist(nomePlaylist:str, dicionarioPlaylists = dicionarioPlaylists):
    return 0

def mudaNomePlaylist(nomePlaylist:str, novoNome:str, dicionarioPlaylists = dicionarioPlaylists):
    if nomePlaylist in dicionarioPlaylists:
        if novoNome == nomePlaylist:
            resultado = {
                'codigo_retorno': 0,
                'mensagem': 'Erro ao alterar o nome da playlist'
            }
        else:
            aux = dicionarioPlaylists[nomePlaylist]
            del dicionarioPlaylists[nomePlaylist]
            dicionarioPlaylists[novoNome] = aux
            resultado = {
                'codigo_retorno': 1,
                'mensagem': 'Nome da playlist alterado com sucesso'
            }
    else:
        resultado = {
        'codigo_retorno': -1, 
        'mensagem': 'Playlist não existe'
        }
    return resultado