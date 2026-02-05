# Generator expression, Iterables e Iterators
# O iterável tem a responsabilidade de ter os valores sequencialmente
# O iterator tem a responsabilidade de te entregar um valor por vez, ele só sabe entregar o proximo valor
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # Tem__inter__e__next__
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))