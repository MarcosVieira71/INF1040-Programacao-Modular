import os
import platform
import ctypes

__all__ = ["geraTxtAvaliacoes"]

def retornaLibPath():
    sistemaOperacional = platform.system()
    if sistemaOperacional == "Windows":
        lib = "converteutf.dll"
        libcpath = "msvcrt.dll"  # Biblioteca padrão C no Windows

    elif sistemaOperacional == "Darwin": 
        lib = "converteutf.dylib"
        libcpath = None  # Usado em Linux/macOS

    else:  
        lib = "converteutf.so"
        libcpath = None  # Usado em Linux/macOS

    return os.path.join(os.path.dirname(__file__), "libsSB", lib), libcpath




def converteUtf8_32Linux(caminho_entrada, caminho_saida):
    
    libPath, libcpath = retornaLibPath()
    converteutf = ctypes.CDLL(libPath)

    converteutf.convUtf8p32.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    converteutf.convUtf8p32.restype = ctypes.c_int

    libc = ctypes.CDLL(libcpath)
    libc.fdopen.argtypes = [ctypes.c_int, ctypes.c_char_p]
    libc.fdopen.restype = ctypes.c_void_p

    try:
        entrada_fd = os.open(caminho_entrada, os.O_RDONLY)
        saida_fd = os.open(caminho_saida, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o666)

        entrada_file = libc.fdopen(entrada_fd, b"rb")
        saida_file = libc.fdopen(saida_fd, b"wb")

        resultado = converteutf.convUtf8p32(entrada_file, saida_file)

        if resultado == 0:
            return {"codigo_retorno": 1, "mensagem": "Conversão UTF-8 para UTF-32 concluída com sucesso"}
        else:
            return {"codigo_retorno": 0, "mensagem": "Erro na conversão UTF-8 para UTF-32"}
    finally:
        os.close(entrada_fd)
        os.close(saida_fd)

def geraTxtAvaliacoes(listaStrings, tipoCodificacao):
    resultado = {"codigo_retorno": 1, "mensagem": "Relatório de avaliações gerado com sucesso"}
    pastaRelatorios = os.path.join(os.path.dirname(__file__), "../relatorios")
    os.makedirs(pastaRelatorios, exist_ok=True)  
    caminho_utf8 = os.path.join(pastaRelatorios, "avaliacoes_utf8.txt")
    caminho_utf32 = os.path.join(pastaRelatorios, "avaliacoes_utf32.txt")

    with open(caminho_utf8, 'w', encoding='utf-8') as arquivo:
        arquivo.write("\n\n".join(listaStrings))

    if tipoCodificacao == "UTF-32":
        sistemaOperacional = platform.system()
        if sistemaOperacional == "Windows":
            resultadoConversao = converteUtf8_32Windows(caminho_utf8, caminho_utf32)
        else: resultadoConversao = converteUtf8_32Linux(caminho_utf8, caminho_utf32)
        
        if resultadoConversao["codigo_retorno"] == 1:
            os.remove(caminho_utf8)  
        else:
            return {"codigo_retorno": 0, "mensagem": resultadoConversao["mensagem"]}
    else:

        if os.path.exists(caminho_utf32): os.remove(caminho_utf32)  
        resultadoConversao = resultado
    return resultadoConversao

def converteUtf8_32Windows(caminho_entrada, caminho_saida):
    libPath, libcpath = retornaLibPath()
    converteutf = ctypes.CDLL(libPath)

    # Configurar os argumentos e retorno da função convUtf8p32
    converteutf.convUtf8p32.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    converteutf.convUtf8p32.restype = ctypes.c_int

    # Carregar a biblioteca padrão C no Windows
    libc = ctypes.CDLL(libcpath)
    libc.fopen.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
    libc.fopen.restype = ctypes.c_void_p

    libc.fclose.argtypes = [ctypes.c_void_p]
    libc.fclose.restype = ctypes.c_int

    try:
        entrada_file = libc.fopen(caminho_entrada.encode('utf-8'), b"rb")
        saida_file = libc.fopen(caminho_saida.encode('utf-8'), b"wb")

        resultado = converteutf.convUtf8p32(entrada_file, saida_file)
        if resultado == 0:
            return {"codigo_retorno": 1, "mensagem": "Conversão UTF-8 para UTF-32 concluída com sucesso"}
        else:
            return {"codigo_retorno": 0, "mensagem": "Erro na conversão UTF-8 para UTF-32"}
    finally:
        if entrada_file:
            libc.fclose(entrada_file)
        if saida_file:
            libc.fclose(saida_file)
