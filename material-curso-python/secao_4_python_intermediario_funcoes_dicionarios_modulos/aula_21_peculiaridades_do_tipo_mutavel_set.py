"""
Sets - Peculiaridades importantes

1) O que caracteriza um set
- Armazena apenas valores ÚNICOS
- Remove automaticamente valores duplicados
- Não possui índices (não existe posição)
- Não garante ordem
- É iterável (for, in, not in)
- Não aceita valores mutáveis

Tipos NÃO permitidos dentro de um set:
- list, dict, set
"""
# Removendo valores duplicados de um iterável
l1 = [1, 2, 3, 3, 3, 3, 3, 1]
print('Lista original:', l1)

# Convertendo a lista em set (remove duplicados)
s1 = set(l1)
print('Set:', s1)

# Convertendo o set de volta para lista
l2 = list(s1)
print('Lista sem duplicados:', l2)

print()

# Testando pertencimento (in / not in)

s1 = {1, 2, 3}
print(3 not in s1)   # False
print(4 not in s1)   # True

print()

# Percorrendo um set

for numero in s1:
    print(numero)