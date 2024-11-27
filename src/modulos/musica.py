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

# Descrição:
# Esta função verifica se o arquivo especificado pelo caminho é válido. O arquivo é considerado válido se existir e 
# tiver a extensão `.mp3`. Retorna um dicionário com um `codigo_retorno` e uma mensagem correspondente ao status 
# da validação.

# Parâmetros:
# - `caminhoDoArquivo` (str): O caminho completo do arquivo que será validado.

# Acoplamento:
# A função espera receber uma string no parâmetro `caminhoDoArquivo`, representando o caminho completo de um arquivo.
# O `codigo_retorno` pode ser:
# - 1: Sucesso (arquivo válido com extensão `.mp3`).
# - 0: Erro (arquivo inválido ou inexistente).

# Condições de Acoplamento:
# A função depende de `os.path.isfile` para verificar a existência do arquivo e `os.path.splitext` para validar sua extensão.

# Hipóteses:
# - Assume-se que o caminho fornecido é acessível pelo sistema operacional.
# - O arquivo deve estar localizado no caminho especificado.

# Interface com o Usuário:
# - Retorna um dicionário com:
#   - `codigo_retorno`: Inteiro indicando o status da validação.
#   - `mensagem`: String descrevendo o resultado da validação.

def verificaArquivo(caminhoDoArquivo: str):
    if os.path.isfile(caminhoDoArquivo):
        if os.path.splitext(caminhoDoArquivo)[1].lower() == ".mp3":
            return {"codigo_retorno": 1, "mensagem": "Arquivo válido"}
    return {"codigo_retorno": 0, "mensagem": "Arquivo inválido ou inexistente"}

# Descrição:
# Esta função extrai os metadados de uma música no formato MP3, incluindo informações como duração, autor, nome e o caminho 
# do arquivo. Caso o arquivo não seja válido ou a extração falhe, retorna um erro. 

# Parâmetros:
# - `caminhoDoArquivo` (str): O caminho completo do arquivo MP3 que terá os metadados extraídos.

# Acoplamento:
# A função espera receber uma string no parâmetro `caminhoDoArquivo`, representando o caminho completo de um arquivo MP3.
# O `codigo_retorno` pode ser:
# - 1: Sucesso (metadados extraídos com sucesso).
# - 0: Erro (arquivo inválido ou inexistente).
# - -1: Erro (falha ao extrair os metadados).

# Condições de Acoplamento:
# - A função depende de `verificaArquivo` para validar o arquivo antes da extração.
# - Depende da biblioteca `mutagen` para extrair os metadados.

# Hipóteses:
# - O arquivo fornecido é válido e acessível.
# - Os metadados esperados (autor e nome) estão presentes ou valores padrão podem ser atribuídos.

# Interface com o Usuário:
# - Retorna um dicionário com:
#   - `codigo_retorno`: Inteiro indicando o status da operação.
#   - `mensagem`: String descrevendo o resultado da extração.
#   - `metadados`: Dicionário contendo os metadados extraídos, incluindo:
#     - `duracao` (float): Duração da música em segundos.
#     - `autor` (str): Nome do autor da música.
#     - `nome` (str): Nome da música.
#     - `caminho` (str): Caminho completo do arquivo.

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

# Descrição:
# Esta função adiciona uma música ao dicionário `dicionarioMusicas` com base nos metadados extraídos do arquivo. 
# Antes de adicionar, verifica se a música já existe no dicionário. Retorna um dicionário com um `codigo_retorno` 
# e uma mensagem correspondente ao status da operação.

# Parâmetros:
# - `caminhoArquivo` (str): O caminho completo do arquivo MP3 que será adicionado.
# - `dicionarioMusicas` (dict, opcional): O dicionário onde as músicas serão armazenadas. 
#   - Chave: Tupla (`nomeAutor`, `nomeMusica`).
#   - Valor: Dicionário com os metadados da música.

# Acoplamento:
# O parâmetro `dicionarioMusicas` deve ser um dicionário conforme especificado.
# O `codigo_retorno` pode ser:
# - 1: Sucesso (música adicionada).
# - 0: Erro (arquivo inválido ou inexistente).
# - -1: Erro (música já existe no dicionário).

