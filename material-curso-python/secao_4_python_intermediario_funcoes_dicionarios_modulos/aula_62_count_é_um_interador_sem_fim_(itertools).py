"""
itertools.count (contador infinito)

O count é uma função do módulo itertools que cria um contador infinito.

O que isso significa?
- Ele nunca para sozinho (não tem fim)
- Ele gera números continuamente
- Muito parecido com o range, mas sem limite final

Diferença entre count e range:
- range -> tem início, fim e passo (step)
- count -> tem início e passo, mas NÃO tem fim

Importante:
- count é um ITERADOR
- range é apenas ITERÁVEL (não é iterador)

Iterável:
Objeto que pode ser percorrido (tem __iter__)

Iterador:
Objeto que:
1. Pode ser percorrido
2. Tem __next__ (gera o próximo valor)

Como o coun funciona:
- Ele começa em um valor (start)
- A cada next(), ele:
  1. retorna o valor atual
  2. soma o step
  3. guarda o novo valor

Cuidado:
Como ele é infinito, pode causa loop infinito se não usar break.

Quando usar?
- Quando você NÃO sabe o limite final
- Quando precisa gerar valores continuamente
"""

# 1 - Importando o count do módulo itertools
from itertools import count

# 2 - Criando um contador infinito:
# start=8 -> começa em 8
# step=8 -> soma 8 a cada iteração
c1 = count(step=8, start=8)

# 3 - Criando um range para comparação (tem fim)
r1 = range(8, 100, 8)

# 4 - Verificando se são iteráveis (possuem __inter__)
print('c1', hasattr(c1, '__iter__'))
print('r1', hasattr(r1, '__iter__'))

# 5 - Verificando se são iteradores (possuem __next__)
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__next__'))

print()

# 6 - Usando o count (ITERADOR INFINITO)
print('count')
for i in c1:
    # 7 - IMPORTANTE: condição de parada para não travar o programa
    if i >= 100:
        break

    # 8 - Exibindo os valores
    print(i)

print()

# 9 - Usando o range (tem fim definido)
print('range')
for i in r1:
    # 10 - Aqui não precisa de break, pois o range já tem limite
    print(i)