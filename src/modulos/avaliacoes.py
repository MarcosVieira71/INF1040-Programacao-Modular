from modulos.auxiliarJson import *

import json
import os

__all__ = ["criarAvaliacao","excluirAvaliacao", "atualizaAvaliacao", "leJsonAvaliacoes", "escreveJsonAvaliacoes", "exportarAvaliacoes", "geraStringAvaliacao", "verificaAvaliacao"]


dicionarioAvaliacoes={}

# Descrição:
# Esta função cria uma avaliação para uma música específica, recebendo como entrada o nome do autor (`nomeAutor`), 
# o nome da música (`nomeMusica`), uma nota (`nota`), o texto da avaliação (`texto`) e um dicionário de avaliações (`dicionarioAvaliacoes`).
# A função verifica se a música existe no sistema utilizando `verificaMusica`. Se a música existir e ainda não houver 
# uma avaliação para ela, a avaliação é adicionada ao dicionário, e a função retorna um dicionário com `codigo_retorno` 1 e uma 
# mensagem de sucesso. Caso contrário, retorna um código de erro (`codigo_retorno` -1 ou 0) e a respectiva mensagem.

# Acoplamento:
# A função depende de outra função `verificaMusica` (do módulo `musica`) para validar a existência da música no sistema.
# A entrada `dicionarioAvaliacoes` deve ser um dicionário onde as chaves são tuplas (autor, música) e os valores são 
# dicionários com as chaves `nota` e `texto`.

# Condições de Acoplamento:
# - O dicionário de avaliações deve seguir a estrutura esperada.
# - A função assume que `nomeAutor`, `nomeMusica` e `texto` são strings válidas e que `nota` é um inteiro.

# Hipóteses:
# - A música já deve existir no sistema para que a avaliação seja criada.
# - Não são aceitas duplicatas de avaliações para o mesmo autor e música.

# Interface com o Usuário:
# A função não interage diretamente com o usuário, mas retorna um dicionário com informações de sucesso ou erro,
# que podem ser usadas por interfaces para exibir mensagens ao usuário.

def criarAvaliacao(nomeAutor: str, nomeMusica: str, nota: int, texto: str, dicionarioAvaliacoes=dicionarioAvaliacoes):
    from modulos.musica import verificaMusica
    resultado = {
        "codigo_retorno": 0,
        "avaliacao": {}
    }

    verifica_musica = verificaMusica(nomeAutor, nomeMusica)
    if verifica_musica["codigo_retorno"] == 1:  
        chave = (nomeAutor, nomeMusica)
        if chave in dicionarioAvaliacoes:
            resultado["mensagem"] = "Avaliação já existente para esta música"
            resultado["codigo_retorno"] = -1
            return resultado
        dicionarioAvaliacoes[chave] = {
            "nota": nota,
            "texto": texto
        }

        resultado["codigo_retorno"] = 1
        resultado["mensagem"] = "Avaliação criada com sucesso"
        resultado["avaliacao"] = {
            "nota": nota,
            "texto": texto
        }
    else:
        resultado["mensagem"] = "Música não encontrada"

    return resultado

# Descrição:
# A função verifica se há uma avaliação correspondente para um determinado par (autor, música) no dicionário de avaliações 
# (`dicionarioAvaliacoes`). Retorna um dicionário com `codigo_retorno` 1 e uma mensagem de sucesso caso a avaliação seja encontrada. 
# Caso contrário, retorna um código de erro (`codigo_retorno` 0) com uma mensagem indicando que a avaliação não foi encontrada.

# Acoplamento:
# - A função utiliza diretamente o dicionário de avaliações (`dicionarioAvaliacoes`).
# - A entrada `dicionarioAvaliacoes` deve conter tuplas (autor, música) como chaves.

# Condições de Acoplamento:
# - O dicionário deve seguir a estrutura esperada, com tuplas como chaves e dicionários contendo "nota" e "texto" como valores.

# Hipóteses:
# - A função assume que `nomeAutor` e `nomeMusica` são strings válidas.

# Interface com o Usuário:
# A função retorna um dicionário com `codigo_retorno` e `mensagem`, permitindo que as interfaces exibam resultados ao usuário.

