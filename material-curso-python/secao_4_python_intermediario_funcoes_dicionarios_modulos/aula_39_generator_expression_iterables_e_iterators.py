# Generator expression, Iterables e Iterators
# Generator é especifica do Python
# Generator são funções que sabem basicamente pausar em determinada ocasião
# Iterator é uma classe que tem que ter o método __iter__ e __next__ e geralmente trabalha com o iterables
# Iterator não é um generator
import sys

lista = [ n for n in range(1000000)]
generator = (n for n in range(1000000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(generator)