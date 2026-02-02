"""
🟢 Exercício 1 — Dobro de números pares
Crie uma nova lista contendo o dobro apenas dos números pares de 0 a 20.

Estrutura esperada (comentários):
# 1. Criar uma lista usando list comprehension
# 2. Percorrer os números de 0 a 20
# 3. Filtrar apenas números pares
# 4. Mapear retornando o dobro do número
"""
# 1 - Criação da list comprehension
numeros_pares = [
    # 4 - Retorna o dobro do número
    numero * 2
    # 2 - Percorre os números de 0 a 20
    for numero in range (21)
    # 3 - Filtra apenas números pares (resto da divisão por 2 igual a zero)
    if numero % 2 == 0
]

print(numeros_pares)

# --------------------------------------------------------------------------------------------

"""
🟢 Exercício 2 — Nomes em maiúsculo
Dada uma lista de nomes, crie outra lista com todos os nomes em letras maiúsculas.

Estrutura:
# 1. Criar uma nova lista
# 2. Percorrer a lista de nomes
# 3. Mapear cada nome para maiúsculo
"""
# 1 - Lista original de nomes
nomes = ['wonwoo', 'vernon', 'jaemin', 'jeno', 'san', 'eric']

# 2 - Criação de uma nova lista usando list comprehension
nova_lista = [
    # 3 - Converte cada nome para letras maiúsculas
    nome.upper()
    # 4 - Percorre cada nome da lista original
    for nome in nomes
]

print(nova_lista)

# --------------------------------------------------------------------------------------------

"""
🟢 Exercício 3 — Filtro de números maiores que 10
Crie uma lista apenas com números maiores que 10 de uma lista original.

Estrutura:
# 1. Criar nova lista com list comprehension
# 2. Percorrer a lista original
# 3. Filtrar valores maiores que 10
"""
# 1 - Lista original com números abaixo e acima 10
numeros_originais = [7, 42, 15, 3, 89, 24, 10, 56, 1, 77]

# 2 - Nova lista usando list comprehension
nova_lista_de_numeros = [
    # 4 - Retorna apenas números maiores que 10
    numero
    # 3 - Percorre a lista original
    for numero in numeros_originais
    if numero > 10
]

print(nova_lista_de_numeros)

# --------------------------------------------------------------------------------------------

"""
🟢 Exercício 4 — Aumento condicional de preços
Dada uma lista de produtos, aumente o preço em 10% apenas para produtos acima de 50.

Estrutura:
# 1. Criar uma nova lista de produtos
# 2. Percorrer a lista de produtos
# 3. Usar mapeamento com if/else
# 4. Manter produtos sem alteração quando não atenderem a condição
"""
# 1 - Lista original
lista_produtos = [
    {'produto': 'Fone de ouvido', 'preco': 129.90},
    {'produto': 'Caderno universitário', 'preco': 18.90},
    {'produto': 'Ventilador de mesa', 'preco': 89.00},
    {'produto': 'Barra de cereal', 'preco': 4.20},
    {'produto': 'Mouse sem fio', 'preco': 65.50},
]

# 2 - Nova lista usando list comprehension
nova_lista = [
    # 3 - Se o preço for maior que 50, cria cópia com aumento de 10%
    {**produto, 'preco': produto['preco'] * 1.10}
    # 4 - Caso contrário, copia o produto sem alterações
    if produto['preco'] > 50 else {**produto}
    # 5 - Percore cada produto da lista original
    for produto in lista_produtos
]

# Formatação de print para ficar mais legível ao usuário
for produto in nova_lista:
    print(
        f'nome: {produto['produto']} | '
        f'preço: {produto['preco']:.2f}'
    )

# --------------------------------------------------------------------------------------------

"""
🟡 Exercício 5 — Filtro + mapeamento juntos
Crie uma lista apenas com produtos acima de 30 reais e retorne apenas nome e preço.

Estrutura:
# 1. Criar nova lista
# 2. Percorrer produtos
# 3. Filtrar produtos com preço acima de 30
# 4. Mapear retornando apenas nome e preço
"""
# 1 - Lista original
lista_produtos = [
    {'produto': 'Caneca personalizada', 'preco': 24.90},
    {'produto': 'Fone de ouvido com fio', 'preco': 45.00},
    {'produto': 'Livro de bolso', 'preco': 27.50},
    {'produto': 'Power bank', 'preco': 89.90},
    {'produto': 'Kit lápis de cor', 'preco': 19.99},
]

# 2 - Nova lista utilizando list comprehension
nova_lista = [
    # 4 - Retorna apenas nome e preço
    {
        'produto': produto['produto'],
        'preco': produto['preco']
    }
    # 2 - Percorre os produtos na lista original
    for produto in lista_produtos
    # 3 - Filtra produtos com preço acima de 30
    if produto['preco'] > 30
]