def verificaAvaliacao(nomeAutor: str, nomeMusica: str, dicionarioAvaliacoes=dicionarioAvaliacoes):
  resultado={
    "codigo_retorno":0,
    "mensagem":"Avaliação inexistente",
  }
  chave=(nomeAutor,nomeMusica)
  if chave in dicionarioAvaliacoes:
    resultado["codigo_retorno"]=1
    resultado["mensagem"] = "Avaliação encontrada"
  return resultado


# Descrição:
# Esta função remove uma avaliação específica de uma música no dicionário de avaliações (`dicionarioAvaliacoes`), 
# recebendo como entrada o nome do autor (`nomeAutor`) e o nome da música (`nomeMusica`). Caso a avaliação exista, 
# ela é removida do dicionário, e a função retorna um dicionário com `codigo_retorno` 1 e uma mensagem de sucesso.
# Caso a avaliação não exista, a função retorna um dicionário com `codigo_retorno` 0 e uma mensagem indicando que 
# a avaliação não foi encontrada.

# Acoplamento:
# - A função depende do dicionário `dicionarioAvaliacoes`, que deve conter as avaliações organizadas com tuplas 
# (autor, música) como chaves.

# Condições de Acoplamento:
# - O dicionário de avaliações deve seguir a estrutura padrão.
# - A entrada `nomeAutor` e `nomeMusica` devem ser strings válidas.

# Hipóteses:
# - A função assume que o dicionário contém a estrutura correta e que os parâmetros são válidos.

# Interface com o Usuário:
# A função não possui interação direta com o usuário, mas fornece mensagens claras de sucesso ou erro através do retorno.

def excluirAvaliacao(nomeAutor: str, nomeMusica: str, dicionarioAvaliacoes=dicionarioAvaliacoes):
  resultado={
    "codigo_retorno":0,
    "mensagem":"Avaliação inexistente",
  }
  chave = (nomeAutor, nomeMusica)
  if chave in dicionarioAvaliacoes:
    del dicionarioAvaliacoes[chave]  
    resultado["codigo_retorno"] = 1
    resultado["mensagem"] = "Avaliação excluída com sucesso"

  return resultado


# Descrição:
# Esta função recebe como parâmetros o nome do autor (`nomeAutor`), o nome da música (`nomeMusica`), uma nova nota 
# (`nota`) e o novo texto da avaliação (`texto`). A função verifica se existe uma entrada correspondente no `dicionarioAvaliacoes` 
# para o par (nome do autor, nome da música). Caso a entrada exista, a função atualiza a nota e o texto da avaliação e retorna 
# um dicionário com `codigo_retorno` 1 e uma mensagem de sucesso. Caso contrário, retorna um dicionário com `codigo_retorno` 0 
# e uma mensagem indicando que a avaliação não foi encontrada.
# Caso a chave (nome do autor, nome da música) não exista no dicionário, a função não lança uma exceção, mas retorna uma mensagem de erro.

# Acoplamento: 
# A função assume que vai receber strings nos parâmetros nomeAutor, nomeMusica e texto sem restrição de tamanho. A nota é um inteiro e assume
# que vai ter valor entre 0 e 5. O parâmetro dicionarioAvaliacoes espera receber um dicionario com avaliacoes num formato em que as chaves
# são tuplas com duas strings nelas.  
#  Os retornos são sempre em forma de dicionário com campos de "codigo_retorno" e "mensagem", sendo o codigo de retorno um valor inteiro
# 0 ou 1 (1 para representar que tudo funcionou de acordo e 0 para indicar que houve um erro na execução da função).  A mensagem só informa o que aconteceu durante
# a execução da função.
# 
# Condições de Acoplamento: 
# A função depende de `dicionarioAvaliacoes` como um dicionário em que as chaves são tuplas (nome do autor, nome da música) 
# e os valores são dicionários contendo as chaves "nota" e "texto".

# Hipóteses:
# - A função assume que `dicionarioAvaliacoes` segue a estrutura esperada.
# - A nota e o texto fornecidos devem ser do tipo `int` e `str`, respectivamente, para evitar problemas de tipo.