# Condições de Acoplamento:
# - Depende de `extraiMetadadosMusicas` para obter os metadados do arquivo.
# - Depende de `verificaMusica` para garantir que a música não está duplicada.

# Hipóteses:
# - O dicionário segue a estrutura esperada.
# - O arquivo fornecido é válido e contém metadados compatíveis.

# Interface com o Usuário:
# - Retorna um dicionário com:
#   - `codigo_retorno`: Inteiro indicando o status da operação.
#   - `mensagem`: String descrevendo o resultado da operação.
#   - `metadados_extraidos`: Metadados da música adicionada, em caso de sucesso.

def adicionarMusica(caminhoArquivo:str, dicionarioMusicas=dicionarioMusicas):
    resultado = {        
        "codigo_retorno": 0,
        "mensagem": "Erro ao adicionar a música: arquivo inválido ou inexistente",
        "metadados_extraidos": {}
    }

    retornoExtracaoMetadados = extraiMetadadosMusicas(caminhoArquivo)
    if(retornoExtracaoMetadados["codigo_retorno"]):
        metadados = retornoExtracaoMetadados["metadados"]
        resultadoVerificaMusica = verificaMusica(metadados["autor"], metadados["nome"])
        if resultadoVerificaMusica["codigo_retorno"]:
            resultado["codigo_retorno"] = -1
            resultado["mensagem"] = "Música já existente."
        else:
            dicionarioMusicas[(metadados["autor"], metadados["nome"])] = metadados
            resultado["codigo_retorno"] = 1
            resultado["mensagem"] = "Música adicionada com sucesso"
            resultado["metadados_extraidos"] = metadados
    return resultado

# Descrição:
# Esta função verifica se uma música existe no dicionário `dicionarioMusicas` com base no autor e nome fornecidos.
# Retorna um dicionário com um `codigo_retorno` e uma mensagem correspondente ao status da verificação.

# Parâmetros:
# - `nomeAutor` (str): Nome do autor da música a ser verificada.
# - `nomeMusica` (str): Nome da música a ser verificada.
# - `dicionarioMusicas` (dict, opcional): O dicionário de músicas onde será feita a verificação.
#   - Chave: Tupla (`nomeAutor`, `nomeMusica`).
#   - Valor: Dicionário com os metadados da música.

# Acoplamento:
# O parâmetro `dicionarioMusicas` deve ser um dicionário conforme especificado.
# O `codigo_retorno` pode ser:
# - 1: Sucesso (música encontrada).
# - 0: Erro (música não encontrada).

# Condições de Acoplamento:
# - O dicionário segue a estrutura esperada.

# Hipóteses:
# - Assume-se que o dicionário de músicas está populado e segue o formato esperado.

# Interface com o Usuário:
# - Retorna um dicionário com:
#   - `codigo_retorno`: Inteiro indicando o status da verificação.
#   - `mensagem`: String descrevendo o resultado da verificação.

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

# Descrição:
# Esta função busca uma música no dicionário `dicionarioMusicas` com base no autor e no nome fornecidos. 
# Se a música for encontrada, retorna seus metadados. Caso contrário, retorna uma mensagem de erro.

# Parâmetros:
# - `nomeAutor` (str): Nome do autor da música a ser buscada.
# - `nomeMusica` (str): Nome da música a ser buscada.
# - `dicionarioMusicas` (dict, opcional): O dicionário de músicas onde será feita a busca.
#   - Chave: Tupla (`nomeAutor`, `nomeMusica`).
#   - Valor: Dicionário com os metadados da música.

# Acoplamento:
# O parâmetro `dicionarioMusicas` deve ser um dicionário conforme especificado.
# O `codigo_retorno` pode ser:
# - 1: Sucesso (música encontrada).
# - 0: Erro (música não encontrada).

# Condições de Acoplamento:
# - O dicionário segue a estrutura esperada.

# Hipóteses:
# - Assume-se que o dicionário de músicas está populado e segue o formato esperado.

