"""
Lista de listas e seus índices
Lista de listas:
Cada lista interna representa um grupo.
Para acessar um valor:
1º índice -> escolhe a lista interna
2º índice -> escolhe o valor dentro dessa lista
Primeiro escolhemos a lista,
depois escolhemos o valor dentro dela.
"""
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

# print(salas[1][0])                  # Pegue o índice 1 da lista salas e depois pegue o índice 0 da lista que está dentro dela
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][3])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)