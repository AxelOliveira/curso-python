# isinstance - para saber se objeto é de determinado tipo
# No python eu posso checar se alguma coisa é de determinado tipo, usando isinstance(valor, str)
# Consigo passar uma tupla no is instance(valor, (in, float))
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Wonwoo'},
]

for item in lista:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print('STR')
        print(item.upper())

    elif isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 2)

    else:
        print('OUTRO')
        print(item)