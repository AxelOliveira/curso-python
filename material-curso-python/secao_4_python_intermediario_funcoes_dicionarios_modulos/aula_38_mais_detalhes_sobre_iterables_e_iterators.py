"""
Iterables e Iterators em Python

Iterable:
- É um objeto que possui vários valores sequenciais
- Pode ser percorrido com for
- Possui o método __iter__()
Ex: list, tuple, string, dict, set, range...

Iterator:
- É o objeto que entrega os valores um por vez
- Possui __iter__() e __next__()
- Guarda o estado atual da iteração

Resumo:
Iterable -> contém os dados
Iterator -> entrega o próximo valor

Usamos:
iter(objeto) -> transforma um iterable em iterator
next(iterator) -> pega o próximo valor
"""

# Iterable (possui vários valores)
iterable = ['Eu', 'Tenho', '__iter__']

# Criando um iterator a partir do iterable
iterator = iter(iterable) # Tem__inter__e__next__

# next() pega sempre o próximo valor disponível
print(next(iterator))
print(next(iterator))
print(next(iterator))

# Aqui vai gerar erro (StopIteration), pois não existem mais valores para entregar
print(next(iterator))