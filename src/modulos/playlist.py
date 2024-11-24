
from modulos.auxiliarJson import *
import os
import json

dicionarioPlaylists = {}

__all__ = ["criarPlaylist","adicionarMusicaNaPlaylist", "excluirMusicaDaPlaylist", "verificarMusicaNaPlaylist", "excluirPlaylist", 
           "mudaNomePlaylist", "escreveJsonPlaylists", "leJsonPlaylists","obterNomesPlaylists" ,"obtemMusicasDePlaylist"]

# Descrição:
# Essa função recebe como parâmetros o nome a ser utilizado para uma playlist ('nomePlaylist') e um dicionário de playlists ('dicionarioPlaylists'). A função verifica se existe
# uma entrada no 'dicionarioPlaylists' correspondente ao valor de nomePlaylist. Caso exista, retorna um dicionário com 'codigo_retorno' igual a 0
# e uma mensagem indicando erro ao criar a playlist. Caso contrário, retorna um dicionário com 'codigo_retorno' igual a 1, uma mensagem indicando
# sucesso ao criar a playlist, além de adicionar uma chave nova (nomePlaylist) no dicionário de playlists, sendo seu valor uma lista vazia.

# Acoplamento:
# A função assume que irá receber uma string no parâmetro nomePlaylist. O parâmetro dicionarioPlaylists espera receber um dicionário com
# os nomes das playlists como suas chaves.
# Os retornos são sempre em forma de dicionário com campos de "codigo_retorno" e "mensagem", sendo o código de retorno um valor inteiro
# 0, 1 ou -1 (1 para representar que tudo funcionou de acordo e 0 e/ou -1 para indicar que houve um erro na execução da função). A mensagem só informa o que aconteceu durante
# a execução da função.
#
# Condições de Acoplamento:
# A função depende de 'dicionarioPlaylists' como um dicionário em que as chaves são strings que representam os nomes das playlists
# e os valores são uma lista de tuplas, da forma (nomeAutor, nomeMusica), que representam o nome do autor e o nome da música dentro daquela playlist.

# Hipóteses:
# - A função assume que 'dicionarioPlaylists' segue a estrutura esperada.

# Interface com o Usuário:
# A função não interage diretamente com o usuário, mas retorna um dicionário com `codigo_retorno` e `mensagem`, que podem 
# ser utilizados por uma interface para exibir feedback ao usuário.

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

# Descrição:
# Esta função recebe o nome de uma playlist (`nomePlaylist`), o nome do autor da música (`nomeAutor`), o nome da música 
# (`nomeMusica`) e o dicionário de playlists ('dicionarioPlaylists'). A função verifica se a playlist existe no dicionário 
# e se a música especificada existe no sistema usando a função `verificaMusica` do módulo `musica`. Caso ambas as verificações 
# sejam positivas, a música é adicionada à playlist. Caso contrário, a função retorna uma mensagem de erro específica. 
# Retorna um dicionário com um `codigo_retorno` e uma mensagem correspondente ao sucesso ou falha da operação.

# Acoplamento:
# A função espera receber strings nos parâmetros nomePlaylist, nomeAutor e nomeMusica. O parâmetro dicionarioPlaylists espera receber um dicionário com
# os nomes das playlists como suas chaves. A função utiliza a função `verificaMusica` do módulo `musica` para validar se a música existe no sistema.
# O `codigo_retorno` pode ser:
# - 1: Sucesso (música adicionada à playlist).
# - 0: Erro (música inexistente no sistema).
# - -1: Erro (playlist inexistente).
#
# Condições de Acoplamento:
# A função depende da estrutura do `dicionarioPlaylists`, que deve ser um dicionário onde as chaves são strings (nomes das playlists) 
# e os valores são listas de músicas, onde cada música é representada como tupla de dois elementos: (nomeAutor, nomeMusica).

# Hipóteses:
# - Assume-se que o `dicionarioPlaylists` já contém todas as playlists necessárias.
# - A função `verificaMusica` retorna um dicionário com um `codigo_retorno` indicando se a música existe.
# - Os nomes de autor e de música recebidos devem ser do tipo str, para não haver conflito de tipagem.

