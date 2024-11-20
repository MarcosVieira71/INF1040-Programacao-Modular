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
    if nomePlaylist in dicionarioPlaylists:
        musica_existe = musica.verificaMusica(nomeAutor, nomeMusica)
        if musica_existe["codigo_retorno"] == 1:
            dicionarioPlaylists[nomePlaylist].append((nomeAutor,nomeMusica))
            resultado = {
            'codigo_retorno': 1,
            'mensagem': "Música adicionada com sucesso"
            }
        else:
            resultado = {
            'codigo_retorno': 0,
            'mensagem': "Música não existe no dicionário"
            }
    else:
        resultado = {
        'codigo_retorno': -1,
        'mensagem': "Playlist inexistente"
        }
    return resultado

def excluirMusicaDaPlaylist(nomePlaylist:str, nomeAutor:str, nomeMusica:str, dicionarioPlaylists = dicionarioPlaylists):
    if nomePlaylist in dicionarioPlaylists:
        if (nomeAutor,nomeMusica) in dicionarioPlaylists[nomePlaylist]:
            dicionarioPlaylists[nomePlaylist].remove((nomeAutor,nomeMusica))
            resultado = {
            'codigo_retorno': 1, 
            'mensagem': 'Música removida da playlist'
            }
        else:
            resultado = {
            'codigo_retorno': 0, 
            'mensagem': 'Música inexistente'
            }
    else:
        resultado = {
        'codigo_retorno': -1, 
        'mensagem': 'Playlist inexistente'
        } 
    return resultado

def verificarMusicaNaPlaylist(nomePlaylist:str, nomeAutor:str, nomeMusica:str, dicionarioPlaylists = dicionarioPlaylists):
    if nomePlaylist in dicionarioPlaylists:
        if (nomeAutor,nomeMusica) in dicionarioPlaylists[nomePlaylist]:
            resultado = {
            'codigo_retorno': 1, 
            'mensagem': 'Música existe na playlist'
            }
        else:
            resultado = {
            'codigo_retorno': 0, 
            'mensagem': 'Música não existe na playlist'
            }
    else:
        resultado = {
        'codigo_retorno': -1, 
        'mensagem': 'Playlist inexistente'
        } 
    return resultado

def excluirPlaylist(nomePlaylist:str, dicionarioPlaylists = dicionarioPlaylists):
    if nomePlaylist in dicionarioPlaylists:
        del dicionarioPlaylists[nomePlaylist]
        resultado = {
        'codigo_retorno': 1, 
        'mensagem': 'Playlist excluída com sucesso'
        }
    else:
        resultado = {
        'codigo_retorno': 0, 
        'mensagem': 'Playlist inexistente'
        }
    return resultado

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