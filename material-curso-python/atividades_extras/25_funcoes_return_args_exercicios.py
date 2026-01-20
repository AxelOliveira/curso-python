"""
🧠 AULA 6 — Retorno de valores (return)
🧩 Exercício 1 — Retorno simples
Crie uma função chamada dobro que:
- Receba um número
- Retorne o dobro desse número
Depois:
- Guarde o retorno em uma variável
- Imprima a variável
"""
# 1 - Função que recebe um argumento
def dobro(numero):
    # 2 - retorna o argumento multiplicado por 2
    return numero * 2

# 3 - Variável que recebe o retorno da função
num = dobro(2)

print(num)

# --------------------------------------------------------------------------------------------

"""
🧩 Exercício 2 — Return com condição
Crie uma função chamada verificar_numero que:
- Receba um número
- Se o número for maior que 10, retorne "Maior que 10"
- Caso contrário, retorne "10 ou menor"
"""
# 1 - Função que recebe um argumento
def verificar_numero(numero):
        # 2 - Verifica se o numero informado é maior que 10
    if numero > 10:
        # 3 - Se for maior que 10, retorna "Maior que 10"
        return "Maior que 10"
    # 4 - Caso contrário, retorna "10 ou menor"
    return "10 ou menor"

num = verificar_numero(100)

print(num)

# --------------------------------------------------------------------------------------------

"""
🧠 AULA 7 — *args (argumentos não nomeados)
🧩 Exercício 3 — Soma com args
Crie uma função chamada somar_todos que:
- Receba qualquer quantidade de números usando *args
- Retorne a soma de todos eles
Depois:
- Teste com 2 números
- Teste com 5 números
"""
# 1 - Criar uma função recebendo *args
def somar_todos(*args):
    # 2 - Cria uma variavel total
    total = 0
    # 3 - Percorre todos os números dentro de args
    for numero in args:
        total += numero
    # 4 - Retorna a soma deles
    return total

# 5 - Argumentos não nomeados que serão passados para a função
soma_1 = somar_todos(1, 2, 3)
soma_2 = somar_todos(1, 2, 3, 4, 5)

print(soma_1)
print(soma_2)

# --------------------------------------------------------------------------------------------

"""
🧩 Exercício 4 — Maior número
Crie uma função chamada maior_numero que:
- Receba vários números com *args
- Retorne o maior número recebido
- (Não use max())
"""
# 1 - Função que recebe vários argumentos não nomeados
def maior_numero(*args):
    # 2 - Guarda o primeiro valor como base de comparação
    maior_valor = args[0]

    # 3 - Percorre todos os valores recebidos
    for numero in args:
        if numero > maior_valor:
            maior_valor = numero

    # 4 - Retorna o maior valor encontrado
    return maior_valor

num_maior = maior_numero(10, 4, 3, 6, 0, 25)
print(num_maior)

# --------------------------------------------------------------------------------------------

"""
🧠 AULA 8 — Exercícios com funções
🧩 Exercício 5 — Multiplicação com args
Crie uma função que:
- Receba vários números (*args)
- Retorne a multiplicação de todos eles
Depois:
- Mostre o resultado na tela
"""
# 1 - Criar a função e receber os valores
def multiplicacao(*args):
    # 2 - Variavel total para armazenar os valores
    total = 1

    # 3 - For vai percorrer toda a tupla e fazer a multiplicacao
    for numero in args:
        total *= numero
    # 4 - Retorna o valor da multiplicação
    return total

# 5 - Argumentos
num = multiplicacao(5, 6, 3, 8, 1, 7)

print(num)

# --------------------------------------------------------------------------------------------

"""
🧩 Exercício 6 — Par ou ímpar com return
Crie uma função chamada par_ou_impar que:
- Receba um número
- Retorne "par" ou "ímpar"
Depois:
- Teste a função com pelo menos 3 números
"""
# 1 - Criar função e receber o número
def par_ou_impar(numero):
    # 2 - Verifica se o número é múltiplo de 2
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return "Par"
    return "ímpar"

num = par_ou_impar(3)
num_1 = par_ou_impar(2)
num_2 = par_ou_impar(17)

print(num)
print(num_1)
print(num_2)

