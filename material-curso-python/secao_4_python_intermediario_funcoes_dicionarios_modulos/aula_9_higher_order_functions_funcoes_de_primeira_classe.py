"""
Higher Order Functions (Funções de ordem superior)
Funções de primeira classe

Em Python, funções são objetos de primeira classe:
- Podem ser atribuídas a variáveis
- Podem ser passadas como argumentos
- Podem ser retornadas por outras funções

Funções são objetos de primeira classe: 
- Isso significa que elas podem ser tratadas como qualquer outro valor

Uma função é considerada higher order quando:
- Recebe outra função como argumento OU retorna uma função

Funções em Python podem ser usadas como dados:
- Podem ser passadas, armazenadas e executadas dinamicamente.
"""

# Função comum que recebe dois parâmetros e retorna uma string
def saudacao(msg, nome):
    return f'{msg}, {nome}!'

# Função de ordem superior (higher order function)
# Recebe uma função como parâmetro e executa essa função
def executa(funcao, *args):
    # Aqui a função só é executada quando usamos ()
    return funcao(*args)

# Passamos a função saudacao SEM executar (sem parênteses)
print(executa(saudacao, 'Bom dia', 'Luiz'))
print(executa(saudacao, 'Boa noite', 'Axel'))