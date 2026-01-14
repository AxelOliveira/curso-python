"""
🧠 Exercício 1 — Criando e chamando função (bem básico)
Crie uma função chamada mensagem que:
- Não receba nenhum parâmetro
- Imprima a frase: "Aprendendo funções em Python"
Depois:
- Chame essa função duas vezes
"""
# 1 - Criação da função
def mensagem():
    # 2 - Mensagem que será exibida
    print('Aprendendo funções em python')

# 3 - Chamadas da função
mensagem()
mensagem()

#--------------------------------------------------------------------------------------------------------

"""
🧠 Exercício 2 — Parâmetro e argumento
Crie uma função chamada mostrar_nome que:
- Receba um parâmetro chamado nome
- Imprima: "Seu nome é: nome"
Depois:
- Chame a função passando dois nomes diferentes
"""
# 1 - Criação da função
def mostrar_nome(nome='Sem nome'):
    # 2 - Mensagem que será exibida
    print(f'Seu nome é: {nome}')

# 3 - Chamadas da função
mostrar_nome('Axel')
mostrar_nome('Wonwoo')

#--------------------------------------------------------------------------------------------------------

"""
🧠 Exercício 3 — Argumentos posicionais e nomeados
Crie uma função chamada dados_pessoais que:
- Receba três parâmetros: nome, idade, cidade
- Imprima tudo em uma linha
Depois:
1. Chame a função usando argumentos posicionais
2. Chame a função usando argumentos nomeados
"""
# 1 - Criação da função
def dados_pessoais(nome, idade, cidade):
    # 2 - Mensagem que será exibida
    print(f'Seu nome é: {nome}, você tem {idade} anos e mora em {cidade}')

# 3 - Argumentos nomeados
dados_pessoais(nome='Axel', idade=27, cidade='Goiânia')

# 4 - Chamadas da função
dados_pessoais('Axel', 27, 'Seul')

#--------------------------------------------------------------------------------------------------------

"""
🧠 Exercício 4 — Valor padrão
Crie uma função chamada boas_vindas que:
- Receba um parâmetro nome
- Receba um parâmetro curso com valor padrão "Python"
A função deve imprimir:
- Olá nome, bem-vindo ao curso de curso
Depois:
1. Chame a função passando nome e curso
2. Chame a função passando somente o nome
"""
# 1 - Criação da função
def boas_vindas(nome, curso='Python'):
    print(f'Olá {nome}, bem-vindo ao curso de {curso}')

# 6 - Chamadas da função
boas_vindas('Axel', 'Python')
boas_vindas('Wonwoo')

#--------------------------------------------------------------------------------------------------------

"""
🧠 Exercício 5 — Valor padrão com None
Crie uma função chamada somar que:
- Receba dois números obrigatórios a e b
- Receba um terceiro número opcional c com valor padrão None
Se c não for None:
- Imprima a soma dos três números
Se c for None:
- Imprima a soma apenas de a + b
Depois:
- Teste a função chamando com dois valores
- Teste a função chamando com três valores
- Teste usando argumentos nomeados
"""
# 1 - Criação da função
def somar(a, b, c=None):
    # 2 - Se c não for None, irá somar os 3 valores
    if c is not None:
        print(f'O resultado da soma de {a} + {b} + {c} é: ', a + b + c)
    # 3 - Se o c for None, irá somar somente a + b
    else:
        print(f'O resultado da soma de {a} + {b} é: ', a + b)

# 4 - Argumentos
somar(26, 17)
somar(a=27, b=18)
somar(c=26, a=17, b=18)