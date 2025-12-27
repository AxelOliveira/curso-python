"""
For + Range
range -> range(start, stop, step)
numeros = range(começo do número, parar em tal numero, pular de tanto numeros)
Não precisa de índices dentro do for que nem o while precisa, pois o For já faz isso sozinho
"""
numeros = range(0, 100, 8) # Aqui ele inicia do 0, vai até 100 pulando de 8 em 8 

for numero in numeros:
    print(numero)

print()

numeross = range(0, -10, -1) # Aqui ele inicia do 0, vai até -10 e pula de -1 em -1

for numere in numeross:
    print(numere)