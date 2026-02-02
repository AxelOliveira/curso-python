# Importa o módulo pprint para exibir estruturas de dados de forma mais organizada e legível
import pprint

# Função auxiliar para imprimir dados formatados
# sort_dicts=False mantém a ordem original dos dicionários
# width controla a largura máxima antes da quebra de linha
def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

# Lista de produtos, onde cada item é um dicionário
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

# Exemplo simples de filtro com números
# Apenas número menores que 5 entram na nova lista
lista = [n for n in range(10) if n < 5]

# Criação de uma nova lista de produtos usando:
# - mapeamento (if ternário à esquerda do for)
# - filtro (if à direita do for)
novos_produtos = [
    # MAPEAMENTO:
    # Se o preço for maior que 20, cria uma cópia do produto com o preço aumentado em 5%
    {**produto, 'preco': produto['preco'] * 1.05}

    # ELSE de if ternário:
    # Caso o preço não seja maior que 20, apenas copia o produto sem alterações
    if produto['preco'] > 20 else {**produto}

    # FOR:
    # Percorre cada produto da lista original
    for produto in produtos

    # FILTRO:
    # O produto só entra na lista final se:
    # - o preço for maior ou igual a 20
    # - e o preço com aumento for maior que 10
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
]

# Exibe os produtos formatados usando pprint
p(novos_produtos)