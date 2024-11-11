from modulos.auxiliarJson import *

import json
import os

dicionarioAvaliacoes={}

def criarAvaliacao(nomeAutor: str, nomeMusica: str, nota: int, texto: str, dicionarioAvaliacoes=dicionarioAvaliacoes):
    from modulos.musica import verificaMusica
    resultado = {
        "codigo_retorno": 0,
        "mensagem": "Erro ao criar a avaliação",
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

def leJsonAvaliacoes(dicionarioAvaliacoes=dicionarioAvaliacoes):
    resultado = {
        "codigo_retorno": 0,
        "mensagem": "Erro ao ler o arquivo ",
        "dicionario_avaliacoes": {}
    }

    try:
        with open("src/jsons/avaliacoes.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            dicionarioAvaliacoes.clear()
            dicionarioAvaliacoes.update(dados)

            resultado["codigo_retorno"] = 1
            resultado["mensagem"] = "Avaliações obtidas com sucesso"
            resultado["dicionario_avaliacoes"] = dicionarioAvaliacoes
    except Exception as e:
       pass

    return resultado

def escreveJsonAvaliacoes(dicionarioAvaliacoes=dicionarioAvaliacoes):
    resultado={
        "codigo_retorno":0,
        "mensagem":"Erro ao escrever o arquivo de avaliações",
    }
    try:
        os.makedirs("src/jsons", exist_ok=True)
        # Falar sobre com o Marcos
        dicionarioAvaliacoes = converteChavesParaString(dicionarioAvaliacoes)
        
        with open("src/jsons/avaliacoes.json", "w", encoding="utf-8") as arquivo:
            json.dump(dicionarioAvaliacoes, arquivo, indent=4, ensure_ascii=False)
            resultado["codigo_retorno"]=1
            resultado["mensagem"]="Arquivo escrito com sucesso"
    except Exception as e:
        pass
    return resultado

def geraStringAvaliacao(nomeAutor: str, nomeMusica: str, dicionarioAvaliacoes=dicionarioAvaliacoes):
    resultado = {
        "codigo_retorno": 0,
        "stringAvaliacao": ""
    }
    chave = (nomeAutor, nomeMusica)

    if chave in dicionarioAvaliacoes:
        avaliacao = dicionarioAvaliacoes[chave]
        resultado["stringAvaliacao"] = f"Avaliação do {nomeMusica} do artista {nomeAutor}:\n{avaliacao['texto']}"
        resultado["codigo_retorno"] = 1
    else:
        resultado["stringAvaliacao"] = "Erro: Avaliação não encontrada."

    return resultado

