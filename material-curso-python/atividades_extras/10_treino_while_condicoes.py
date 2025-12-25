"""
🧩 Exercício 1 — Quando a condição muda?
Peça um número ao usuário.
Enquanto o número for menor que 5:
- mostre o número
- peça outro número
🎯 Treinar:
- entender quando o while continua
- identificar quem controla a condição
🔍 Debug:
- breakpoint no while
- observe quando a condição vira False
"""
while True:
    numero_usuario = input('Informe um número: ')                      # Solicita um número ao usuario.......# A entrada do usuario controla a condição
    numero_int = int(numero_usuario)                                   # Converte a entrada para inteiro

    if numero_int < 5:                                                 # Verifica se a entrada é menor que 5....# Controle da continuação do loop
        print(f'{numero_int}, informe outro número')                   # Exibe mensagem final

    else:                                                              # Caso a entrada seja maior que 5
        break                                                          # Encerra o loop

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 2 — Controle consciente do loop
Crie um while True.
Peça números ao usuário.
- Se o número for negativo → encerre o loop
- Caso contrário → mostre o número
🎯 Treinar:
- while True
- uso correto do break
🔍 Debug:
- observe quando o break é atingido
"""
while True:
    numero_usuario = int(input('Insira um número: '))              # Entrada do usuário

    if numero_usuario >= 0:                                        # Controle da continuação do loop
        print(numero_usuario)                                      # Mensagem final
    else:                                                          # Caso o número seja menor que 0
        break                                                      # Encerra o loop

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 3 — Conversão segura
Peça um número ao usuário.
Use try/except apenas na conversão.
Enquanto o valor não for um número válido:
- mostre erro
- peça novamente
🎯 Treinar:
- erro acontece na conversão
- fluxo correto do except
🔍 Debug:
- veja o fluxo entrar e sair do except
"""
while True:
    numero_usuario = input('Informe um número: ')                     # Entrada do usuário
    try:
        numero_int = int(numero_usuario)                              # Conversão da entrada
        break                                                         # Para o loop se for um número
    except ValueError:                                                # Se não for número, vai repetir o loop
        print('Insira somente números')                               # Mensagem final

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 4 — Condição em português → código
Peça uma nota.
Crie variáveis booleanas:
- aprovado
- recuperacao
- reprovado
🎯 Treinar:
- transformar regra escrita em lógica
- evitar condições quebradas
🔍 Debug:
- observe os valores booleanos
"""
nota = float(input('Insira sua nota: '))                                 # Entrada do usuário

# Variaveis auxiliares
aprovado = nota >= 6
recuperacao = nota >= 4 and nota < 6
reprovado = nota < 4

if aprovado:
    print('Aprovado')
elif recuperacao:
    print('Recuperação')
else:
    print('Reprovado')

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 5 — while + validação clara
Peça uma senha.
Enquanto:
- tiver menos de 8 caracteres
ou
- contiver "123"
→ peça novamente
Quando for válida:
- mostre mensagem
- encerre o loop
🎯 Treinar:
- condição composta
- leitura do while
🔍 Debug:
- veja quando a condição deixa de ser True
"""
TAMANHO_MIN_SENHA = 8
PALAVRA_PROIBIDA = "123"

while True:
    senha_usuario = input('Insira a sua senha: ')

    if len(senha_usuario) < TAMANHO_MIN_SENHA or PALAVRA_PROIBIDA in senha_usuario:               # A condição deixa de ser true quando tem += 8 caracteres e nao tem 123
        print('Senha inválida, informe outra senha')

    else:
        print('Senha válida') 
        break

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 6 — Variável que controla tudo
Crie:
contador = 0
Enquanto o contador for menor que 3:
- mostre o valor
- incremente
🎯 Treinar:
- entender quem muda a condição
- evitar loop infinito
🔍 Debug:
- observe contador mudando
"""
contador = 0

while contador < 3:
    contador = contador + 1
    print(contador)

print('Acabou')

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 7 — Ordem de execução
Crie um programa que:
- peça idade
- converta
- verifique maioridade
Antes de rodar:
- escreva em comentário:
    - qual linha executa primeiro
    - qual linha decide o resultado
🎯 Treinar:
- fluxo do código
- leitura mental
"""
idade_usuario = input('Insira sua idade: ')              # Primeira linha a executar
idade_int = int(idade_usuario)

maioridade = 18

if idade_int >= maioridade:                              # Linha que decide o resultado
    print('maior de idade')
else:
    print('menor de idade')

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 8 — Boolean não é magia
Crie uma variável:
idade = 20
Crie:
maior = idade >= 18
menor = idade < 18
Mostre os valores.
🎯 Treinar:
- condição como valor
- perder o medo do True/False
🔍 Debug:
- observe as variáveis no painel
"""
idade = 20
maior = idade >= 18
menor = idade < 18

print(idade)
print(maior)
print(menor)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 9 — Código confuso vs código limpo
Faça dois códigos que:
- validam uma nota
1️⃣ usando if aninhado
2️⃣ usando variáveis auxiliares booleanas
Depois responda:
- qual foi mais fácil de debugar?
- qual você entendeu melhor?
🎯 Treinar:
- legibilidade
- clareza mental
"""
nota = int(input('Insira sua nota: '))

# if nota >= 6:
#     print('Aprovado')
# elif nota >= 4 and nota < 6:
#     print('Recuperação')
# else:
#     print('Reprovado')

# Variaveis auxiliares
aprovado = nota >= 6
recuperacao = nota >= 4 and nota < 6
reprovado = nota < 4

if aprovado:
    print('Aprovado')
elif recuperacao:
    print('Recuperação')
else:
    print('Reprovado')

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 🔟 — Simulação completa
Crie um programa que:
- peça nome, idade e senha
- valide idade e senha
- use while para repetir até estar correto
🎯 Treinar:
- juntar tudo
- pensar antes de codar
🔍 Debug:
- breakpoints estratégicos
- observar fluxo completo
"""
IDADE_MIN = 18
TAMANHO_MIN_SENHA = 8
PALAVRA_PROIBIDA = "123"


while True:
    nome_usuario = input('Insira seu nome: ')
    idade = int(input('Insira sua idade: '))
    senha = input('Insira sua senha: ')

    if idade >= IDADE_MIN and len(senha) >= TAMANHO_MIN_SENHA and PALAVRA_PROIBIDA not in senha:
        print('Usuário validado')
        break
    else:
        print('Usuario incorreto, informe novamente')        
        
