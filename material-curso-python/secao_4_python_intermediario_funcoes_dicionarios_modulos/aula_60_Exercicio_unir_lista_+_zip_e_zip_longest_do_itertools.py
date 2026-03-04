"""
Exercício: Unir listas + zip e zip_longest (itertools)

1) zip():
    - Une iteráveis posição por posição.
    - Para quando o menor iterável acabar.

2) zip_longest():
    - Continua até o maior iterável acabar
    - Preenche valores faltantes com fillvalue

3) Pensamento computacional:
    - Identificar o menor tamanho
    - Controlar limite do laço
    - Criar nova estrutura com base em duas listas

4) itertools:
    - Biblioteca padrão do Python para trabalhar com iteradores.
"""

# ============================================================
# 1) Criar função manual (pensamento computacional puro)
# ============================================================

# 1 - Criar função que recebe duas listas
def zipper(l1, l2):

    # 2 - Decobrir o menor tamanho entre as listas
    intervalo = min(len(l1), len(l2))

    # 3 - Criar nova lista unindo elementos pela posição
    return [(l1[i], l2[i]) for i in range(intervalo)]

# ============================================================
# 2) Importar ferramenta pronta do Python
# ============================================================

# 4 - Importar zip_longest do itertools
from itertools import zip_longest

# ============================================================
# 3) Criar listas de exemplo
# ============================================================

# 5 - Lista de cidades
l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']

# 6 - Lista de estados
l2 = ['BA', 'SP', 'MG', 'RJ']

# ============================================================
# 4) Executar comparações
# ============================================================

# 7 - Usando função criada manualmente
print(zipper(l1, l2))

# 8 - Usando zip (para no menor)
print(list(zip(l1, l2)))

# 9 - Usando zip_longest (vai até o maior)
print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE')))