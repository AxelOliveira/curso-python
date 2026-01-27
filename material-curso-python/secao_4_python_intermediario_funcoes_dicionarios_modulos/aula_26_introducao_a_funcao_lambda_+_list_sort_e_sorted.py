"""
FUNÇÃO LAMBDA
- É uma função anônima (não tem nome)
- Possui apenas UMA expressão
- Retorna o resultado automaticamente (não usa return)
- Muito usada como argumento de outras funções (key, map, filter, etc.)

SORT vs SORTED
list.sort() -> modifica a lista original (in-place)
sorted()    -> cria uma NOVA lista (cópia rasa = uma nova lista, mas o elementos internos(dicionários, listas) continuam sendo os mesmos objetos.)
"""
lista = [
    {'nome': 'Vernon', 'sobrenome': 'miranda'},
    {'nome': 'Wonwoo', 'sobrenome': 'Oliveira'},
    {'nome': 'San', 'sobrenome': 'Silva'},
    {'nome': 'Eric', 'sobrenome': 'Moreira'},
    {'nome': 'Mingyu', 'sobrenome': 'Souza'},
]

def exibir(lista):
    #Percorre todos os elementos da lista recebida
    for item in lista:
        # Exibe cada dicionário individualmente
        print(item)
    # Linha em branco apenas para organização visual    
    print()

# Percorre toda a lista, para cada item a função lambda é executada e retorna o valor de item [nome]
l1 = sorted(lista, key=lambda item: item['nome'])

# Percorre toda a lista, para cada item a função lambda é executada e retorna o valor de item [sobrenome]
l2 = sorted(lista, key=lambda item: item['sobrenome'])

# Lista ordenada pelo nome
exibir(l1)

# Lista ordenada pelo sobrenome
exibir(l2)