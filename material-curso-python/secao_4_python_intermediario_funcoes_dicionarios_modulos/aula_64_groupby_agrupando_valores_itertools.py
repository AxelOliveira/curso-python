"""
itertools.groupby (agrupando valores)

O groupby serve para AGRUPAR elementos com base em uma chave.

Ideia principal:
Agrupar dados que têm algo em comum.

Ex:
Agrupar alunos pela nota:
A -> alunos com nota A
B -> alunos com nota B

--------------------------------------------------

IMPORTANTE (isso é o que mais cai):
Os dados PRECISAM estar ORDENADOS antes do groupby

Se não ordenar:
- O mesmo grupo pode aparecer várias vezes
- Resultado fica incorreto

Sempre use sorted(..., key=...) antes

--------------------------------------------------

Como funciona o groupby:
Ele retorna pares:
(chave, grupo)

- chave -> valor usado para agrupar
- grupo -> iterador com os itens daquele grupo

--------------------------------------------------

groupby retorna ITERATORS:
- Você precisa percorrer com for
- Ou converter com list()

--------------------------------------------------

Quando usar?
- Agrupar dados (relatórios, logs, notas, categorias)
- Muito comum em back-end e análise de dados
"""
# 1 - Importando groupby
from itertools import groupby

# 2 - Lista de alunos com notas
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

# 3 - Função para definir a chave (nota)
def ordena(aluno):
    return aluno['nota']

# 4 - Ordenando os dados (PASSO OBRIGATÓRIO)
alunos_agrupados = sorted(alunos, key=ordena)

# 5 - Agrupando os alunos pela nota
grupos = groupby(alunos_agrupados, key=ordena)

# 6 - Percorrendo os grupos
for chave, grupo in grupos:
    # 7 - chave = nota (A, B, C...)
    print(f'Nota: {chave}')

    # 8 - grupo = iterador com os alunos daquela nota
    for aluno in grupo:
        print(aluno)

    print()