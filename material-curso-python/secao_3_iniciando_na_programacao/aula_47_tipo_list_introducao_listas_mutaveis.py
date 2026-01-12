"""
Listas em Python
Tipo list - mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
É possível colocar uma lista dentro de outra lista
A lista vem antes do print, pois ela é uma váriavel
Em listas, você muda o conteúdo, não cria outra lista.
Lista vazia também é lista, ela é:
 falsa em contexto booleano
 mas ainda é um objeto válido
sum() soma todos os números de uma lista automaticamente.
"""
#        +01234
#        -54321
string = 'ABCDE'   # 5 caracteres (len)
# print(bool([]))    # falsy
# print(lista, type(lista))

#        0     1         2         3     4
#        -5    -4       -3        -2    -1
lista = [123, True, 'Luiz Otávio', 1.2, []]
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))