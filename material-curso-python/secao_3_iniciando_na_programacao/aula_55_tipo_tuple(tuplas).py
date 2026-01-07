"""
Tipo tupla - Uma lista imutável
Tipo lista - Mutável
tupla é um pouco mais eficiente que a lista
se não for ter alteração na lista, pode-se utilizar a tupla
para criar uma tupla é só não utilizar os [] ou trocar eles por ()
se criar uma lista é possível mudar ela para tuple utilizando variavel = tuple()
"""
nomes = ['Maria', 'Helena', 'Luiz']
# nomes = tuple(nomes)
# nomes = list(nomes)
print(nomes[-1])
print(nomes)