# Interface com o Usuário:
# - Retorna um dicionário com `codigo_retorno` e `mensagem` para informar o status da operação.

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

# Descrição:
# Esta função remove uma música de uma playlist específica. Recebe o nome da playlist (`nomePlaylist`), o nome do autor 
# (`nomeAutor`), o nome da música (`nomeMusica`) e um dicionário de playlists (`dicionarioPlaylists`). A função verifica se a 
# playlist existe e se a música especificada está presente na lista de músicas da playlist. Caso ambas as verificações 
# sejam positivas, a música é removida da playlist. Caso contrário, retorna uma mensagem de erro específica. Retorna um 
# dicionário com um `codigo_retorno` e uma mensagem correspondente ao sucesso ou falha da operação.

# Acoplamento:
# A função espera receber strings nos parâmetros `nomePlaylist`, `nomeAutor` e `nomeMusica`. O parâmetro `dicionarioPlaylists` 
# espera receber um dicionário com os nomes das playlists como suas chaves. 
# O `codigo_retorno` pode ser:
# - 1: Sucesso (música removida da playlist).
# - 0: Erro (música inexistente na playlist).
# - -1: Erro (playlist inexistente).
#
# Condições de Acoplamento:
# A função depende da estrutura do `dicionarioPlaylists`, que deve ser um dicionário onde as chaves são strings (nomes das playlists) 
# e os valores são listas de músicas, onde cada música é representada como tupla de dois elementos: (nomeAutor, nomeMusica).

# Hipóteses:
# - Assume-se que o `dicionarioPlaylists` segue a estrutura esperada.
# - Os nomes de autor e de música recebidos devem ser do tipo str, para não haver conflito de tipagem.

# Interface com o Usuário:
# - Retorna um dicionário com `codigo_retorno` e `mensagem` para informar o status da operação.

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

# Descrição:
# Esta função verifica se uma música, identificada pelo autor (`nomeAutor`) e pelo nome da música (`nomeMusica`), está 
# presente em uma playlist específica (`nomePlaylist`). Caso a playlist exista e a música esteja presente, retorna um dicionário 
# com `codigo_retorno` 1 e uma mensagem de confirmação. Caso contrário, retorna mensagens de erro apropriadas.

# Acoplamento:
# A função espera receber strings nos parâmetros `nomePlaylist`, `nomeAutor` e `nomeMusica`. O parâmetro `dicionarioPlaylists` 
# espera receber um dicionário com os nomes das playlists como suas chaves. 
# O `codigo_retorno` pode ser:
# - 1: Sucesso (música encontrada na playlist).
# - 0: Erro (música não encontrada na playlist).
# - -1: Erro (playlist inexistente).
#
# Condições de Acoplamento:
# A função depende da estrutura do `dicionarioPlaylists`, que deve ser um dicionário onde as chaves são strings (nomes das playlists) 
# e os valores são listas de músicas, onde cada música é representada como tupla de dois elementos: (nomeAutor, nomeMusica).

# Hipóteses:
# - Assume-se que o `dicionarioPlaylists` segue a estrutura esperada.
# - Os nomes de autor e de música recebidos devem ser do tipo str, para não haver conflito de tipagem.

# Interface com o Usuário:
# - Retorna um dicionário com `codigo_retorno` e `mensagem` para informar o status da verificação.

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

# Descrição:
# Esta função remove uma playlist do dicionário de playlists. Recebe o nome da playlist (`nomePlaylist`) e o dicionário de playlists 
# (`dicionarioPlaylists`). Caso a playlist exista, ela é excluída e a função retorna um dicionário com `codigo_retorno` 1 e uma 
# mensagem de sucesso. Caso contrário, retorna um dicionário com `codigo_retorno` 0 e uma mensagem indicando que a playlist não existe.

# Acoplamento:
# A função espera receber uma string no parâmetro `nomePlaylist`. O parâmetro `dicionarioPlaylists` espera receber um dicionário 
# com os nomes das playlists como suas chaves.
# O `codigo_retorno` pode ser:
# - 1: Sucesso (playlist excluída).
# - 0: Erro (playlist inexistente).
#
# Condições de Acoplamento:
# A função depende da estrutura do `dicionarioPlaylists`, que deve ser um dicionário onde as chaves são strings representando 
# os nomes das playlists.