# --------------------------------------------------------------------------------------------

"""
🧠 AULA 9 — Higher Order Functions / First-Class Functions
🧩 Exercício 7 — Função como argumento
Crie:
- Uma função quadrado que retorna o quadrado de um número
- Uma função executar que:
- Receba uma função
- Receba um número
- Retorne o resultado da função aplicada ao número
"""
# 1 - Função que retorna o quadrado de um número
def quadrado(numero):
    return numero ** 2

# 2 - Função que recebe outra função e um número
def executar(funcao, numero):
    # 3 - Recebe uma função como argumento (Higher Order Function)
    return funcao(numero)

# 4 - Passa a função 'quadrado' como argumento (Execute a função quadrado usando o número 9)
resultado = executar(quadrado, 9)

print(resultado)

# --------------------------------------------------------------------------------------------

"""
🧩 Exercício 8 — Função atribuída a variável
Crie uma função que:
- Receba um nome
- Retorne "Olá, nome"
Depois:
- Atribua essa função a uma variável
- Use a variável para chamar a função
"""
# 1 - Função que recebe um nome e retorna uma saudação
def saudacao(nome):
    return f'Olá, {nome}!'

# 2 - Atribui a função a uma variável 
outra_saudacao = saudacao                           # função

# 3 - Usa a variável para chamar a função
print(outra_saudacao('Axel'))                       # chamada da função

# --------------------------------------------------------------------------------------------

"""
🧠 AULA 10 — Termos técnicos (fixação conceitual)
🧩 Exercício 9 — Identificação
Observe o código abaixo e responda nos comentários:

def mensagem(nome):
    return f'Olá, {nome}'
outra = mensagem
print(outra('Maria'))

Explique:
- Por que isso é um exemplo de First-Class Function
"""
# É um exemplo de First-Class Function porque a função 'mensagem' foi atribuída a uma variável e usada como qualquer outro valor

# --------------------------------------------------------------------------------------------

"""
🧩 Exercício 10 — Higher Order
Crie uma função chamada aplicar que:
- Receba uma função
- Receba um valor
- Retorne o resultado da função aplicada ao valor
Explique nos comentários:
- Por que essa função é uma Higher Order Function? É uma Higher Order Function porque recebe outra função como argumento
"""
# 1 - Função simples que recebe um número
def dobro(numero):
    # 2 - Retorna o número multiplicado por 2
    return numero * 2

# 3 - Função aplicar recebe outra função e um valor
def aplicar(funcao, valor):
    # 4 - Executa a função recebida passando o valor como argumento
    return funcao(valor)

resultado = aplicar(dobro, 5)
print(resultado)

# --------------------------------------------------------------------------------------------

"""
🧠 AULA 11 — Closure
🧩 Exercício 11 — Closure básico
Crie uma função chamada criar_multiplicador que:
- Receba um número
- Retorne uma função que multiplica outro número por esse valor
Exemplo esperado:
    dobrar = criar_multiplicador(2)
        print(dobrar(5))  # 10
"""
# 1 - Função externa que recebe um número
def criar_multiplicador(multiplicador):

    # 2 - Função interna que usa o valor da função externa
    def multiplicar(numero):
        # 3 - Usa o valor 'multiplicador' mesmo após a função externa terminar
        return numero * multiplicador
    
    # 4 - Retorna a funçao interna (closure)
    return multiplicar

dobrar = criar_multiplicador(2)
print(dobrar(5))

# --------------------------------------------------------------------------------------------

"""
🧩 Exercício 12 — Closure com texto
Crie uma função chamada criar_mensagem que:
Receba uma palavra (ex: "Bom dia")
Retorne uma função que recebe um nome
Retorne a mensagem completa
Exemplo:
bom_dia = criar_mensagem('Bom dia')
print(bom_dia('Axel'))
"""
# 1 - Função externa que recebe uma mensagem fixa
def criar_mensagem(mensagem):

    # 2 - Função interna que recebe o nome
    def mostrar(nome):
        # 3 - Usa a mensagem da função externa + o nome recebido
        return f'{mensagem}, {nome}'
    
    # 4 - Retorna a função interna
    return mostrar

bom_dia = criar_mensagem('Bom dia')
print(bom_dia('Axel'))