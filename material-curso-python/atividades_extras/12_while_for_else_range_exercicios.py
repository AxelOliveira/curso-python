"""
🧩 Exercício 1 — while + else básico
Peça um número ao usuário.
Enquanto o número for menor que 5, peça novamente.
Quando o loop terminar sem break, mostre:
 * Número válido informado
🎯 Treinar:
- while
- else do while
- leitura do fluxo
"""
# Pede o primeiro número ao usuário
numero = float(input('Informe um número: '))

# Enquanto o número for menor que 5, o loop continua
while numero < 5:
    print('Número inválido, tente novamente')
    numero = float(input('Informe um número: '))          # Pede novamente

else:
    # Este else executa quando o while termina SEM usar break
    print('Número válido informado')                                                       
# ----------------------------------------------------------------------------------------------------

"""
🧩 Exercício 2 — while + break + else
Peça números ao usuário.
- Se o usuário digitar 0, use break
- Se sair naturalmente do while, execute o else
🎯 Treinar:
- diferença entre sair por condição vs break
"""
numero_usuario = 1

while numero_usuario != 0:
    numero_usuario = float(input('Insira um número: '))
else:
    print('Loop terminou sem usar break')
# ----------------------------------------------------------------------------------------------------    

"""
🧩 Exercício 3 — while iterando string
Peça uma palavra ao usuário.
Use while para mostrar cada caractere da palavra, um por linha.
🎯 Treinar:
- índice
- len()
- while com string
"""
palavra_usuario = input('Insira uma palavra: ')
i = 0                                                # índice inicial

while i < len(palavra_usuario):                      # Enquanto o índice for válido
    letra = palavra_usuario[i]                       # Pega a letra da posição i
    print(letra)                                     # Mostra a letra
    i += 1                                           # Avança o índice
# ----------------------------------------------------------------------------------------------------    

"""
🧩 Exercício 4 — while + string + contador
Peça uma frase.
Mostre apenas os caracteres nas posições pares usando while.
🎯 Treinar:
- controle de índice
- leitura de posição
"""
palavra_usuario = input('Insira uma palavra: ')
i = 0

while i < len(palavra_usuario):
    if i % 2 == 0:                                        # Se a posição for par
        print(palavra_usuario[i])                         # Mostra o caractere da posição
    i += 1                                                # Avança o índice
# ----------------------------------------------------------------------------------------------------    

"""
🧩 Exercício 5 — introdução ao for + in
Use for para mostrar cada letra da palavra:
* Python
🎯 Treinar:
- for
- in
- iteração simples
"""
palavra = 'Python'

for letra in palavra:                           # Para cada letra da palavra                
    print(letra)                                # Mostra a letra
# ---------------------------------------------------------------------------------------------------- 

"""
🧩 Exercício 6 — for iterando string do usuário
Peça um nome ao usuário.
Use for para mostrar:
* Letra: X
para cada caractere.
🎯 Treinar:
- for com entrada do usuário
"""
nome_usuario = input('Insira seu nome: ')

for letra in nome_usuario:                       # Percorre cada caractere do nome
    print(f'Letra: {letra}')                     # Mostra a letra formatada
# ----------------------------------------------------------------------------------------------------

"""
🧩 Exercício 7 — for + range simples
Use for e range para mostrar números de 1 até 5.
🎯 Treinar:
- range(inicio, fim)
- entender que o fim não entra
"""
numeros = range(1, 6)

for numero in numeros:
    print(numero)
# ----------------------------------------------------------------------------------------------------

"""
🧩 Exercício 8 — for + range com passo
Mostre os números pares de 0 até 10 usando range.
🎯 Treinar:
- range(inicio, fim, passo)
"""
for numero in range(0, 11, 2):
    print(numero)
# ----------------------------------------------------------------------------------------------------

"""
🧩 Exercício 9 — comparação while vs for
Faça duas versões do mesmo programa:
* uma usando while
* outra usando for
Objetivo:
Mostrar números de 1 até 5.
🎯 Treinar:
- perceber quando for é mais simples
"""
# Versão com while
contador = 1

while contador <= 5:
    print(contador)
    contador += 1


print()

# Versão com for
for numero in range(1, 6):
    print(numero)
# ----------------------------------------------------------------------------------------------------

"""
🧩 Exercício 10 — for + else (conceito)
Use for para percorrer números de 1 até 5.
* Se encontrar o número 3, use break
* Se não encontrar, o else deve executar
🎯 Treinar:
- for + else
- fluxo de controle
"""
for numero in range(1, 6):                               # Percorre de 1 até 5
    if numero == 3:                                      # Se encontrar o número 3
        print('Número 3 encontrado') 
        break                    
    print(numero) 

else:
    # Só executa se o for terminar sem break
    print('Número 3 não foi encontrado')