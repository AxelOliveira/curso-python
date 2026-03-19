"""
Aula: reduce (redução de um iterável em um único valor)

O que é reduce?

Reduce = reduzir vários valores em UM único valor

Ex:
[10, 20, 30] -> 60

--------------------------------------------------

Como funciona?

reduce(função, iterável, valor_inicial)

- função -> recebe (acumulador, elemento)
- iterável -> lista, etc
- valor_inicial -> ponto de partida

--------------------------------------------------

Conceito chave: ACUMULADOR

O acumulador:
- guarda o resultado anterior
- vai sendo atualizado a cada passo

Ex:
0 + 10 -> 10
10 + 20 -> 30
30 + 30 -> 60

--------------------------------------------------

Importante:

- Não vem direto do Python -> precisa importar
- Está no módulo functools
"""

# 1 - Importando reduce
from functools import reduce

# 2 - Lista de produtos
produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

# ==============================
# 3. Usando reduce com lambda
# ==============================

# 4 - Soma todos os preços
total = reduce(
    lambda ac, p: ac + p['preco'],              # 5 - Acumulador + valor atual
    produtos,
    0                                           # 6 - Valor inicial
)

print('Total é', total)

# ==============================
# 7. Versão com função (didática)
# ==============================

def funcao_reduce(acumulador, produto):
    # 8 - Mostrando o que acontece internamente
    print('Acumulador:', acumulador)
    print('Produto:', produto)
    print()

    # 9 - Retorna o novo valor acumulado
    return acumulador + produto['preco']

total_debug = reduce(
    funcao_reduce,
    produtos,
    0
)

print('Total (debug):', total_debug)

# ==============================
# 10. Forma tradicional (for)
# ==============================

total_for = 0

for p in produtos:
    total_for += p['preco']

print('Total com for:', total_for)

# ==============================
# 11. Forma mais comum no Python
# ==============================

total_sum = sum(
    p['preco'] for p in produtos
)

print('Total com sum:', total_sum)