# Formatação de print para ficar mais legível ao usuário
for produto in nova_lista:
    print(
        f'nome: {produto['produto']} | '
        f'preço: {produto['preco']:.2f}'
    )
  
# --------------------------------------------------------------------------------------------
  
"""
🟡 Exercício 6 — Lista de tuplas (número e quadrado)
Crie uma lista de tuplas contendo (número, número_ao_quadrado) de 1 a 10.

Estrutura:
# 1. Criar list comprehension
# 2. Percorrer números de 1 a 10
# 3. Criar tupla com número e seu quadrado
"""
# 1 - Criação da list comprehension
lista_de_tuplas = [
    # 3 - Cria tupla com número e seu quadrado
    (x, x * x)
    # 2 - Percorre números de 1 a 10
    for x in range(1, 11)    
]

print(*lista_de_tuplas, sep='\n')
  
# --------------------------------------------------------------------------------------------
  
"""
🟡 Exercício 7 — Dois for (coordenadas)
Crie uma lista de tuplas representando coordenadas (x, y) onde x e y vão de 0 a 2.

Estrutura:
# 1. Criar list comprehension
# 2. Criar primeiro for para x
# 3. Criar segundo for para y
# 4. Retornar tupla (x, y)
"""
# 1 - Criação da list comprehension
lista_tuplas = [
    # 2 - Gerando tupla com as coordenadas
    (x, y)
    # 3 - Primeiro for que irá percorrer os valores de x
    for x in range(3)
    # 4 - Segundo for que irá percorrer os valores de y
    for y in range(3)
]

print(*lista_tuplas, sep='\n')
  
# --------------------------------------------------------------------------------------------
  
"""
🟠 Exercício 8 — Produto com desconto
Aplique 20% de desconto apenas nos produtos acima de 100.

Estrutura:
# 1. Criar nova lista de produtos
# 2. Percorrer produtos
# 3. Usar if/else para aplicar desconto
# 4. Manter produtos sem alteração
"""
# 1 - Lista original
lista_produtos = [
    {'produto': 'Mouse gamer', 'preco': 85.00},
    {'produto': 'Jogo digital', 'preco': 69.90},
    {'produto': 'Livro capa dura', 'preco': 59.50},
    {'produto': 'Smartwatch', 'preco': 250.00},
    {'produto': 'Batedeira planetária', 'preco': 329.00},
]

# 2 - Lista nova com o desconto criada por list comprehension
lista_produtos_desconto = [
    # 3 - Se o preço for maior que 100, cria uma cópia do produto e aplica o desconto
    {**produto, 'preco': produto['preco'] * 0.80}
    # 4 - Se o preço for maior que 100, copia o produto e o valor com desconto
    if produto['preco'] > 100 else {**produto}
    # 5 - Percorre cada produto da lista original
    for produto in lista_produtos
]

print(*lista_produtos_desconto, sep='\n')
  
# --------------------------------------------------------------------------------------------
 
"""
🟠 Exercício 9 — Letras e índices (dois for)
Crie uma lista de tuplas com (índice, letra) para cada letra de uma palavra.

Estrutura:
# 1. Criar list comprehension
# 2. Percorrer índices da palavra
# 3. Percorrer letras da palavra
# 4. Retornar tupla com índice e letra
"""
# 1 - List comprehension usando enumerate
lista = [
    # 4 - Retorna tupla com índice e letra
    (indice, letra)
    # 2 e 3 - Percorre índice e letras da palavra
    for indice, letra in enumerate('Jaemin')
]

print(*lista, sep='\n')
  
# --------------------------------------------------------------------------------------------
 
"""
🔴 Exercício 10 — Desafio final (estrutura manda)
Dada uma lista de produtos:
- Filtrar produtos acima de 50
- Aplicar aumento de 10%
- Retornar apenas nome e novo preço

Estrutura:
# 1. Criar nova lista
# 2. Percorrer produtos
# 3. Filtrar produtos com preço acima de 50
# 4. Mapear aplicando aumento
# 5. Retornar apenas nome e preço
"""
# 1 - Lista original
lista_de_produtos = [
    {'produto': 'Caneta 3D', 'preco': 34.90},
    {'produto': 'Garrafa térmica', 'preco': 42.00},
    {'produto': 'Caixa de som', 'preco': 127.00},
    {'produto': 'Kit maquiagem', 'preco': 89.90},
    {'produto': 'Console portátil', 'preco': 299.00},
]

# 2 - Nova lista feita com list comprehension
nova_lista_com_aumento = [
    {
        'produto': produto['produto'],
        'preco': produto['preco'] * 1.10
    }
   # 2 - Percorre os produtos
   for produto in lista_de_produtos
   # 3 - Filtra produtos acima de 50
   if produto['preco'] > 50
]

print(*nova_lista_com_aumento, sep='\n')