# Interface com o Usuário:
# A função não interage diretamente com o usuário, mas retorna um dicionário com `codigo_retorno` e `mensagem`, que podem 
# ser utilizados por uma interface para exibir feedback ao usuário.

def atualizaAvaliacao(nomeAutor: str, nomeMusica: str, nota: int, texto: str, dicionarioAvaliacoes=dicionarioAvaliacoes):
    resultado={
        "codigo_retorno":0,
        "mensagem":"Avaliação inexistente"
    }
    chave = (nomeAutor, nomeMusica)
    if chave in dicionarioAvaliacoes:
        dicionarioAvaliacoes[chave]["nota"] = nota
        dicionarioAvaliacoes[chave]["texto"] = texto
        resultado["codigo_retorno"] = 1
        resultado["mensagem"] = "Avaliação atualizada com sucesso"
    return resultado

# Descrição:
# A função tenta carregar avaliações a partir de um arquivo JSON no disco. O parâmetro `ambiente` define 
# se o arquivo será lido do ambiente de teste ou produção. Após carregar os dados, a função atualiza o 
# `dicionarioAvaliacoes` com as avaliações do arquivo e retorna um dicionário com `codigo_retorno` 1 e uma mensagem de sucesso. 
# Caso ocorra algum erro, retorna `codigo_retorno` 0 e uma mensagem de erro.

# Acoplamento:
# - A função depende de um arquivo JSON organizado corretamente e da função auxiliar `reverterChavesParaTipoOriginal`.

# Condições de Acoplamento:
# - O arquivo JSON deve existir e conter os dados no formato esperado.

# Hipóteses:
# - O ambiente deve ser corretamente especificado como "test" ou "prod".
# - O arquivo JSON segue a estrutura de avaliações esperada.

# Interface com o Usuário:
# A função não interage diretamente com o usuário, mas retorna mensagens claras sobre o sucesso ou falha da operação.

