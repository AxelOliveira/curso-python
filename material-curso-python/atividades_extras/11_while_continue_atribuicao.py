"""🧠 Exercícios
🧩 Exercício 1 — Contador com +=
Crie uma variável contador = 0.
Use while para somar 1 até o contador chegar em 5, usando +=.
Mostre o valor a cada repetição.
🎯 Treinar: += + while
"""
contador = 0

while contador < 5:
    contador +=1
    print(contador)

# ----------------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 2 — Subtração controlada com -
Crie valor = 20.
Enquanto valor for maior que 0:
 - subtraia 2 usando -=
 - mostre o valor
🎯 Treinar: -= + condição do while
"""
valor = 20

while valor > 0:
    valor -= 2
    print(valor)

# ----------------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 3 — Pulando números pares (continue)
Crie um contador de 1 até 10.
Use continue para pular os números pares.
Mostre apenas os ímpares.
🎯 Treinar: continue + leitura do fluxo
"""
contador = 0

while contador < 10:
    contador += 1

    if contador % 2 == 0:
        continue

    print(f'{contador}')

# ----------------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 4 — Soma acumulada
Peça números ao usuário.
Some cada número em uma variável total usando +=.
Quando o usuário digitar 0, pare o loop e mostre o total.
🎯 Treinar: += + controle do loop
"""
total = 0

while True:
    numero_usu = float(input('Insira um número: '))
    
    if numero_usu == 0:
        print(f'Total final: {total}')
        break
    total += numero_usu

# ----------------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 5 — Multiplicação repetida com *=
Crie:
 * resultado = 1
 * contador = 1
Enquanto contador ≤ 5:
 - multiplique resultado por contador usando *=
 - incremente o contador
Mostre o resultado final.
🎯 Treinar: *= + loop controlado
"""

resultado = 1
contador = 1

while contador <= 5:
    resultado *= contador
    contador += 1

print(resultado)

# ----------------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 6 — continue para ignorar valor específico
Crie um contador de 1 até 10.
Use continue para ignorar o número 7.
Mostre os demais números.
🎯 Treinar: continue bem posicionado
"""
contador = 0

while contador < 10:
    contador += 1

    if contador == 7:
        continue

    print(contador)

# ----------------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 7 — Laço dentro de laço (while + while)
Use dois contadores:
 - externo: de 1 até 3
 - interno: de 1 até 5
Mostre algo como:
 * Linha 1: 1 2 3 4 5
 * Linha 2: 1 2 3 4 5
 * Linha 3: 1 2 3 4 5
🎯 Treinar: while interno e externo
"""
qtd_externo_linha = 3
qtd_interno_coluna = 5

externo_linha = 1
while externo_linha <= qtd_externo_linha:
    interno_coluna = 1
    print(f'Linha {externo_linha}:', end=' ')

    while interno_coluna <= qtd_interno_coluna:
        print(interno_coluna, end=' ')
        interno_coluna += 1
    
    print()
    externo_linha += 1

print('Acabou')

# ----------------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 8 — Tabuada com while interno
Peça um número ao usuário.
Use while para mostrar a tabuada desse número de 1 a 10.
🎯 Treinar: laço interno + controle manual
"""
numero = int(input('Insira um número: '))

contador = 1

while contador <= 10:
    resultado = numero * contador
    print(resultado)
    contador += 1
    
# ----------------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 9 — Acumulador com condição e continue
Peça números ao usuário enquanto o número for positivo.
Some apenas os números maiores que 5 usando +=.
Use continue para ignorar os menores ou iguais a 5.
🎯 Treinar: lógica + continue + atribuição
"""
total = 0

while True:
    numero_usuario = int(input('Insira um número: '))

    if numero_usuario < 0:
        break

    if numero_usuario <= 5:
        continue

    total += numero_usuario

print(f'Total final: {total}')

# ----------------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 🔟 — Simulação com dois whiles
Crie:
 - um while externo que controla tentativas (máx. 3)
 - um while interno que pede um número até ser maior que 10
Mostre:
 - quantas tentativas foram feitas
 - quando o número válido foi inserido
🎯 Treinar: controle mental de laços internos
"""

tentativas_max = 3
tentativas = 0

while tentativas < tentativas_max:
    print(f'\nTentativa {tentativas + 1}')

    while True:
        numero_usuario = int(input('Insira um número: '))

        if numero_usuario > 10:
            print('Número válido!')
            break

        else:
            print('Número inválido, tente novamente')

    tentativas += 1

print('\nFim das tentativas')