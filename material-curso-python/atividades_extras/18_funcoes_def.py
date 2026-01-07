"""
🧩 Exercício 1
Crie uma função chamada saudacao que:
- não recebe parâmetros
- imprime "Olá, mundo!"
"""
def saudacao():
    print('Olá, mundo!')

saudacao()
    
#--------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 2
Crie uma função chamada mostrar_nome que:
- recebe um nome como parâmetro
- imprime o nome recebido
"""
def mostrar_nome(nome):
    print(nome)

nome = input('Insira seu nome: ')
mostrar_nome(nome)
    
#--------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 3
Crie uma função chamada soma que:
- recebe dois números
- retorna a soma deles
"""
def soma(a, b):
    return a + b

numero_1 = float(input('Insira o primeiro número: '))
numero_2 = float(input('Insira o segundo valor: '))

resultado = soma(numero_1, numero_2)
print('A soma dos dois valores é:', resultado)
    
#--------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 4
Crie uma função chamada maior_numero que:
- recebe dois números
- retorna o maior deles
"""
def maior_numero(a, b):
    if a > b:
        return a
    else:
        return b
"""
🧩 Exercício 5
Crie uma função chamada par_ou_impar que:
- recebe um número
- retorna "par" ou "ímpar"
"""
def par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"