"""
🧩 Exercício 1
Crie um programa que:
- crie uma lista vazia
- permita inserir valores digitados pelo usuário
- permita listar todos os valores
- utilize while True e if / elif / else
"""
# 1 - Criação lista vazia
lista = []

# 2 - Laço de repetição 
while True:

    # 3 - Exibe as opções disponíveis para o usuário
    print('Selecione uma opção')

    # 4 - Listar opções disponivel para o usuário
    opcao = input('[i]nserir [l]istar: ')

    # 5 - Verifica se a opção escolhida foi inserir
    if opcao == 'i':
        
        # 6 - Solicita o valor ao usuario
        valor = input('Valor: ')

        # 7 - Inclui o valor inserido pelo usuario na lista
        lista.append(valor)

    # 8 - Verifica se a opção escolhida foi listar    
    elif opcao == 'l':

        # 9 - Verifica se a lista está vazia
        if len(lista) == 0:
            # 10 - Mostra que não tem nenhum valor inserido
            print('Nada para listar')
        
        # 11 - Percorre a lista mostrando índice e valor
        for i, valor in enumerate(lista):
            # 12 - Imprime o índice e o valor correspondente
            print(i, valor)

    # 13 - Caso o usuário digite uma opção inválida        
    else:
        # 14 - Exibe uma mensagem orientando as opções corretas
        print('Por favor, escolha i ou l.')
        

#--------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 2
Crie um programa que:
- tenha uma lista com alguns valores iniciais
- peça ao usuário um índice para apagar
- use try / except para:
- tratar erro de índice inexistente
- tratar erro de valor não numérico
"""
# 1 - Criação da Lista
lista = [1, 2, 3, 4, 5]

# 2 - Laço de repetição
while True:

    # 3 - Solicita ao usuario um índice para ser apagado
    indice_str = input('Escolha um índice para ser apagada: ')

    try:
        # 4 - Tenta converter valor para inteiro
        indice = int(indice_str)

        # 5 - Deleta da lista o índice informado
        del lista[indice]
        # 6 - Mostra a lista
        print(lista)

    except ValueError:
        # 7 - Trata o erro caso o valor digitado não seja um número inteiro
        print('Por favor digite número int.')

    except IndexError:
        # 8 - Trata o erro caso o índice não exista na lista
        print('Índice não existe na lista')
        break

#--------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 3
Crie um programa que:
- permita listar os itens da lista
- se a lista estiver vazia, mostre uma mensagem informando isso
- use len(lista) para a verificação
"""
lista = [1, 2, 3, 4, 5]

# 1 - Verifica se a lista está vazia
if len(lista) == 0:
    print('Nada para listar')
else:
    # 2 - Percorre a lista exibindo índice e valor
    for i, valor in enumerate(lista):
        print(i, valor)
    

#--------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 4
Crie um programa que:
- some dois números decimais (float)
- mostre o resultado normal
- mostre o resultado usando round(valor, 2)
- observe a diferença de precisão
"""
numero_1 = 15.56
numero_2 = 13.68

# 1 - Soma usando float 
soma_1 = numero_1 + numero_2
print(soma_1)

# 2 - Mostra o valor arredondado
print(round(soma_1, 2))

#--------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 5
Crie um programa que:
- importe o módulo decimal
- crie dois números usando decimal.Decimal
- faça a soma
- imprima o resultado sem imprecisão
"""
import decimal

# 1 - Cria números decimais precisos usando Decimal (evita imprecisão do float)
numero_1 = decimal.Decimal('5.36')
numero_2 = decimal.Decimal('6.36')

# 2 - Realiza a soma dos dois valores decimais
soma = numero_1 + numero_2

# 3 - Imprime o resultado exato, sem erro de precisão
print(soma)

#--------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 6
Crie um programa que:
- tenha uma string com espaços extras
- use .split() para dividir a string
- use .strip() para remover espaços
- gere uma nova lista com os valores limpos
"""
# 1 - String original com espaços extras
palavra = 'Sou,             bonita'

# 2 - Divide a string usando a vírgula como separador
lista_palavra = palavra.split(',')

# 3 - Cria uma lista vazia para armazenar os valores limpos
lista_frases = []

# 4 - Percorre cade parte da string dividida
for i, frase in enumerate(lista_palavra):
    # 5 - Remove espaços extras do início e do fim de cada parte
    lista_frases.append(lista_palavra[i].strip())

# 6 - Une os valores limpos em uma única string separada por vírgula
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)

#--------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 7
Crie um programa que:
- tenha uma lista de palavras
- use .join() para transformar a lista em uma string
- separe os valores usando ,
"""
# 1 - Lista de palavras
lista = ['Axel', 'Wonwoo', 'Vernon', 'San', 'Jaemin', 'Jeno']

# 2 - Lista auxiliar para armazenas os valores tratados
lista_frases = []

# 3 - Percorre cada item da lista
for i, frase in enumerate(lista):
    # 4 - Adiciona cada palavra à nova lista (strip é redundante, mas não prejudica)
    lista_frases.append(lista[i].strip())

# 5 - Une as palavras em uma única string separada por vírgula
palavras_unidas = ', '.join(lista_frases)
print(palavras_unidas)

#--------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 8
Crie uma lista de listas representando salas com alunos.
Depois:
- imprima um aluno específico usando dois índices
- comente explicando o significado de cada índice
"""
salas = [

    ['Axel', 'Wonwoo'],
    ['Vernon'],
    ['San', 'Jaemin', 'Jeno']
]

# salas[0] -> acessa a primeira lista (primeira sala)
# [1] -> acessa o segundo aluno dentro dessa sala
print(salas[0][1])
        
#--------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 9
Crie uma lista de listas com nomes.
Use:
- um for para percorrer as listas
- outro for interno para percorrer os valores
- imprima cada valor separadamente
"""
salas = [

    ['Axel', 'Wonwoo'],
    ['Vernon'],
    ['San', 'Jaemin', 'Jeno']
]

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)
        
#--------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 10
Crie um programa que:
- use uma lista de listas
- permita listar os valores
- use try / except para evitar erro de índice
- utilize comentários explicando a lógica computacional
"""
# 1 - Lista de listas
salas = [
    ['Axel', 'Wonwoo'],
    ['Vernon'],
    ['San', 'Jaemin', 'Jeno']
]

try:
    # 2 - Solicita índices
    indice_sala = int(input('Informe o índice da sala: '))
    indice_aluno = int(input('Informe o índice do aluno: '))

    # 3 - Acessa usando dois índices
    print(salas[indice_sala][indice_aluno])

except IndexError:
    print('índice não existe na lista')

except ValueError:
    print('Digite apenas números')        