def leJsonAvaliacoes(ambiente, dicionarioAvaliacoes=dicionarioAvaliacoes):
    if ambiente == "test":
        caminhoPasta = "src/test/jsons"
    else:
        caminhoPasta = "src/jsons"
    
    resultado = {
        "codigo_retorno": 0,
        "mensagem": "Erro ao ler o arquivo",
    }
    caminhoArquivo = os.path.join(caminhoPasta, "avaliacoes.json")
    try:
        with open(caminhoArquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            dicionarioAvaliacoes.clear()
            
            dicionarioAvaliacoes.update(reverterChavesParaTipoOriginal(dados))

            resultado["codigo_retorno"] = 1
            resultado["mensagem"] = "Avaliações obtidas com sucesso"
    except Exception as e:
       pass

    return resultado

# Descrição:
# A função salva o dicionário de avaliações (`dicionarioAvaliacoes`) em um arquivo JSON no disco. O parâmetro `ambiente` 
# define se o arquivo será salvo no ambiente de teste ou produção. Caso o dicionário esteja vazio ou ocorra algum erro, 
# a função retorna `codigo_retorno` 0 e uma mensagem indicando o problema. Caso a operação seja bem-sucedida, retorna 
# `codigo_retorno` 1 e uma mensagem de sucesso.

# Acoplamento:
# - A função depende do dicionário de avaliações (`dicionarioAvaliacoes`) e da função `converteChavesParaString` para 
# converter as chaves antes de salvar.

# Condições de Acoplamento:
# - O dicionário deve seguir a estrutura esperada.
# - O ambiente deve ser corretamente especificado como "test" ou "prod".

# Hipóteses:
# - O dicionário contém dados válidos e estruturados.

# Interface com o Usuário:
# A função fornece mensagens sobre o status da operação, permitindo feedback claro para o usuário final.

def escreveJsonAvaliacoes(ambiente, dicionarioAvaliacoes=dicionarioAvaliacoes):
    if ambiente == "test":
        caminhoPasta = "src/test/jsons"
    else:
        caminhoPasta = "src/jsons"
    
    resultado={
        "codigo_retorno":0,
        "mensagem":"Erro ao escrever o arquivo, dicionário inexistente.",
    }

    if not dicionarioAvaliacoes:
        return resultado
    
    try:
        os.makedirs(caminhoPasta, exist_ok=True)
        dicionarioAvaliacoes = converteChavesParaString(dicionarioAvaliacoes)
        caminhoArquivo = os.path.join(caminhoPasta, "avaliacoes.json")
        with open(caminhoArquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dicionarioAvaliacoes, arquivo, indent=4, ensure_ascii=False)
            resultado["codigo_retorno"]=1
            resultado["mensagem"]="Arquivo escrito com sucesso"
    except Exception as e:
        pass
    return resultado



# Descrição:
# Esta função gera uma string formatada com as informações de uma avaliação. Recebe como parâmetros o nome do autor 
# (`nomeAutor`), o nome da música (`nomeMusica`), e o dicionário de avaliações (`dicionarioAvaliacoes`). Se a avaliação 
# for encontrada, retorna a string formatada e `codigo_retorno` 1. Caso contrário, retorna uma mensagem de erro com 
# `codigo_retorno` 0.

# Acoplamento:
# - A função depende do dicionário de avaliações, que deve conter chaves no formato de tuplas (autor, música).

# Condições de Acoplamento:
# - O dicionário deve conter avaliações organizadas corretamente.

# Hipóteses:
# - Os parâmetros fornecidos são strings válidas e correspondem a uma avaliação existente.

# Interface com o Usuário:
# A função retorna mensagens claras para que as interfaces possam exibir o resultado da operação ao usuário.


def geraStringAvaliacao(nomeAutor: str, nomeMusica: str, dicionarioAvaliacoes=dicionarioAvaliacoes):
    resultado = {
        "codigo_retorno": 0,
        "stringAvaliacao": ""
    }
    chave = (nomeAutor, nomeMusica)

    if chave in dicionarioAvaliacoes:
        avaliacao = dicionarioAvaliacoes[chave]
        resultado["stringAvaliacao"] = f"Avaliação do {nomeMusica} do artista {nomeAutor}\n\n {avaliacao['texto']} \n\n Nota: {avaliacao['nota']} estrelas"
        resultado["codigo_retorno"] = 1
    else:
        resultado["stringAvaliacao"] = "Erro: Avaliação não encontrada."

    return resultado

# Descrição:
# A função exporta as avaliações em formato de texto, convertendo-as para a codificação especificada 
# (`tipoCodificacao`). As avaliações são extraídas do dicionário (`dicionarioAvaliacoes`) e processadas em uma lista 
# de strings formatadas. Caso a exportação seja bem-sucedida, a função retorna `codigo_retorno` 1 e uma mensagem de sucesso. 
# Caso contrário, retorna `codigo_retorno` 0 e uma mensagem de erro.

# Acoplamento:
# - A função depende do módulo `texto` para converter e salvar os textos em diferentes formatos de codificação.

# Condições de Acoplamento:
# - O dicionário de avaliações deve seguir a estrutura esperada.
# - As strings geradas são corretamente formatadas antes de serem exportadas.

# Hipóteses:
# - O tipo de codificação fornecido é válido e suportado pelo módulo `texto`.

# Interface com o Usuário:
# A função fornece mensagens claras para que as interfaces possam informar o status da operação ao usuário.

def exportarAvaliacoes(tipoCodificacao, dicionarioAvaliacoes=dicionarioAvaliacoes):
    from modulos.texto import geraTxtAvaliacoes
    listaStrings = []
    for autor, musica in dicionarioAvaliacoes.keys():
        stringAvaliacaoRetorno = geraStringAvaliacao(autor, musica)  # Gera string da avaliação
        if not stringAvaliacaoRetorno["codigo_retorno"]:
            return {"codigo_retorno": -1, "mensagem": "Erro no formato de texto"}
        listaStrings.append(stringAvaliacaoRetorno["stringAvaliacao"])

    resultado = geraTxtAvaliacoes(listaStrings, tipoCodificacao)

    if resultado["codigo_retorno"] == 1:
        return {"codigo_retorno": 1, "mensagem": "Arquivo de avaliações escrito com sucesso"}
    else:
        return {"codigo_retorno": 0, "mensagem": "Erro ao escrever o arquivo de avaliações"}
