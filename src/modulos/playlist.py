
from modulos.auxiliarJson import *
import os
import json

dicionarioPlaylists = {}

__all__ = ["criarPlaylist","adicionarMusicaNaPlaylist", "excluirMusicaDaPlaylist", "verificarMusicaNaPlaylist", "excluirPlaylist", 
           "mudaNomePlaylist", "escreveJsonPlaylists", "leJsonPlaylists","obterNomesPlaylists" ,"obtemMusicasDePlaylist"]

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
    from modulos.musica import verificaMusica
    if nomePlaylist in dicionarioPlaylists:
        musica_existe = verificaMusica(nomeAutor, nomeMusica)
        if musica_existe["codigo_retorno"] == 1:
            dicionarioPlaylists[nomePlaylist].append([nomeAutor,nomeMusica])
            resultado = {
            'codigo_retorno': 1,
            'mensagem': "Música adicionada com sucesso"
            }
        else:
            resultado = {
            'codigo_retorno': 0,
            'mensagem': "Música inexistente"
            }
    else:
        resultado = {
        'codigo_retorno': -1,
        'mensagem': "Playlist inexistente"
        }
    return resultado

def excluirMusicaDaPlaylist(nomePlaylist:str, nomeAutor:str, nomeMusica:str, dicionarioPlaylists = dicionarioPlaylists):
    if nomePlaylist in dicionarioPlaylists:
        if [nomeAutor,nomeMusica] in dicionarioPlaylists[nomePlaylist]:
            dicionarioPlaylists[nomePlaylist].remove([nomeAutor,nomeMusica])
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

def verificarMusicaNaPlaylist(nomePlaylist:str, nomeAutor:str, nomeMusica:str, dicionarioPlaylists=dicionarioPlaylists):
    if nomePlaylist in dicionarioPlaylists:
        if [nomeAutor,nomeMusica] in dicionarioPlaylists[nomePlaylist]:
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

def escreveJsonPlaylists(ambiente, dicionarioPlaylists = dicionarioPlaylists):
    if ambiente == "test":
        caminhoPasta = "src/test/jsons"
    else:
        caminhoPasta = "src/jsons"

    resultado = {
        "codigo_retorno": 0,
        "mensagem": "Erro ao escrever o arquivo, dicionário inexistente."
    }

    if not dicionarioPlaylists:
        return resultado
    
    try:
        os.makedirs(caminhoPasta, exist_ok=True)
        dicionarioPlaylists = converteChavesParaString(dicionarioPlaylists)
        caminhoArquivo = os.path.join(caminhoPasta, "playlists.json")
        
        with open(caminhoArquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dicionarioPlaylists, arquivo, ensure_ascii=False, indent=4)
            resultado["codigo_retorno"] = 1
            resultado["mensagem"] = "Arquivo escrito com sucesso."
    except Exception as e:
        pass
    return resultado

def leJsonPlaylists(ambiente, dicionarioPlaylists = dicionarioPlaylists):
    if ambiente == "test":
        caminhoPasta = "src/test/jsons"
    else:
        caminhoPasta = "src/jsons"

    resultado = {
        "codigo_retorno": 0,
        "mensagem": "Erro ao ler o arquivo"
    }

    caminhoArquivo = os.path.join(caminhoPasta, "playlists.json")

    try:
        with open(caminhoArquivo, "r", encoding="utf-8") as arquivo:
            leituraJson = json.load(arquivo)
            dicionarioPlaylists.clear()
            dicionarioPlaylists.update(reverterChavesParaTipoOriginal(leituraJson))
            resultado["codigo_retorno"] = 1
            resultado["mensagem"] = "Músicas obtidas com sucesso do arquivo."
    except Exception as e:
        pass
    return resultado

def obterNomesPlaylists(dicionarioPlaylists=dicionarioPlaylists):
    if dicionarioPlaylists:
        return {"codigo_retorno": 1, "nomes": dicionarioPlaylists.keys(), "mensagem": "Nomes das playlists obtidos com sucesso."}
    return {"codigo_retorno": 0, "nomes": None, "mensagem": "Falha ao obter nomes das playlists"}

def obtemMusicasDePlaylist(nomePlaylist, dicionarioPlaylists=dicionarioPlaylists):
    if nomePlaylist in dicionarioPlaylists.keys():
        return {"codigo_retorno":1, "musicas": dicionarioPlaylists[nomePlaylist], "mensagem": "Músicas obtidas com sucesso"}
    return {"codigo_retorno":0, "musicas":None, "mensagem":"Não foi possível obter as músicas da playlist"}