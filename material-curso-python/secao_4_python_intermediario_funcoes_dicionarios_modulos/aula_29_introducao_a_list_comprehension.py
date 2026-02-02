"""
Introdução à List comprehension em Python

List comprehension é uma forma mais curta e expressiva de criar listas a partir de iteráveis (como range, listas, strings, etc.)
"""
# 1 - Cria uma lista vazia que será preenchida manualmente
lista = []

# 2 - Laço for que percorre os números de 0 até 9
for numero in range(10):
    # 3 - A cada iteração, adiciona o valor atual de numero à lista
    lista.append(numero)

# --------------------------------------------------------------------------------------

# Reatribui a veriável lista usando list comprehension
# Aqui estamos criando uma nova lista do zero
lista = [
    # Expressão: define o valor que será colocado na lista
    numero * 2
    # Laço: para cada numero gerado pelo range de 0 até 9
    for numero in range(10)
]

# Exibe a lista final no terminal
print(lista)