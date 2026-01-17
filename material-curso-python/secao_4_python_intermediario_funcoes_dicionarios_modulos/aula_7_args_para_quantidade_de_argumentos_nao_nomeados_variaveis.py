"""
args - Argumentos não nomeados
*args permite que uma função receba qualquer quantidade de argumentos não nomeados

Dentro da função, args se comporta como uma tupla

O * também é usado para desempacotar valores, ou seja, enviar vário valores de uma vez para uma função.

sum: recebe um iterável (lista, tupla, etc) e opcionalmente um valor inicial, exemplo:
sum([1, 2, 3])
sum([1, 2, 3], 10)

"""
# Lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

# def soma(x, y):
#     return x + y

def soma(*args):
    # args é uma tupla com todos os valores recebidos
    total = 0

    # Percorre todos os números dentro de args
    for numero in args:
        total += numero

    # Retorna o valor total da soma    
    return total

# Chamando a função com vários argumentos não nomeados
soma_1_2_3 = soma(1, 2, 3)
soma_4_5_6 = soma(4, 5, 6)

# Tupla de números
numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10

# Desempacotando a tupla para passar como argumentos
outra_soma = soma(*numeros)
print(outra_soma)

# A função sum faz algo parecido, mas recebe um iterável
print(sum(numeros))
