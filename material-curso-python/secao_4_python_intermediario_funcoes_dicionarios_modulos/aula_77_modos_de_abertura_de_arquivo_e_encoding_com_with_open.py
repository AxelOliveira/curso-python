"""
TEORIA - MODOS DE ABERTURA + ENCODING

1. Modos principais:
    - 'r' -> leitura (arquivo deve existir)
    - 'w' -> escrita (APAGA tudo e escreve de novo)
    - 'a' -> append (NÃO apaga, escreve no final)
    - 'x' -> cria (erro se já existir)
    - '+' -> leitura + escrita

2. Diferença CRÍTICA:
    - w -> sempre começa do zero (zera o arquivo)
    - a -> continua do final (não perde dados)

3. encoding:
    - Define como os caracteres são salvos (acentos, ç, etc)
    - Problema comum no Windows: caracteres quebrados
    - Solução: usar encoding='utf-8'

4. Regra prática:
    - Sempre usar encoding='utf-8'ao trabalhar com texto

5. Cursor continua existindo:
    - Mesmo conceito da aula anterior (seek)
"""
caminho_arquivo = 'aula77.txt'

# 1 - Escrevendo (APAGA tudo sempre)
with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:

    # 2 - Escrevendo com acentuação
    arquivo.write('Atenção\n')
    arquivo.write('Linhas 1\n')

# 3 - Adicionando conteúdo (NÃO apaga)
with open(caminho_arquivo, 'a', encoding='utf-8') as arquivo:

    # 4 - Adiciona no final do arquivo
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')

print('#' * 10)

# 5 - Lendo o arquivo
with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    print(arquivo.read())