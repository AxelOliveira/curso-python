"""
map, partial, GeneratorType e esgotamento de iterators

1. map (mapeamento de dados)

Mapear = pegar um dado e transformar em outro

Ex:
[1, 2, 3] -> [2, 4, 6]

O map:
- Recebe uma função
- Recebe um iterável
- Aplica a função em cada elemento

Retorna um ITERATOR (não uma lista)

--------------------------------------------------

2. partial (functools)

Permite criar uma nova função com argumentos já definidos

Ex:
função(valor, porcentagem)

-> criar uma nova função:
função_10_porcento(valor)

--------------------------------------------------

3. GeneratorType

Serve para verificar se algo é um generator

Todo generator é um iterator
Nem todo iterator é generator

--------------------------------------------------

4. Esgotamento de iterators

Iterators:
- Só podem ser usados UMA VEZ
- Depois que percorre, ficam vazios

Ex:
list(iterator) -> consome tudo

Se usar de novo -> vazio

--------------------------------------------------

Quando usar map?
- Transformar listas
- Substituir for simples
- Código mais funcional
"""

# 1 - Importações
from functools import partial
from types import GeneratorType

# 2 - Função auxiliar para imprimir iterators
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

# 3 - Lista de produtos
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# 4 - Função para aumentar porcentagem
def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

# 5 - Criando uma nova função com partial (10%)
aumentar_dez_porcento = partial(
    aumentar_porcentagem,
    porcentagem=1.1
)

# 6 - Função que altera o preço do produto
def muda_preco_de_produtos(produto):
    return {
        **produto,  # 7 - copia do dicionário
        'preco': aumentar_dez_porcento(produto['preco'])  # 8 - altera preço
    }

# 9 - Usando map para aplicar a função em todos os produtos
novos_produtos = map(
    muda_preco_de_produtos,
    produtos
)

# 10 - Convertendo para lista (evita esgotamento posterior)
novos_produtos = list(novos_produtos)

# 11 - Mostrando resultados
print('Produtos originais:')
print_iter(produtos)

print('Produtos com aumento:')
print_iter(novos_produtos)

# ==============================
# 12. Exemplo simples com lambda
# ==============================

resultado = list(map(
    lambda x: x * 3,        # 13 - função
    [1, 2, 3, 4]            # 14 - iterável
))

print('Multiplicando por 3:')
print(resultado)

# ==============================
# 15. Verificando generator
# ==============================

generator = (x for x in range(5))

print('É generator?', isinstance(generator, GeneratorType))

# ==============================
# 16. Exemplo de esgotamento
# ==============================

iterator = map(lambda x: x * 2, [1, 2, 3])

print(list(iterator))   # primeira vez -> funciona
print(list(iterator))   # segunda vez -> vazio