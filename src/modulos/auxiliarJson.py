import ast

def converteChavesParaString(data):
    if isinstance(data, dict):
        novoDict = {}
        for key, value in data.items():
            if isinstance(key, tuple):
                key = f"tuple:{key}"  # Converte a tupla para string com prefixo
            elif isinstance(key, int):
                key = f"int:{key}"
            elif isinstance(key, float):
                key = f"float:{key}"
            elif isinstance(key, bool):
                key = f"bool:{key}"
            else:
                key = f"str:{key}"  # Default para strings

            novoDict[key] = converteChavesParaString(value)
        return novoDict
    elif isinstance(data, list):
        return [converteChavesParaString(element) for element in data]
    else:
        return data

def reverterChavesParaTipoOriginal(data):
    if isinstance(data, dict):
        novoDict = {}
        for key, value in data.items():
            # Reverte tuplas
            if key.startswith("tuple:"):
                key = ast.literal_eval(key[6:])  # Converte a string de volta para uma tupla
            elif key.startswith("int:"):
                key = int(key[4:])
            elif key.startswith("float:"):
                key = float(key[6:])
            elif key.startswith("bool:"):
                key = key[5:] == "True"
            else:
                key = key[4:]  # Remove "str:" para chaves de string

            novoDict[key] = reverterChavesParaTipoOriginal(value)
        return novoDict
    elif isinstance(data, list):
        return [reverterChavesParaTipoOriginal(element) for element in data]
    else:
        return data
