"""
Yiled from em Generator Functions

O que é yield from?
- Permite que um generator use outro generator internamente.
- Em vez de criar um for manual, o yield from delega a execução.
- Ele repassa TODOS os valor do generator interno automaticamente.

Sem yield from:
    for valor in outro_gen:
        yield valor

Com yield from:
    yield from outro_gen

Fluxo mental:
1) Generator principal começa
2) Se existir outro generator -> ele executa primeiro
3) Quando o interno termina -> o principal continua
"""

# 1 - Primeiro generator
def gen1():
    # 2 - Primeiro valor
    yield 1

    # 3 - Agora o print aparece após o primeiro valor
    print('COMECOU GEN1')

    yield 2
    yield 3

    # 4 - Finalização
    print('ACABOU GEN1')


# 5 - Generator principal
def gen2(gen=None):
    # 6 - Primeiro valor do gen2
    yield 4

    # 7 - Print vem depois do primeiro yield
    print('COMECOU GEN2')

    # 8 - Executa generator interno
    if gen is not None:
        yield from gen

    yield 5
    yield 6

    # 9 - Finalização
    print('ACABOU GEN2')


# 10 - Criação dos generators
g1 = gen2(gen1())
g3 = gen2()

# 11 - Execução
for numero in g1:
    print(numero)

print()

for numero in g3:
    print(numero)