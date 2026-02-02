# É possível utilizar vários for aninhados dentro de um list comprehension, seguindo a mesma lógica dos loops for tradicionais

# Lista vazia criada para o exemplo com for tradicional
lista = []

# Primeiro laço for (externo)
for x in range(3):
    # Segundo laço for (interno)
    for y in range(3):
        # Adiciona uma tupla (x, y) à lista
        # A tupla é usada porque uma lista só aceita UM objeto por posição
        lista.append((x, y))

# Reescrita do mesmo código acima usando list comprehension        
lista = [
    # Cada elemento da lista será uma tupla (x, y)
    (x, y)
    # Primeiro for (externo)
    for x in range(3)
    # Segundo for (interno)
    for y in range(3)
]

# List comprehension com múltiplos for e um iterável de texto
lista = [
    # Para cada x, será criada uma lista interna
    # Cada elemento da lista interna será uma tupla (x, letra)
    # Percorre cada caractere da strin 'Wonwoo'
    [(x, letra) for letra in 'Wonwoo']
    # Percorre os valores de x
    for x in range(3)
]

# Exibe a lista final no terminal
print(lista)