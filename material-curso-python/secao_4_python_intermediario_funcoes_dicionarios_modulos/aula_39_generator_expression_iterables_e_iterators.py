"""
Generator Expression, Iterables e Iterators

Generator expression é uma forma de criar generators usando uma sintaxe parecida com list comprehension

Generator:
- Cria valores sob demanda (um por vez)
- Consome menos memória
- Usa parênteses ()
- É um tipo de iterator

Diferença principal:

List comprehension -> cria todos os valores na memória
Generator expression -> cria valores somente quando necessário

Generators são muito úteis quando trabalhamos com grandes quantidades de dados, pois evitam gastar memória desnecessária
"""

import sys

# List comprehension (cria todos os valores)
lista = [ n for n in range(1000000)]

# Generator expression (cria sob demanda)
generator = (n for n in range(1000000))

# getsizeof mostra o tamanho ocupado na memória
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

# Generator não mostra os valores diretamente, ele apenas indica que é um objeto generator
print(generator)