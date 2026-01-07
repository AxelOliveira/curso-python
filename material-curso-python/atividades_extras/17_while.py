"""
🧩 Exercício 1
Use while para imprimir os números de 1 até 10.
"""
contador = 0

while contador <= 9:
    contador += 1
    print(contador)
    
#--------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 2
Use while para imprimir os números de 10 até 1.
"""
contador = 11

while contador >= 2:
    contador -= 1
    print(contador)
    
#--------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 3
Crie uma variável contador iniciando em 0.
Use while para imprimir os valores enquanto contador for menor que 5.
"""
contador = 0

while contador < 5:
    contador += 1
    print(contador)
    
#--------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 4
Use while para imprimir apenas os números pares de 0 até 20.
"""
contador = 0

while contador <= 20:
    if contador % 2 == 0:
        print(contador)
    contador += 1
else:
    print('loop acabou')
    
#--------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 5
Use while para somar os números de 1 até 100 e imprimir o resultado final.
"""
contador = 1
soma = 0

while contador <= 100:
    soma = contador + soma
    contador += 1    
else:
    print(soma)