"""
enumerate - enumera iteráveis (índices)
pega um iterável (lista, tupla,string) e transforma cada item um (índice, valor)
quando usar enumerate? Quando você precisa do índice e do valor ao mesmo tempo
se utilizar start=, o enumerate começa por aquele número (não é a mesma coisa que índice)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

for indice, nome in enumerate(lista):                   # indice recebe 0, nome recebe 'Maria' e depois indice recebe 1 e nome recebe 'Helena'
    print(indice, nome)

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)


# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')