# Interface com o Usuário:
# - Retorna um dicionário com:
#   - `codigo_retorno`: Inteiro indicando o status da busca.
#   - `mensagem`: String descrevendo o resultado da busca.
#   - `musica`: Os metadados da música encontrada ou `None` em caso de erro.

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

# Descrição:
# Esta função remove uma música do dicionário `dicionarioMusicas` com base no autor e no nome fornecidos. 
# Antes de excluir, verifica se a música está associada a avaliações ou a playlists. Caso esteja vinculada, 
# a exclusão é bloqueada e uma mensagem de erro específica é retornada.

# Parâmetros:
# - `nomeAutor` (str): Nome do autor da música a ser excluída.
# - `nomeDaMusica` (str): Nome da música a ser excluída.
# - `dicionarioMusicas` (dict, opcional): O dicionário de músicas onde será feita a exclusão.
#   - Chave: Tupla (`nomeAutor`, `nomeMusica`).
#   - Valor: Dicionário com os metadados da música.

# Acoplamento:
# O parâmetro `dicionarioMusicas` deve ser um dicionário conforme especificado.
# O `codigo_retorno` pode ser:
# - 1: Sucesso (música excluída com sucesso).
# - 0: Erro (música inexistente).
# - -1: Erro (música vinculada a avaliações).
# - -2: Erro (música vinculada a playlists).

# Condições de Acoplamento:
# - Depende das funções `verificaMusica`, `verificaAvaliacao` e `verificarMusicaNaPlaylist` para validações.
# - Depende de `obterNomesPlaylists` para listar as playlists existentes.

# Hipóteses:
# - Assume-se que o dicionário de músicas e as funções de validação estão corretamente implementados.

# Interface com o Usuário:
# - Retorna um dicionário com:
#   - `codigo_retorno`: Inteiro indicando o status da exclusão.
#   - `mensagem`: String descrevendo o resultado da operação.

def excluirMusica(nomeAutor: str, nomeDaMusica: str, dicionarioMusicas=dicionarioMusicas):
    from modulos.avaliacoes import verificaAvaliacao
    from modulos.playlist import obterNomesPlaylists, verificarMusicaNaPlaylist
    resultado = {
        "codigo_retorno": 0,
        "mensagem": "Música não existe."
    }

    verificaResultado = verificaMusica(nomeAutor, nomeDaMusica)
    if verificaResultado["codigo_retorno"] == 0:
        return resultado  # Música não existe

    # Verifica se a música tem avaliação
    if verificaAvaliacao(nomeAutor, nomeDaMusica)["codigo_retorno"]:
        resultado["codigo_retorno"] = -1
        resultado["mensagem"] = "A música não pode ser excluída pois tem avaliação."
        return resultado

    # Verifica se a música está em uma playlist
    resultadoNomesPlaylists = obterNomesPlaylists()
    if resultadoNomesPlaylists["codigo_retorno"]:
        for nome in resultadoNomesPlaylists["nomes"]:
            if verificarMusicaNaPlaylist(nome, nomeAutor, nomeDaMusica)["codigo_retorno"]:
                resultado["codigo_retorno"] = -2
                resultado["mensagem"] = "A música não pode ser excluída pois está em uma playlist."
                return resultado

    # Remove a música do dicionário
    chave = (nomeAutor, nomeDaMusica)
    del dicionarioMusicas[chave]
    resultado["codigo_retorno"] = 1
    resultado["mensagem"] = "Música excluída com sucesso."
    
    return resultado

# Descrição:
# Esta função grava o conteúdo do dicionário `dicionarioMusicas` em um arquivo JSON. O local de armazenamento 
# varia conforme o ambiente (`test` ou produção). As chaves do dicionário são convertidas para strings para 
# garantir compatibilidade com o formato JSON.

# Parâmetros:
# - `ambiente` (str): Define o ambiente de execução (`test` ou produção).
# - `dicionarioMusicas` (dict, opcional): O dicionário de músicas a ser gravado.
#   - Chave: Tupla (`nomeAutor`, `nomeMusica`).
#   - Valor: Dicionário com os metadados da música.

