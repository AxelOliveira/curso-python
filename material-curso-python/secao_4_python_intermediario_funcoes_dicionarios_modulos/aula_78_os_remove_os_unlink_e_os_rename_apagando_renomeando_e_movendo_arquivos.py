"""
TEORIA - MANIPULAÇÃO DE ARQUIVOS COM MÓDULO OS

1. O módulo os permite interagir com o sistema operacional

2. Funções principais:
    - os.remove(caminho)
        -> apaga um arquivo

    - os.unlink(caminho)
        -> mesma coisa que remove

    - os.rename(origem, destino)
        -> renomeia ou move um arquivo

3. IMPORTANTE:
    - O arquivo precisa existir para remover ou renomear
    - Se não existir, dá erro (FileNotFoundError)

4. Boas práticas:
    - Sempre verificar se o arquivo existe antes de apagar
"""
import os

caminho_arquivo = 'aula78.txt'

# 1 - Criando o arquivo
with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')

# 2 - Renomeando o arquivo
novo_nome = 'aula78_novo.txt'
os.rename(caminho_arquivo, novo_nome)

# 3 - Apagando o arquivo renomeado
os.remove(novo_nome)