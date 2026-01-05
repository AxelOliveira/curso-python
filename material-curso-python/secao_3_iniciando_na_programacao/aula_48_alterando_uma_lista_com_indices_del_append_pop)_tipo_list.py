"""
Listas em Python
Tipo list - mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i]   (CRUD)
.append = adiciona ao final da lista
.pop = remove o ultimo item da lista
.del = remove um indice informado
É possível colocar uma lista dentro de outra lista
A lista vem antes do print, pois ela é uma váriavel
Depois de um del ou pop, os índices mudam.

"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, 'Removido, ', ultimo_valor)