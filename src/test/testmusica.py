def test_verificaArquivoArquivoValido():
    resultado = verificaArquivo("../../musicas_teste/11 - Max Coveri - Running in the 90's.mp3")
    assert resultado == {'codigo_retorno': 1, 'mensagem': 'Arquivo válido'}

def test_verificaArquivoInvalido():
    resultado = verificaArquivo("../../musicas_teste/arquivo_invalido.txt")
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Arquivo inválido ou inexistente'}

def test_verificaArquivoInexistente():
    resultado = verificaArquivo("../../musicas_teste/arquivo_inexistente.mp3")
    assert resultado == {'codigo_retorno': 0, 'mensagem': 'Arquivo inválido ou inexistente'}

