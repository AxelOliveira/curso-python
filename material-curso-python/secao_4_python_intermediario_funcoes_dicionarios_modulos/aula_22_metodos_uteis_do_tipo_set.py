"""
Métodos úteis do tipo set:

add()       -> adiciona UM único valor ao set
update()    -> adiciona VÁRIOS valores de um iterável
discard()   -> remove um valor específico (não gera erro se não existir)
clear()     -> remove todos os valores do set
"""

# Criando um set vazio
s1 = set()

# Adicionando valores com add()
# add adiciona apenas UM valor por vez
s1.add('Wonwoo')
s1.add(1)

print(s1)
print()

# Adiciona vários valores com update()
# update recebe um iterável (lista, tupla, string, etc)
s1.update(('Olá mundo', 1, 2, 3, 4))

print(s1)
print()

# Removendo valores com discard()
# discard remove o valor diretamente (não usa índice)
# Se o valor não existir, não gera erro
s1.discard('Olá mundo')
s1.discard('Wonwoo')

print(s1)
print()

# Limpando todo o set
s1.clear()
print(s1)