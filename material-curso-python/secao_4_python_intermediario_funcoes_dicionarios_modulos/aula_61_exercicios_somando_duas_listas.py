"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.

Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

# ============================================================
# 1) Criar listas de exemplo
# ============================================================

# 1 - Lista A (maior)
lista_a = [1, 2, 3, 4, 5, 6, 7]

# 2 - Lista B (menor)
lista_b = [1, 2, 3, 4]

# ============================================================
# 2) Somar valores das listas
# ============================================================

# 3 - zip junta os elementos das duas listas
#     formando pares (tuplas)
#     Exemplo:
#     (1,1), (2,2), (3,3), (4,4)

# 4 - Para cada par (x, y), somamos os valores
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]

# ============================================================
# 3) Mostrar resultado
# ============================================================

# 5 - Exibir nova lista com valores somados
print(lista_soma)