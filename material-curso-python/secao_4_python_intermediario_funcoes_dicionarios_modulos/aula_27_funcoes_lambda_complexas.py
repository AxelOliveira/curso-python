"""
FUNÇÕES LAMBDA MAIS COMPLEXAS

Funções em Python são objetos de primeira classe:
- Podem ser armazenadas em variáveis
- Podem ser passadas como argumento
- Podem ser retornadas por outras funções

Função de alta ordem:
- Função que recebe outra função como parâmetro
- Função que retorna outra função

Closure:
- Função que "lembra" o valor do escopo onde foi criada

Lambda:
- Função anônima
- Possui apenas uma expressão
- Retorna o valor automaticamente
"""


def executa(funcao, * args):
    # Executa a função recebida passando os argumentos informados
    return funcao(*args)

# ======================================================
# LAMBDA RETORNANDO OUTRA FUNÇÃO (CLOSURE)
# ======================================================

# A lambda externa recebe um valor (m)
# e retorna outra função que multiplica n por m
duplica = executa(
    lambda m: lambda n: n * m,
    2
)

print(duplica(2))

print()


# ======================================================
# LAMBDA COM DOIS PARÂMETROS
# ======================================================
soma = executa(
    lambda x, y: x + y,
    2, 3
)

print('Soma:', soma)

print()

# ======================================================
# LAMBDA COM QUANTIDADE VARIÁVEL DE ARGUMENTOS
# ======================================================
soma_varios = executa(
    lambda *args: sum(args),
    1, 2, 3, 4, 5, 6, 7
)

print('Soma de vários:', soma_varios)