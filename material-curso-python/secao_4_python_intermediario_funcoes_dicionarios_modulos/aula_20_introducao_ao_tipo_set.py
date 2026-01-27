"""
Sets - Conjuntos em Python (tipo set)

1) O que é um set
- Um set é uma estrutura de dados que armazena apenas VALORES
- Não possui chave nem valor associado (diferente do dict)
- Não garante ordem dos elementos
- Não permite valores duplicados

2) Origem do conceito
- Vem da matemática (conjuntos)
- Pode ser representado pelo diagrama de Venn

3) Regras importantes
- Sets em Python são MUTÁVEIS
- Porém, aceitam apenas valores IMUTÁVEIS

Tipos permitidos dentro de um set:
- str, int, float, bool, tuple

Tipos não permitidos:
- list, dict, set
"""

# Criando um set

# Forma 1 - Criando um set a partir de um iterável
# Duplicados são removidos e a ordem não é mantida
s1 = set('Wonwoo')
print(s1)

# Forma 2 - Criando um set vazio
# {} cria um dicionário vazio, por isso usamos set()
s2 = set()
print(s2)

# Forma 3 - Criando um set já com valores
s3 = {'Wonwoo', 1, 2, 3}
print(s3)