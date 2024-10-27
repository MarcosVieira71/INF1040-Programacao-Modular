import playlist
import avaliacoes

from mutagen import File
from pathlib import Path
import json
import os 

def leJsonMusicas(dicionarioMusicas: dict):
    resultado = {
        "codigo_retorno": 0,
        "dicionarioMusicas": {}
    }

    try:
        with open("musicas.json", "r", encoding="utf-8") as arquivo:
            dicionarioMusicas.update(json.load(arquivo))
            resultado["codigo_retorno"] = 1
            resultado["dicionarioMusicas"] = dicionarioMusicas
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

    return resultado

def escreveJsonMusicas(dicionarioMusicas:dict):
    resultado = {
        "codigoRetorno": 0,
        "mensagem": "Erro ao escrever o arquivo."
    }
    
    try:
        with open("musicas.json", "w", encoding="utf-8") as arquivo:
            json.dump(dicionarioMusicas, arquivo, ensure_ascii=False, indent=4)
            resultado["codigoRetorno"] = 1
            resultado["mensagem"] = "Arquivo escrito com sucesso."
    except Exception as e:
        print(f"Erro ao escrever o arquivo: {e}")

    return resultado
def geraDicionarioDeMusicas():
    global dicionarioMusicas
    dicionarioMusicas = {}
    retornoLeituraJson = leJsonMusicas(dicionarioMusicas)
    codigoDeRetorno = retornoLeituraJson["codigo_retorno"]
    mensagem = "Erro ao gerar dicionário usando o json" if not codigoDeRetorno else "Dicionário gerado com sucesso"
    return {"codigo_retorno": codigoDeRetorno, "mensagem":mensagem, "dicionario_musicas": dicionarioMusicas}

def verificaArquivo(caminhoDoArquivo: str):
    if os.path.isfile(caminhoDoArquivo):
        if os.path.splitext(caminhoDoArquivo)[1].lower() == ".mp3":
            return {"codigo_retorno": 1, "mensagem": "Arquivo válido"}
    return {"codigo_retorno": 0, "mensagem": "Arquivo inválido"}

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

def adicionarMusica(caminhoArquivo:str, dicionarioMusicas:dict):
    resultado = {        
        "codigo_retorno": 0,
        "mensagem": "Erro ao adicionar a música: arquivo inválido ou inexistente"
    }

    retornoExtracaoMetadados = extraiMetadadosMusicas(caminhoArquivo)
    if(retornoExtracaoMetadados["codigo_retorno"]):
        musica = retornoExtracaoMetadados["metadados"]
        dicionarioMusicas[(musica["autor"], musica["nome"])] = musica
        resultado["codigo_retorno"] = 1
        resultado["mensagem"] = "Música adicionada com sucesso"
    return resultado
 
def verificaMusica(nomeAutor: str, nomeMusica: str, dicionarioMusicas: dict):
    resultado = {
        "codigo_retorno": 0,
        "mensagem": "Música existe no dicionário"
    }

    chave = (nomeAutor, nomeMusica)
    if chave in dicionarioMusicas:
        resultado["codigo_retorno"] = 1
        resultado["mensagem"] = "Música não existe no dicionário"
    return resultado  

def encontrarMusica(nomeAutor: str, nomeMusica: str, dicionarioMusicas: dict):
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


def excluirMusica(nomeAutor: str, nomeDaMusica: str, dicionarioMusicas:dict):
    resultado = {
        "codigoRetorno": 0,
        "mensagem": "Música não existe."
    }

    verificaResultado = verificaMusica(nomeAutor, nomeDaMusica)
    if verificaResultado["codigoRetorno"] == 0:
        return resultado  # Música não existe

    # Verifica se a música tem avaliação
    if avaliacoes.verificaAvaliacao(nomeAutor, nomeDaMusica):
        resultado["codigoRetorno"] = -1
        resultado["mensagem"] = "A música não pode ser excluída pois tem avaliações."
        return resultado

    # Verifica se a música está em uma playlist
    if playlist.verificaMusicaNaPlaylist(nomeAutor, nomeDaMusica):
        resultado["codigoRetorno"] = -2
        resultado["mensagem"] = "A música não pode ser excluída pois está em uma playlist."
        return resultado

    # Remove a música do dicionário
    chave = (nomeAutor, nomeDaMusica)
    del dicionarioMusicas[chave]
    resultado["codigoRetorno"] = 1
    resultado["mensagem"] = "Música excluída com sucesso."
    
    return resultado
