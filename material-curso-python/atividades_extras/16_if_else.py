"""
🧩 Exercício 1
Crie uma variável idade.
Use if / else para:
- imprimir "Maior de idade" se idade for maior ou igual a 18
- imprimir "Menor de idade" caso contrário
"""
idade = 12

if idade >= 18:
    print('Maior de idade')
else:
    print('Mneor de idade')
    
#--------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 2
Crie uma variável numero.
Use if / else para verificar:
- se o número é positivo
- ou negativo
"""
numero = -6

if numero >= 0:
    print('número positivo')
else:
    print('número negativo')
    
#--------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 3
Crie duas variáveis a e b.
Use if / else para:
- imprimir qual é o maior número
- ou informar que são iguais
"""
a = 5
b = 5

if a > b:
    print(f'número', a, 'é maior que o número', b)
elif a == b:
    print('os valores são iguais')
else:
    print(f'número', b, 'é maior que o número', a)
    
#--------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 4
Crie uma variável nota.
Use if / else para:
- aprovar se a nota for maior ou igual a 7
- reprovar caso contrário
"""
nota = 7

if nota >= 7:
    print('Aprovado')
else:
    print('Reprovado')
    
#--------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 5
Crie uma variável senha.
Use if / else para:
- permitir acesso se a senha for "1234"
- negar acesso caso contrário
"""
senha = "1234"

if senha == "1234":
    print('Acesso permitido')
else:
    print('Acesso negado')