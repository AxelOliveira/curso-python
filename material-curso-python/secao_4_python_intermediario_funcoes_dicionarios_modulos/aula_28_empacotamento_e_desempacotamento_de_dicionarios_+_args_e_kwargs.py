"""
EMPACOTAMENTO E DESEMPACOTAMENTO DE DICIONÁRIOS

Empacotamento:
- Reunir vários valores em uma única variável

Desempacotamento:
- Extrair valores de uma estrutura e passá-los separadamente

*args:
- Empacota argumentos NÃO nomeados em uma tupla

**kwargs:
- Empacota argumentos NOMEADOS em um dicionário

** (em dicionários):
- Usado para desempacotar dicionários
- Para extrair um dicionário dentro de outro, usa-se **
"""
# ======================================================
# DESEMPACOTAMENTO SIMPLES DE VALORES
# ======================================================
a, b = 1, 2
a, b = b, a      # troca de valores por desempacotamento

# print(a, b)

# ======================================================
# DESEMPACOTAMENTO DE DICIONÁRIOS
# ======================================================

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

# Une os dois dicionários em um novo
# Caso existam chaves iguais, a última prevalece
pessoa_completa = {**pessoa, **dados_pessoa}

# print(pessoas_completa)

# ======================================================
# ITERAÇÃO COM DESEMPACOTAMENTO
# ======================================================

# for chave, valor in pessoa.items():
#       print(chave, valore)


# ======================================================
# *args e **kwargs EM FUNÇÕES
# ======================================================

def mostra_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

# ======================================================
# CHAMADAS DA FUNÇÃO
# ======================================================

# mostra_argumentos_nomeados(nome='Joana', qlq=123)

# Passando um dicionário como argumentos nomeados
# O ** desempacota o dicionário
configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostra_argumentos_nomeados(**configuracoes)