# Hipóteses:
# - Assume-se que o `dicionarioPlaylists` segue a estrutura esperada.

# Interface com o Usuário:
# - Retorna um dicionário com `codigo_retorno` e `mensagem` para informar o status da operação.

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

# Descrição:
# Esta função altera o nome de uma playlist existente no dicionário de playlists. Recebe o nome atual da playlist 
# (`nomePlaylist`), o novo nome desejado (`novoNome`) e o dicionário de playlists (`dicionarioPlaylists`). Caso a playlist 
# exista e o novo nome seja diferente do nome atual, a alteração é realizada com sucesso. Caso contrário, a função retorna 
# uma mensagem de erro específica. Retorna um dicionário com um `codigo_retorno` e uma mensagem correspondente ao sucesso ou falha da operação.

# Acoplamento:
# A função espera receber strings nos parâmetros `nomePlaylist` e `novoNome`. O parâmetro `dicionarioPlaylists` espera 
# receber um dicionário com os nomes das playlists como suas chaves. 
# O `codigo_retorno` pode ser:
# - 1: Sucesso (nome da playlist alterado).
# - 0: Erro (nome da playlist não alterado porque é igual ao nome atual).
# - -1: Erro (playlist inexistente).
#
# Condições de Acoplamento:
# A função depende da estrutura do `dicionarioPlaylists`, que deve ser um dicionário onde as chaves são strings representando 
# os nomes das playlists.

# Hipóteses:
# - Assume-se que o `dicionarioPlaylists` segue a estrutura esperada.
# - O novo nome da playlist deve ser do tipo str para evitar conflitos de tipagem.

# Interface com o Usuário:
# - Retorna um dicionário com `codigo_retorno` e `mensagem` para informar o status da operação.

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

# Descrição:
# Esta função salva o dicionário `dicionarioPlaylists` em um arquivo JSON no diretório apropriado, dependendo do ambiente 
# fornecido. Se o ambiente for "test", o arquivo será salvo em "src/test/jsons"; caso contrário, será salvo em "src/jsons". 
# A função converte as chaves do dicionário para strings antes de salvar. Retorna um dicionário indicando o sucesso ou falha da operação.

# Acoplamento:
# O parâmetro `ambiente` deve ser uma string para determinar o caminho do arquivo.
# O parâmetro `dicionarioPlaylists` deve ser um dicionário cujas chaves podem ser convertidas para strings e valores seguem 
# a estrutura de playlists (listas de tuplas de músicas).
# Depende da função `converteChavesParaString` para ajustar as chaves do dicionário para um formato compatível com JSON.
# O `codigo_retorno` pode ser:
# - 1: Sucesso (arquivo salvo com sucesso).
# - 0: Falha (dicionário inexistente ou erro ao salvar).

# Condições de Acoplamento:
# - A função depende do módulo `os` para criar o diretório se ele não existir.
# - O arquivo deve ser gravável no sistema de arquivos.
# - Caso o dicionário esteja vazio, a função retorna erro sem tentar gravar o arquivo.

# Hipóteses:
# - Assume-se que o dicionário fornecido é válido para escrita em JSON.

# Interface com o Usuário:
# - Retorna um dicionário com `codigo_retorno` e `mensagem` para informar o status da operação.

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

# Descrição:
# Esta função lê um arquivo JSON contendo playlists e atualiza o dicionário `dicionarioPlaylists` com os dados obtidos. 
# O ambiente (`ambiente`) define o caminho onde o arquivo JSON será buscado: "src/test/jsons" para testes ou "src/jsons" 
# para o ambiente padrão. Caso a leitura do arquivo seja bem-sucedida, o dicionário é atualizado e a função retorna um 
# dicionário indicando sucesso. Caso contrário, retorna uma mensagem de erro genérica.

