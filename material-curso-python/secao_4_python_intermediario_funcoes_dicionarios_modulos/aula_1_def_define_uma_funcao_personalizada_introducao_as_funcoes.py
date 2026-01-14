"""
Introdução às funções (def) em Python
- Funções são uma forma de dar um nome para um pedaço de código que você quer usar mais de uma vez.
- Em vez de escrever o mesmo código várias vezes, você guarda esse código dentro de uma função e chama quando precisar
- Uma função só executa quando é chamada pelo nome.
- Funções podem receber informações de fora.
- Essas informações entram pelos parâmetros, que funcionam como variáveis temporárias dentro de uma função.
- Quando você chama a função, você passa os argumentos, que são os valores que vão preencher esses parâmetros.
- Toda vez que a função é chamada, os valores podem ser diferentes.

- Criar uma função é diferente de executar uma função:
    def saudacao(nome):
        print(f'Olá, {nome}!')
    No codigo acima, você está falando: Python, quando eu pedir saudacao, faça isso.
    saudacao('Maria')
    Agora sim a função será executada

Parâmetro X Argumento
Parâmetro -> nome da variável
Argumento -> valor passado

def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')

def = palavra reservada que significa: "Vou definir uma função"
Não usa letra maiúscula no início
Sem espaço
Nome que faça sentido

(nome='Sem nome')
nome -> parâmetro
'Sem nome' -> valor padrão
Se ninguém passar um nome, o Python usa 'Sem nome'

PARÂMETRO X ARGUMENTO
def imprimir(a, b, c):
    print(a, b, c)      -> parâmetros (são caixas vazias)
imprimir(1, 2, 3)       -> argumentos (são os valores colocados nas caixinhas)
"""

# def Print(a, b, c):
#     print('Várias1')
#     print('Várias2')
#     print('Várias3')
#     print('Várias4')

# def imprimir(a, b, c):
#     print(a, b, c)
# imprimir(1, 2, 3)
# imprimir(4, 5, 6)

def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')

saudacao('Luiz Otávio')
saudacao('Maria')
saudacao('Helena')