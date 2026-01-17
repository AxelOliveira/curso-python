"""
Exercícios com funções

Crie uma função que multiplica todos os argumentos não nomeados recebidos
Retorne o total para uma variável e mostre o valor da variável.
"""
# *args recebe todos os valores como uma tupla
def multiplicar(*args):
    # Começa com 1 porque 1 é o valor dentro da multiplicação
    total = 1

    # Percorre todos os números recebidos
    for numero in args:
        total *= numero

    # Retorna o valor final da multiplicação    
    return total

# Armazena o retorno da função em uma variável
multiplicacao = multiplicar(10, 2, 3, 4, 5)
print(multiplicacao)

"""
Crie uma função fala se um número é par ou ímpar.
Retorne se o número é par ou ímpar.
"""
def par_impar(numero):
    # Verifica se o número é múltiplo de 2
    multiplo_de_dois = numero % 2 == 0

    # Se for verdaddeiro, retorna "par"
    if multiplo_de_dois:
        return f'{numero} é par'
    
    # Caso contrário, reotrna "ímpar"
    return f'{numero} é ímpar'

# Funções em Python são objetos e podem ser atribuídas a variáveis
outro_par_impar = par_impar

# Chamando a função através da variável
dois_e_par = outro_par_impar(2)
print(dois_e_par)

# Chamadas diretas da função
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))

# Verifica se as duas variáveis apontam para a mesma função
print(par_impar is outro_par_impar)