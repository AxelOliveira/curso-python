"""
Dictionary Comprehension e Set Comprehension

Comprehension é uma forma curta e organizada de criar estruturas de dados em Python usando uma única expressão.

Dictionary comprehension:
- Cria dicionários de forma rápida
- Usa chaves {}
- Sempre precisa de chave: valor
- Pode ter if/else e filtros

Set comprehension:
- Cria conjuntos (set)
- Também usa chaves {}
- Possui apenas valores (não tem chave:valor)
- Não permite valores duplicados
"""

# Exemplo 1 - Dictionary comprehension modificando valores
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

# Percorremos chave e valor com .items()
# Se o valor for string, transforma em MAIÚSCULO
# Ignora a chave 'categoria'
dc = {
    chave: valor.upper() if isinstance(valor, str) else valor
    for chave, valor in produto.items()
    if chave != 'categoria'
}

#--------------------------------------------------------------------------------------------------
# Exemplo 2 - Criando dict a partir de lista de tuplas

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

# Cada tupla (chave, valor) vira um item do dicionário
dc = {
    chave: valor 
    for chave, valor in lista
}

#--------------------------------------------------------------------------------------------------
# Exemplo 3 - Set comprehension

# Cria um conjunto com potências de 2
# Sets não mantêm ordem e não aceitam repetidos
s1 = {2 ** i for i in range(10)}

print(s1)