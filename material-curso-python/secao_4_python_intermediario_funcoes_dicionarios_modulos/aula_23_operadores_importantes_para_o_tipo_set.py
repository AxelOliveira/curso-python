"""
Operadores importantes para o tipo set (conjuntos)

Esses operadores vêm da matemática e funcionam apenas com sets.

|      -> União (union): Une todos os elementos dos dois sets (sem duplicar)

&      -> Interseção (intersection): Retorna apenas os elementos presentes em AMBOS os sets

-      -> Diferença: Retorna os elementos que estão APENAS no set da esquerda

^      -> Diferença simétrica(symmetric_difference): Retorna os elementos que NÃO estão em ambos
"""

# Criando os sets
s1 = {1, 2, 3}
s2 = {2, 3, 4}

# União
# Todos os valores únicos dos dois sets
s3 = s1 | s2
print('União:', s3)

print()

# Interseção
# Valores que existem nos dois sets
s4 = s1 & s2
print('Interseção:', s4)

print()

# Diferença
# Valores que existem apenas no set da esquerda
s5 = s1 - s2
print('Diferença (s1 - s2):', s5)

print()

# Diferença simétrica
# Valores que não estão presentes nos dois ao mesmo tempo
s6 = s1 ^ s2
print('Diferença simétrica:', s6)
