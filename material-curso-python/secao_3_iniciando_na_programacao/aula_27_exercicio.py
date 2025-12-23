"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

# ENTRADA DE DADOS DO USUARIO
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

nome_invertido = nome[::-1] # 
int_idade = int(idade)
qtd_letras = len(nome)
primeira_letra = nome[:1]
ultima_letra = nome[-1:]

print()

if nome and idade not in '':    
    print("Seu nome é: {}\nSeu nome invertido é: {}\nSeu nome contém {} letras \nA primeira letra do seu nome é: {}\nA última letra do seu nome é: {}".format(nome, nome_invertido, qtd_letras, primeira_letra, ultima_letra))
    if " " in nome:
        print("Seu nome contém espaços")
    else:
        print('Seu nome não contém espaços.')

else:
    print("Desculpe, você deixou campos vazios.")

print(50 * "-")

# RESPOSTA DO PROFESSOR
nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')

print()

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')
    
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')