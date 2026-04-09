"""
Aula: Mais detalhes sobre List Comprehension

Resumo:
List Comprehension é uma forma compacta e elegante de criar listas em Python.

Sintaxe básica:
    [expressao for item in iteravel]

Com condicionais:
    [expressao for item in iteravel if condicao]

Com if/else (ternário):
    [expressao_if if condicao else expressao_else for item in iteravel]

Principais usos:
- Filtrar valores
- Transformar dados
- Criar combinações (loops aninhados)
- Trabalhar com strings e listas

Vantagens:
- Código mais curto
- Mais legível (quando bem usado)
- Mais "pythonico"
"""

# 1 - Filtrando valores com IF
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Cria uma nova lista apenas com números maiores que 5
novo_numeros = [numero for numero in numeros if numero > 5]

# Cria lista com números ímpares
impares = [numero for numero in numeros if numero % 2 != 0]

# Cria lista com números pares
pares =[numero for numero in numeros if numero % 2 == 0]

# 2 - Usando IF/ELSE dentro da expressão (ternário)
# Aqui NÃO é filtro, é transformação
outro_if = [
    numero if numero != 6 else 600
    for numero in pares
]

# 3 - "Achatar" lista (FLAT)
# Criando lista de listas: [numero, numero2]
numeros = [[numero, numero ** 2] for numero in range(5)]

# Transformado em uma lista simples (flatten)
flat = [y for x in numeros for y in x]

# 4 - Loops aninhados (linhas e colunas)
linhas_e_colunas = [
    (x, y) if y != 2 else (x, y * 1000)
    for x in range(1, 5)
    for y in range(1, 4)
    if x != 2
]

# 5 - Trabalhando com strings
nomes = ['Wonwoo', 'Vernon', 'Jun']

# Deixa última letra maiúscula e resto minúsculo
novos_nomes = [
    f'{nome[:-1].lower()}{nome[-1].upper()}'
    for nome in nomes
]

# 6 - Cópia de lista (sem referência)
numeros = [1, 2, 3]
novo_numeros = [numero for numero in numeros]

# Alterando lista original
numeros[0] = 999

# novo_numeros NÃO muda (cópia independente)

# 7 - Trabalhando com strings em blocos
string = 'Jeon Wonwoo'
numero_de_letras = 2

# Divide string em pedaços de 2 caracteres
nova_string = '.'.join([
    string[i:i + numero_de_letras]
    for i in range(0, len(string), numero_de_letras)
])

# 8 - Usando funções dentro de list comprehension

def divisaofn(x, y):
    return x / y

def multiplicacaofn(x, y):
    return x * y

def potenciacaofn(x, y):
    return x ** y

numeros = [1, 2, 3, 4]

# Aplica funções em todos os elementos
divisao = [divisaofn(n, 2) for n in numeros]
multiplicacao = [multiplicacaofn(n, 2) for n in numeros]
quadrado = [potenciacaofn(n, 2) for n in numeros]