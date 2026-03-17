"""
filter (filtro funcional)

O que é filter?

Filter = filtrar dados com base em uma condição

Ele percorre um iterável e:
- mantém os valores que retornam True
- remove os valores que retornam False

--------------------------------------------------

Como funciona?

filter(função, iterável)

- função -> retorna True ou False
- iterável -> lista, tuple, etc

--------------------------------------------------

Diferença entre map e filter:

map -> TRANSFORMA os dados
filter -> FILTRA os dados

--------------------------------------------------

Importante:

- Retorna um ITERATOR (não lista)
- Pode ter:
    - mesmo tamanho
    - menor tamanho
    - até vazio
    
--------------------------------------------------

Quando usar?

- Filtrar dados
- Buscar elementos específicos
- Limpar listas
"""

# 1 - Função auxiliar para imprimir iterators
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

# 2 - Lista de produtos
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# ==============================
# 3. Função de filtro
# ==============================


def filtrar_preco(produto):
    # 4 - Retorna True apenas para produtos > 100
    return produto['preco'] > 100

# 5 - Aplicando filter
novos_produtos = filter(
    filtrar_preco,
    produtos
)

# 6 - Mostrando resultados
print('Produtos originais:')
print_iter(produtos)

print('Produtos filtrados (> 100):')
print_iter(novos_produtos)


# ==============================
# 7. Exemplo com lambda
# ==============================

novos_produtos_lambda = list(filter(
    lambda p: p['preco'] > 50,          # 8 - Condição
    produtos
))

print('Produtos > 50 (lambda):')
print(novos_produtos_lambda)

# ==============================
# 9. Comparação com list comprehension
# ==============================

novos_produtos_lc = [
    p for p in produtos
    if p['preco'] > 50                # 10 - condição
]

print('Produtos > 50 (list comprehension):')
print(novos_produtos_lc)

# ==============================
# 11. Exemplo de lista vazia
# ==============================

sem_resultado = list(filter(
    lambda p: p['preco'] > 1000,
    produtos
))

print('Sem resultado:')
print(sem_resultado)