# Acoplamento:
# O parâmetro `dicionarioMusicas` deve ser um dicionário conforme especificado.
# O `codigo_retorno` pode ser:
# - 1: Sucesso (arquivo escrito com sucesso).
# - 0: Erro (dicionário inexistente ou falha ao escrever o arquivo).

# Condições de Acoplamento:
# - Depende de `converteChavesParaString` para preparar o dicionário para o formato JSON.
# - Depende de bibliotecas padrão (`os`, `json`) para manipulação de arquivos.

# Hipóteses:
# - Assume-se que o ambiente especificado é válido (`test` ou produção).
# - O dicionário segue a estrutura esperada.

# Interface com o Usuário:
# - Retorna um dicionário com:
#   - `codigo_retorno`: Inteiro indicando o status da operação.
#   - `mensagem`: String descrevendo o resultado da gravação.

def escreveJsonMusicas(ambiente, dicionarioMusicas=dicionarioMusicas):
    if ambiente == "test":
        caminhoPasta = "src/test/jsons"
    else:
        caminhoPasta = "src/jsons"

    resultado = {
        "codigo_retorno": 0,
        "mensagem": "Erro ao escrever o arquivo, dicionário inexistente."
    }
    

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

# Descrição:
# Esta função lê o conteúdo de um arquivo JSON e o carrega no dicionário `dicionarioMusicas`. O local de leitura 
# varia conforme o ambiente (`test` ou produção). As chaves no arquivo JSON são convertidas de volta para tuplas 
# para restaurar o formato original.

# Parâmetros:
# - `ambiente` (str): Define o ambiente de execução (`test` ou produção).
# - `dicionarioMusicas` (dict, opcional): O dicionário onde os dados lidos serão carregados.
#   - Chave: Tupla (`nomeAutor`, `nomeMusica`).
#   - Valor: Dicionário com os metadados da música.

# Acoplamento:
# O parâmetro `dicionarioMusicas` deve ser um dicionário conforme especificado.
# O `codigo_retorno` pode ser:
# - 1: Sucesso (dados lidos com sucesso).
# - 0: Erro (arquivo inexistente ou falha ao ler os dados).

# Condições de Acoplamento:
# - Depende de `reverterChavesParaTipoOriginal` para restaurar as chaves ao formato esperado.
# - Depende de bibliotecas padrão (`os`, `json`) para manipulação de arquivos.

# Hipóteses:
# - Assume-se que o arquivo JSON segue o formato esperado.
# - O dicionário será sobrescrito com os dados lidos.

# Interface com o Usuário:
# - Retorna um dicionário com:
#   - `codigo_retorno`: Inteiro indicando o status da leitura.
#   - `mensagem`: String descrevendo o resultado da leitura.

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

# Descrição:
# Esta função retorna todas as músicas presentes no dicionário `dicionarioMusicas`. Caso o dicionário esteja vazio, 
# retorna uma mensagem de erro.

# Parâmetros:
# - `dicionarioMusicas` (dict, opcional): O dicionário de músicas a ser consultado.
#   - Chave: Tupla (`nomeAutor`, `nomeMusica`).
#   - Valor: Dicionário com os metadados da música.

# Acoplamento:
# O parâmetro `dicionarioMusicas` deve ser um dicionário conforme especificado.
# O `codigo_retorno` pode ser:
# - 1: Sucesso (músicas obtidas com sucesso).
# - 0: Erro (não foi possível obter as músicas, dicionário vazio).

# Condições de Acoplamento:
# - O dicionário segue a estrutura esperada.

# Hipóteses:
# - Assume-se que o dicionário de músicas está corretamente estruturado.

# Interface com o Usuário:
# - Retorna um dicionário com:
#   - `codigo_retorno`: Inteiro indicando o status da consulta.
#   - `mensagem`: String descrevendo o resultado da consulta.
#   - `musicas`: As músicas presentes no dicionário ou `None` em caso de erro.

def obtemMusicas(dicionarioMusicas=dicionarioMusicas):
    if dicionarioMusicas:
        return {"codigo_retorno": 1, "musicas": dicionarioMusicas.values(), "mensagem":"Músicas obtidas com sucesso"}
    return {"codigo_retorno": 0, "musicas": None, "mensagem":"Não foi possível obter as músicas"}

