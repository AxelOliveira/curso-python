"""
TEORIA - LEITURA E ESCRITA DE ARQUIVOS + CURSOR

1. Modos importantes:
    - 'w' -> escreve (apaga tudo antes)
    - 'r' -> lê
    - 'w+' -> escreve e permite ler

2. Cursor do arquivo:
    - Sempre que você escreve ou lê, o "cursor" se move
    - Após escrever, o cursos fica no FINAL do arquivo
    - Para ler novamente, precisa voltar com seek(0)

3. Métodos principais:
    - write()   -> escreve uma string
    - writelines() -> escreve várias linhas (iterável)
    - read()    -> lê tudo
    - readline() -> lê uma linha por vez
    - readlines() -> retorna lista de linhas

4. Problema comum:
    - print() NÃO escreve no arquivo
    - quebra de linha precisa ser manual: \n

5. strip():
    - remove espaços e quebras de linha
"""
caminho_arquivo = 'aula76.txt'

# 1 - Criando e escrevendo no arquivo
with open(caminho_arquivo, 'w+') as arquivo:

    # 2 - Escrevendo linhas manualmente
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')

    # 3 - Escrevendo múltiplas linhas
    arquivo.writelines(('Linha 3\n', 'Linha 4\n'))  

    # 4 - Voltando o cursor para o início do arquivo
    arquivo.seek(0)

    # 5 - Lendo todo o conteúdo
    print(arquivo.read())

    print('--- Lendo linha por linha ---')

    # 6 - Voltando novamente o cursor
    arquivo.seek(0)

    # 7 - Lendo linha por linha manualmente
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())

    print('--- READLINES ---')

    # 8 - Voltando o cursor novamente
    arquivo.seek(0)

    # 9 - Lendo todas as linhas como lista
    for linha in arquivo.readlines():
        print(linha.strip())

# 10 - Arquivo já fechado automaticamente aqui
print('#' * 10)

# 11 - Abrindo apenas para leitura
with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())