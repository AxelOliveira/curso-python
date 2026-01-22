"""
Shallow copy vs dados mutáveis em Python

Shallow copy (cópia rasa):
- Cria um novo dicionário
- MAS mantém a referência interna para objetos mutáveis (como listas e outros dicionários)

Ou seja:
- Tipos IMUTÁVEIS: o valor é copiado
- Tipos MUTÁVEIS: o valor é compartilhado
"""
d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

# Criando uma cópia rasa do dicionário
d2 = d1.copy()

# Alterando um valor IMUTÁVEL (não afeta o original)
d2['c1'] = 1000

# Alterando um valor MUTÁVEL (AFETA o original)
d2['l1'][1] = 999999

print(d1)
print(d2)