"""
Operação ternária (condicional de uma linha)
Faz o if e else em uma linha só
<valor> if <condicao> else <outro valor>

Usada quando:
- a decisão é simples
- o código fica mais legível
Não usar quando a lógica for complexa
"""
# condicao = 10 == 11
# variavel = 'Valor' if condicao else 'Outro valor'
# print(variavel)

"""Dois ultimos digitos do cpf"""
digito = 9         
novo_digito = digito if digito <= 9 else 0       # Se o digito for maior que 9 ele vira 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)

# ---------------------------------------------------------------------------------------------------------------------------

# 1 - Criação da variável
numero = 25

# 2 - Verificação se o número é par ou impar
resultado = 'par' if numero % 2 == 0 else 'ímpar'

# 3 - Impressão do valor
print(resultado)

# ---------------------------------------------------------------------------------------------------------------------------

# 1 - Importar o modulo random
import random

# 2 - Gera um número aletório entre 1 e 100
numero = random.randint(0, 100)

# 3 - Classifica usando ternário encadeado
resultado = (
    'menor que 50' if numero < 50
    else 'igual a 50' if numero == 50
    else 'maior que 50'
)

print(f'Número gerado: {numero}')
print(f'Resultado: {resultado}')