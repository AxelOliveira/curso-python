"""
itertools.combinations, permutations e product

Essas funções vêm do módulo itertools e servem para gerar combinações de dados automaticamente - algo que seria MUITO trabalhoso fazer manualmente.

1. combinations (combinações)
- Ordem NÃO importa
- Não repete pares invertidos

Ex:
('João', 'Joana') aparece
('Joana', 'João') NÃO aparece

Use quando:
- A ordem não faz diferença
- Quer grupos únicos

--------------------------------------------------

2. permutations (permutações)
- Ordem IMPORTA
- Gera todas as variações possíveis

Ex:
('João', 'Joana')
('Joana', 'João') 

Use quando:
- A ordem muda o resultado
- Quer todas as possibilidades

--------------------------------------------------

3. product (produto cartesiano)
- Ordem IMPORTA
- Combina TODOS os valores entre listas
- Pode repetir elementos

Use quando:
- Quer gerar todas as combinações possíveis entre múltiplos grupos

Ex:
cor + tamanho + tipo + material

Muito importante:
O número de combinações cresce MUITO rápido (crescimento exponencial)

--------------------------------------------------

Todos retornam ITERATORS
Ou seja:
- Precisam ser percorridos com for
- Ou convertidos para lista (list)
"""

# 1 - Importando as funções do itertools
from itertools import combinations, permutations, product

# 2 - Função auxiliar para imprimir iteradores
def print_inter(iterator):
    # 3 - Converte o iterator em lista e imprime cada item em uma linha
    print(*list(iterator), sep='\n')
    print()

# 4 - Lista de pessoas
pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]

# ==============================
# COMBINATIONS (ordem NÃO importa)
# ==============================

# 5 - Criando combinações de 2 em 2
print('COMBINATIONS:')
print_inter(combinations(pessoas, 2))

# ==============================
# PERMUTATIONS (ordem IMPORTA)
# ==============================

# 6 - Criando permutações de 2 em 2
print('PERMUTATIONS:')
print_inter(permutations(pessoas, 2))

# ==============================
# PRODUCT (produto cartesiano)
# ==============================

# 7 - Lista de características de camisetas
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    [ 'algodão', 'poliéster']
]

# 8 - Gerando todas as combinações possíveis
# *camisetas -> desempacota a lista
print('PRODUCT:')
print_inter(product(*camisetas))