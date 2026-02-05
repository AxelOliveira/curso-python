"""
isinstance() - verificar o tipo de um objeto

A função isinstance() é usada para saber se um valor pertence a um determinado tipo.

Estrutura:

isinstance(valor, tipo)

Também podemos verificar vários tipo ao mesmo tempo passando uma TUPLA:

isinstance(valor, (int, float))

Muito útil quando temos listas com vários tipos diferentes e precisamos tratar cada um de uma forma específica.
"""

# Lista com vários tipo de dados diferentes
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Wonwoo'},
]

for item in lista:

    # Verifica se é um SET
    if isinstance(item, set):
        print('SET')
        item.add(5)    # adiciona novo valor ao set
        print(item, isinstance(item, set))

    # Verifica se é STRING
    elif isinstance(item, str):
        print('STR')
        print(item.upper())   # transforma em maiúsculo

    # Verifica se é número (int ou float)
    elif isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 2)

    # Qualquer outro tipo cai aqui
    else:
        print('OUTRO')
        print(item)