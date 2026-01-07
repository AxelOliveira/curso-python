"""
Exercício
Exiba os índices da lista
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('Axel')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
