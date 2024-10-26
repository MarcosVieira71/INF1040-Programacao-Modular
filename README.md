# INF1040 - Player de Música

## Descrição

Este é o projeto do Player de Música para a disciplina INF1040. O projeto inclui um ambiente virtual Python e um conjunto de bibliotecas necessárias para executar o sistema.

## Instalação e Configuração

### Passo 1: Configurar Ambiente Virtual

Windows:
```bash
python3 -m venv env
.\env\Scripts\activate
```
Linux/MacOS
```bash
python3 -m venv env
source env/bin/activate
```


### Passo 2: Instale as dependências

As bibliotecas necessárias para o projeto estão listadas no arquivo `requirements.txt`. Use o comando abaixo para instalá-las:

```bash
pip install -r requirements.txt
```

## Estrutura de Branches

### 1. Trabalhe na Branch `develop`
Utilizem sempre a branch `develop` para trabalhar nas alterações do programa

### 2. Crie uma Nova Branch para Cada Funcionalidade
Criem uma branch específica a partir de `develop`. Nomeie a branch de forma descritiva para indicar a funcionalidade ou a correção que está sendo trabalhada.

### 3. Finalize e Faça o Merge
Após concluir o trabalho em uma branch de funcionalidade, faça o merge da nova branch para `develop`. Submeta as alterações para validação antes de prosseguir.

### 4. Validação e Merge para `main`
Somente após as validações e testes necessários, daremos merge da branch `develop` para a branch `main`. Isso garante que `main` sempre contenha uma versão estável.