# Acoplamento:
# - O parâmetro `ambiente` deve ser uma string para determinar o caminho do arquivo.
# - O parâmetro `dicionarioPlaylists` é um dicionário que será atualizado com os dados lidos.
# - Depende da função `reverterChavesParaTipoOriginal`, que converte as chaves do JSON de volta ao tipo esperado.
# - O `codigo_retorno` pode ser:
#   - 1: Sucesso (dicionário atualizado com dados do arquivo).
#   - 0: Falha (erro ao ler o arquivo).

# Condições de Acoplamento:
# - Depende da estrutura do arquivo JSON, que deve ser um dicionário com playlists e suas músicas.
# - Caso o arquivo esteja vazio ou inválido, a função retorna erro sem atualizar o dicionário.

# Hipóteses:
# - Assume-se que o arquivo JSON existe e está acessível no caminho especificado.

# Interface com o Usuário:
# - Retorna um dicionário com `codigo_retorno` e `mensagem` para informar o status da operação.

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

# Descrição:
# Esta função obtém os nomes de todas as playlists disponíveis no dicionário `dicionarioPlaylists`. Caso existam playlists, 
# retorna um dicionário com `codigo_retorno` 1, os nomes das playlists e uma mensagem de sucesso. Caso contrário, retorna 
# um dicionário indicando falha.

# Acoplamento:
# - O parâmetro `dicionarioPlaylists` é um dicionário cujas chaves representam os nomes das playlists.
# - O `codigo_retorno` pode ser:
#   - 1: Sucesso (nomes das playlists obtidos).
#   - 0: Falha (nenhuma playlist disponível).

# Condições de Acoplamento:
# - Depende da estrutura do `dicionarioPlaylists`, que deve ser um dicionário com nomes de playlists como chaves.
# - A função retorna `None` no campo `nomes` caso o dicionário esteja vazio.

# Hipóteses:
# - Assume-se que `dicionarioPlaylists` segue a estrutura esperada.

# Interface com o Usuário:
# - Retorna um dicionário com `codigo_retorno`, `nomes` (lista ou `None`) e `mensagem` para informar o status da operação.

def obterNomesPlaylists(dicionarioPlaylists=dicionarioPlaylists):
    if dicionarioPlaylists:
        return {"codigo_retorno": 1, "nomes": dicionarioPlaylists.keys(), "mensagem": "Nomes das playlists obtidos com sucesso."}
    return {"codigo_retorno": 0, "nomes": None, "mensagem": "Falha ao obter nomes das playlists"}

# Descrição:
# Esta função recupera todas as músicas de uma playlist específica (`nomePlaylist`) a partir do dicionário `dicionarioPlaylists`. 
# Caso a playlist exista, retorna um dicionário com `codigo_retorno` 1, as músicas da playlist e uma mensagem de sucesso. 
# Caso contrário, retorna um dicionário indicando falha.

# Acoplamento:
# - O parâmetro `nomePlaylist` é uma string que representa o nome da playlist a ser consultada.
# - O parâmetro `dicionarioPlaylists` é um dicionário onde as chaves são os nomes das playlists e os valores são listas de músicas.
# - O `codigo_retorno` pode ser:
#   - 1: Sucesso (músicas obtidas com sucesso).
#   - 0: Falha (playlist inexistente).

# Condições de Acoplamento:
# - Depende da estrutura do `dicionarioPlaylists`, que deve ser um dicionário onde as músicas de cada playlist são representadas 
# como listas de tuplas (nomeAutor, nomeMusica).
# - A função retorna `None` no campo `musicas` caso a playlist não exista.

# Hipóteses:
# - Assume-se que `dicionarioPlaylists` segue a estrutura esperada.

# Interface com o Usuário:
# - Retorna um dicionário com `codigo_retorno`, `musicas` (lista ou `None`) e `mensagem` para informar o status da operação.

def obtemMusicasDePlaylist(nomePlaylist, dicionarioPlaylists=dicionarioPlaylists):
    if nomePlaylist in dicionarioPlaylists.keys():
        return {"codigo_retorno":1, "musicas": dicionarioPlaylists[nomePlaylist], "mensagem": "Músicas obtidas com sucesso"}
    return {"codigo_retorno":0, "musicas": None, "mensagem":"Não foi possível obter as músicas da playlist"}