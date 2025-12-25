"""🧠 Exercício 1 — Tipos built-in
Peça ao usuário:
Um nome
Uma idade
Mostre:
O valor digitado
O tipo de cada variável usando type()
🎯 Objetivo: entender que input() sempre retorna str.
"""
nome_usuario = input('Insira seu nome: ')                               # Recebe o nome do usuário (sempre string)
idade_usuario = input('Insira sua idade: ')                             # Recebe a idade do usuário (string)

print ()

print(f'Seu nome é: {nome_usuario}')                                    # Exibe o nome digitado
print(f'Sua idade é: {idade_usuario}')                                  # Exibe a idade digitada

print()

print(type(nome_usuario))                                               # Mostra o tipo da variável
print(type(idade_usuario))                                              # Mostra o tipo da variável

#--------------------------------------------------------------------------------

"""🧠 Exercício 2 — Conversão e erro
Peça um número ao usuário e:
Converta para int
Mostre o tipo antes e depois da conversão
Teste digitando:
Um número
Uma letra
🎯 Objetivo: ver onde ocorre o ValueError.
"""
numero_usuario = input('Insira um número: ')                                # Entrada do usuário

print(type(numero_usuario))                                                 # Mostra o tipo antes da conversão

try:
    numero = int(numero_usuario)                                            # Tenta converter para inteiro
    print(type(numero))                                                     # Mostra o tipo após conversão
except ValueError:
    print('Digite apenas números')                                          # Executa se a conversão falhar

#--------------------------------------------------------------------------------

"""🧠 Exercício 3 — Tipos imutáveis
Crie:
texto = "Python"
Tente:
Alterar apenas uma letra
Criar um novo texto mudando uma letra
Pergunta:
Por que uma funciona e a outra não?
🎯 Objetivo: entender imutabilidade de strings.
"""
texto = 'Python'                                                # String original

# Texto [0] = 'P'                                               # Isso não funciona (string é imutável)

texto_novo = 'Pathon'                                           # Cria uma nova string modificada

print(texto)                                                    # Mostra a string original
print(texto_novo)                                               # Mostra a nova string

#--------------------------------------------------------------------------------

"""🧠 Exercício 4 — Métodos de string
Peça um nome e mostre:
Nome em maiúsculo
Nome em minúsculo
Quantidade de caracteres
As 3 primeiras letras
Use:
.upper()
.lower()
len()
fatiamento [:]
"""
nome_usuario = input('Insira seu nome: ')                       # Recebe o nome do usuário

print()                                                         # Linha em branco

print(nome_usuario.upper())                                     # Converte o nome para maiúsculas
print(nome_usuario.lower())                                     # Converte o nome para minúsculas
print(len(nome_usuario))                                        # Mostra a quantidade de caracteres
print(nome_usuario[:3])                                         # Mostra as 3 primeiras letras

#--------------------------------------------------------------------------------

"""🧠 Exercício 5 — while com condição simples
Peça um número ao usuário enquanto ele for menor que 10.
Quando for 10 ou maior:
Mostre uma mensagem
Pare o loop
🎯 Objetivo: entender quando o while continua ou para.
"""
while True:                                                   # Cria o loop infinito controlado por break
    numero_usuario = input('Informe um número: ')             # Recebe o número do usuário (string)
    numero_int = int(numero_usuario)                          # Converte a entrada para inteiro

    if numero_int >= 10:                                      # Verifica se o número é maior ou igual a 10
        print('Número maior ou igual a 10')                   # Exibe a mensagem final
        break                                                 # Encerra o loop

#--------------------------------------------------------------------------------

"""🧠 Exercício 6 — while + break
Faça um loop infinito com while True:
Peça um número
Se o número for 0, use break
Caso contrário, mostre o número digitado
🎯 Objetivo: entender controle manual do loop.
"""
while True:                                                       # Loop infinito
    numero_usuario = input('Insira um número: ')                  # Entrada do usuário
    numero_int = int(numero_usuario)                              # Converte para inteiro

    if numero_int != 0:                                           # Verifica se o número é zero
        break                                                     # Encerra o loop

print(numero_int)                                                 # Mostra o número digitado   

#--------------------------------------------------------------------------------

"""🧠 Exercício 7 — while + validação
Peça uma senha enquanto:
* Tiver menos de 8 caracteres
Quando for válida:
* Mostre "Senha aceita"
* Encerre o loop
🎯 Objetivo: praticar condição booleana no while.
"""

while True:                                                     # Loop infinito (vai rodar até o break)
    senha_usuario = input('Insira sua senha: ')                 # Pede a senha ao usuário

    if len(senha_usuario) < 8:                                  # Verifica se o tamanho da senha é menor que 8
        print('Senha recusada')                                 # Informa que a senha é inválida

    else:                                                       # Caso contrário (8 ou mais caracteres)
        print('Senha aceita')                                   # Informa que a senha é válida
        break                                                   # Encerra o loop

#--------------------------------------------------------------------------------

"""🧠 Exercício 8 — Leitura de condição (sem if complexo)
Crie:
idade = 20
Crie variáveis auxiliares:
maior_de_idade
menor_de_idade
Mostre o valor de cada uma.
🎯 Objetivo: entender que condição também é valor (True / False).
"""
idade = 20                                                         # Define a idade

maior_de_idade = idade >= 18                                       # Retorna True se idade >= 18
menor_de_idade = idade < 18                                        # Retorna True se idade < 18

print(maior_de_idade)                                              # Mostra True ou False
print(menor_de_idade)                                              # Mostra True ou False

#--------------------------------------------------------------------------------

"""🧠 Exercício 9 — while + contador
Use um contador para:
Mostrar números de 1 até 5 usando while
Depois responda:
Quantas vezes o loop executou?
🎯 Objetivo: entender fluxo e repetição controlada.
"""
contador = 1                                                    # Inicializa o contador

while contador <= 5:                                            # Condição do loop
    print(contador)                                             # Mostra o valor atual
    contador = contador + 1                                     # Incrementa o contador
    
print('Acabou')                                                 # Executa após o loop

#--------------------------------------------------------------------------------

"""🧠 Exercício 10 — while + leitura detalhada da condição
Crie:
numero = 1
Faça um while que:
Continue enquanto numero <= 3
Mostre o valor
Incremente o número
Explique em comentário:
Quando a condição é True
Quando se torna False
🎯 Objetivo: dominar avaliação de condição linha por linha.
"""
numero = 1                                                      # Valor inicial

while numero <= 3:                                              # Enquanto a condição for True
    print(numero)                                               # Mostra o valor atual
    numero = numero + 1                                         # Incrementa o valor
    
print('Acabou')                                                 # Executa quando a condição vira False