# Mapeamento de dados consiste em transformar cada elemento de uma lista em um novo elemento, mantendo a relação 1 para 1

# Lista original de produtos
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

# Criação de uma nova lista de produtos usando list comprehension
novos_produtos = [
    # Cria um novo dicionário copiando todas as chaves do produto original e sobrescrevendo o preço com um aumento de 5%
    {**produto, 'preco': produto['preco'] * 1.05}

    # Condição do if ternário:
    # Esse bloco só será aplicado se o preço for maior que 20
    if produto['preco'] > 20
    
    # Caso o preço não seja maior que 20, apenas copia o dicionário original sem alterações
    else {**produto}

    # Laço que percorre cada produto da lista original
    for produto in produtos
]

# Imprime cada produto em uma linha separada
# O operador * desempacota a lista
# O sep define o separador entro os prints
print(*novos_produtos, sep='\n')