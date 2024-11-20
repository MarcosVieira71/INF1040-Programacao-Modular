import modulos.playlist as playlist
import modulos.avaliacoes as avaliacoes
from modulos.auxiliarJson import *

from mutagen import File
from pathlib import Path
import json
import os 

__all__ = ["verificaArquivo","extraiMetadadosMusicas", "adicionarMusica", "verificaMusica", "encontrarMusica", 
           "excluirMusica", "escreveJsonMusicas", "leJsonMusicas", "obtemMusicas"]

dicionarioMusicas = {}

def verificaArquivo(caminhoDoArquivo: str):
    if os.path.isfile(caminhoDoArquivo):
        if os.path.splitext(caminhoDoArquivo)[1].lower() == ".mp3":
            return {"codigo_retorno": 1, "mensagem": "Arquivo válido"}
    return {"codigo_retorno": 0, "mensagem": "Arquivo inválido ou inexistente"}

def extraiMetadadosMusicas(caminhoDoArquivo:str):
    resultado = {
        "codigo_retorno": 0,
        "mensagem": "Arquivo inválido ou inexistente",
        "metadados": {}
    }
    if verificaArquivo(caminhoDoArquivo)["codigo_retorno"]:
        try:
            arquivo_audio = File(caminhoDoArquivo)
            duracao = round(arquivo_audio.info.length, 2) if hasattr(arquivo_audio.info, 'length') else None
            autor = arquivo_audio.tags.get("artist", "Desconhecido") if arquivo_audio.tags else "Desconhecido"
            nome = arquivo_audio.tags.get("title", Path(caminhoDoArquivo).stem) if arquivo_audio.tags else Path(caminhoDoArquivo).stem

            resultado = {
                "codigo_retorno": 1,
                "mensagem": "Metadados extraídos com sucesso",
                "metadados": {
                    "duracao": duracao,
                    "autor": autor,
                    "nome": nome,
                    "caminho": caminhoDoArquivo
                }
            }
        except Exception as e:
            resultado["codigo_retorno"] = -1
            resultado["mensagem"] = f"Erro ao extrair metadados completamente: {str(e)}"

    return resultado

def adicionarMusica(caminhoArquivo:str, dicionarioMusicas=dicionarioMusicas):
    resultado = {        
        "codigo_retorno": 0,
        "mensagem": "Erro ao adicionar a música: arquivo inválido ou inexistente",
        "metadados_extraidos": {}
    }

    retornoExtracaoMetadados = extraiMetadadosMusicas(caminhoArquivo)
    if(retornoExtracaoMetadados["codigo_retorno"]):
        metadados = retornoExtracaoMetadados["metadados"]
        dicionarioMusicas[(metadados["autor"], metadados["nome"])] = metadados
        resultado["codigo_retorno"] = 1
        resultado["mensagem"] = "Música adicionada com sucesso"
        resultado["metadados_extraidos"] = metadados
    return resultado
 
def verificaMusica(nomeAutor: str, nomeMusica: str, dicionarioMusicas=dicionarioMusicas):
    resultado = {
        "codigo_retorno": 0,
        "mensagem": "Música não existe no dicionário"
    }

    chave = (nomeAutor, nomeMusica)
    if chave in dicionarioMusicas:
        resultado["codigo_retorno"] = 1
        resultado["mensagem"] = "Música existe no dicionário"
    return resultado  

def encontrarMusica(nomeAutor: str, nomeMusica: str, dicionarioMusicas=dicionarioMusicas):
    resultado = {
        "codigo_retorno": 0,
        "mensagem": "Música não encontrada",
        "musica": None
    }

    chave = (nomeAutor, nomeMusica)

    if chave in dicionarioMusicas:
        resultado["codigo_retorno"] = 1
        resultado["mensagem"] = "Música encontrada"
        resultado["musica"] = dicionarioMusicas[chave]  
    return resultado    


def excluirMusica(nomeAutor: str, nomeDaMusica: str, dicionarioMusicas=dicionarioMusicas):
    resultado = {
        "codigo_retorno": 0,
        "mensagem": "Música não existe."
    }

    verificaResultado = verificaMusica(nomeAutor, nomeDaMusica)
    if verificaResultado["codigo_retorno"] == 0:
        return resultado  # Música não existe

    # Verifica se a música tem avaliação
    if avaliacoes.verificaAvaliacao(nomeAutor, nomeDaMusica)["codigo_retorno"]:
        resultado["codigo_retorno"] = -1
        resultado["mensagem"] = "A música não pode ser excluída pois tem avaliação."
        return resultado

    # Verifica se a música está em uma playlist
    if playlist.verificaMusicaNaPlaylist(nomeAutor, nomeDaMusica):
        resultado["codigo_retorno"] = -2
        resultado["mensagem"] = "A música não pode ser excluída pois está em uma playlist."
        return resultado

    # Remove a música do dicionário
    chave = (nomeAutor, nomeDaMusica)
    del dicionarioMusicas[chave]
    resultado["codigo_retorno"] = 1
    resultado["mensagem"] = "Música excluída com sucesso."
    
    return resultado


def escreveJsonMusicas(ambiente, dicionarioMusicas=dicionarioMusicas):
    if ambiente == "test":
        caminhoPasta = "src/test/jsons"
    else:
        caminhoPasta = "src/jsons"

    resultado = {
        "codigo_retorno": 0,
        "mensagem": "Erro ao escrever o arquivo, dicionário inexistente."
    }
    
    if not dicionarioMusicas:
        return resultado

    try:
        os.makedirs(caminhoPasta, exist_ok=True)

        dicionarioMusicas = converteChavesParaString(dicionarioMusicas)
        caminhoArquivo = os.path.join(caminhoPasta, "musicas.json")

        with open(caminhoArquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dicionarioMusicas, arquivo, ensure_ascii=False, indent=4)
            resultado["codigo_retorno"] = 1
            resultado["mensagem"] = "Arquivo escrito com sucesso."
    except Exception as e:
        pass
    
    return resultado

def leJsonMusicas(ambiente, dicionarioMusicas=dicionarioMusicas):
    if ambiente == "test":
        caminhoPasta = "src/test/jsons"
    else:
        caminhoPasta = "src/jsons"
    
    resultado = {
        "codigo_retorno": 0,
        "mensagem": "Erro ao ler o arquivo"
    }
    caminhoArquivo = os.path.join(caminhoPasta, "musicas.json")
    try:
        with open(caminhoArquivo, "r", encoding="utf-8") as arquivo:
            leituraJson = json.load(arquivo)
            dicionarioMusicas.clear()
            dicionarioMusicas.update(reverterChavesParaTipoOriginal(leituraJson))
            resultado["codigo_retorno"] = 1
            resultado["mensagem"] = "Músicas obtidas com sucesso do arquivo"
    except Exception as e:
        pass

    return resultado

def obtemMusicas(dicionarioMusicas=dicionarioMusicas):
    if dicionarioMusicas:
        return {"codigo_retorno": 1, "musicas": dicionarioMusicas.values(), "mensagem":"Músicas obtidas com sucesso"}
    return {"codigo_retorno": 0, "musicas": None, "mensagem":"Não foi possível obter as músicas"}

