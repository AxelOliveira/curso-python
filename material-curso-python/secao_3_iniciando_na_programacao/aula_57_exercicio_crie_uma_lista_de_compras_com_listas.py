"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
"""
🔹 1. Inicialização
Criar uma lista vazia para armazenar os itens da compra.
🔹 2. Execução contínua
Iniciar um laço de repetição para o programa continuar funcionando até ser encerrado manualmente.
🔹 3. Interação com o usuário
Exibir as opções disponíveis:
inserir
apagar
listar
Ler a opção escolhida pelo usuário.
🔹 4. Tomada de decisão
Verificar qual opção foi escolhida.
🔹 5. Inserir item
Se a opção for inserir:
solicitar o valor ao usuário
adicionar o valor à lista
🔹 6. Apagar item
Se a opção for apagar:
solicitar o índice do item
tentar converter o valor para número
tentar apagar o item usando o índice
se o índice não existir, tratar o erro sem encerrar o programa
🔹 7. Listar itens
Se a opção for listar:
verificar se a lista está vazia
se estiver vazia, informar o usuário
se não estiver vazia, mostrar cada item com seu índice
🔹 8. Opção inválida
Se a opção não for reconhecida:
informar que a opção é inválida
🔹 9. Continuidade
Após qualquer ação:
voltar ao início do laço
aguardar nova opção do usuário
"""

import os

# 1 - Cria uma lista vazia para armazenar os valores inseridos pelo usuário
lista = []

# 2 - Inicia um loop infinito para o programa continuar rodando
while True:

    # 3 - Exibe as opções disponíveis para o usuário
    print('Selecione uma opção')

    # 4 - Lê a opção escolhida pelo usuário
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    # 5 - Verifica se a opção escolhida foi inserir
    if opcao == 'i':
        # 6 - Limpa a tela do terminal
        os.system('clear')

        # 7 - Solicita um valor ao usuário
        valor = input('Valor: ')

        # 8 - Adiciona o valor digitado à lista
        lista.append(valor)

    # 9 - Verifica se a opção escolhida foi apagar
    elif opcao == 'a':
        # 10 - Solicita ao usuário o índice do valor que deseja apagar
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        
        try:
            # 11 - Tenta converter o índice digitado para inteiro
            indice = int(indice_str)

            # 12 - Tenta remover o valor da lista usando o índice informado
            del lista[indice]

        except ValueError:
            # 13 - Trata o erro caso o valor digitado não seja um número inteiro
            print('Por favor digite número int.')

        except IndexError:
            # 14 - Trata o erro caso o índice não exista na lista
            print('Índice não existe na lista')

        except Exception:
            # 15 - Trata qualquer outro erro inesperado
            print('Erro desconhecido')

    # 16 - Verifica se a opção escolhida foi listar        
    elif opcao == 'l':
        # 17 - Limpa a tela do terminal
        os.system('clear')

        # 18 - Verifica se a lista está vazia
        if len(lista) == 0:
            # 19 - Informa que não há itens para listar
            print('Nada para listar')

        # 20 - Percorre a lista mostrando índice e valor
        for i, valor in enumerate(lista):
            # 21 - Imprime o índice e o valor correspondente
            print(i, valor)

    # 22 - Caso o usuário digite uma opção inválida        
    else:
        # 23 - Exibe uma mensagem orientando as opções corretas
        print('Por favor, escolha i, a ou l.')