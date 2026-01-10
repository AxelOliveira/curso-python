"""
Crie um programa que represente um controle simples de gastos da casa.

1 O programa deve:
- Ter uma lista vazia chamada gastos
    -Cada gasto será uma lista no formato:
        [descricao, valor]

2 Mostrar um menu com as opções:
- [i] inserir gasto
- [l] listar gastos
- [r] remover gasto pelo índice
- [t] mostrar total dos gastos
- [s] sair

3 Inserir gasto
- Pedir ao usuário uma descrição (string)
- Pedir um valor decimal
- Usar try / except para evitar erro se o valor não for número
- Armazenar como:
    ['Mercado', 125.50]

4 Listar gastos
- Se a lista estiver vazia, mostrar:
    Nada para listar
- Caso contrário, mostrar:
    0 - Mercado | R$ 125.50

5 Remover gasto
- Pedir um índice
- Usar try / except para:
    índice inexistente
    valor não numérico

6 Mostrar total
- Somar todos os valores
- Mostrar:
    total normal (float)
    total com round(valor, 2)
    total usando decimal.Decimal

7 Usar comentários explicando a lógica e a ordem computacional, não apenas o que o código faz.
"""
import os
import decimal

# 1 - Cria a lista vazia que armazenará todos os gastos
# Cada gasto será uma lista no formato: [descricao, valor]
gastos = []

# 2 - Inicia um laço infinito para o programa continuar rodando
while True:

    # 3 - Exibe o menu de opções para o usuário
    print('\nSelecione uma opção:')
    print('[i] Inserir gasto')
    print('[l] Listar gastos')
    print('[r] Remover gasto pelo índice')
    print('[t] Mostrar total dos gastos')
    print('[s] Sair')

    # 4 - Lê a opção escolhida pelo usuário
    opcao = input('Opção: ').lower()


# 5 - Se a opção for inserir, solicita a descrição e o valor do gasto
#     e armazena tudo como uma única estrutura na lista de gastos
    if opcao == 'i':

        try:
            # 5.1 - Limpa o terminal
            os.system('cls')

            # 5.2 - Solicita a descrição do gasto
            descricao = input('Informe a descrição do gasto: ').strip()

            # 5.3 - Solicita o valor e tenta converter para número decimal
            valor = float(input('Informe o valor: '))

            # 5.4 - Cria uma estrutura representando UM gasto
            gasto = [descricao, valor]

            # 5.5 - Adiciona o gasto completo à lista principal
            gastos.append(gasto)
   
        except ValueError:
            # 5.6 - Trata erro caso o valor digitado não seja numérico
            print('Por favor digite apenas números no campo "Informe o valor"')


# 6 - Se a opção for listar, verifica se a lista está vazia e, se não estiver, percorre mostrando todos os itens
    elif opcao == 'l':

        # 6.1 - Limpa o terminal
        os.system('cls')

        # 6.2 - Verifica se a lista está vazia
        if len(gastos) == 0:
            print('Nada a mostrar')

        # 6.3 - Percorre a lista mostrando índice e valor
        else:
            # 6.4 - Percorre a lista de gastos
            for i, gasto in enumerate(gastos):
                # gasto[0] → descrição
                # gasto[1] → valor
                print(f'{i} - {gasto[0]} | R$ {gasto[1]:.2f}')     

# 7 - Se a opção for remover, mostra os itens com índices, solicita o índice escolhido e trata erro caso o índice seja inválido
    elif opcao == 'r':

        # 7.1 - Verifica se há gastos para remover
        if len(gastos) == 0:
            print('Não há gastos para remover')
            continue    # volta para o ínicio do loop

        # 7.2 - Mostra todos os gastos com seus índices
        print('\nGastos disponíveis para remoção: ')
        for i, gasto in enumerate(gastos):
            print(f'{i} - {gasto[0]} | R$ {gasto[1]:.2f}')

        try:
        # 7.3 - Solicita o índice do gasto a ser removido
            indice = int(input('Escolha o índice para remover: '))

            # 7.4 - Remove o gasto usando o índice informado
            del gastos[indice]

        except ValueError:
            # 7.5 - Trata erro caso o valor não seja numérico
            print('Por favor digite números inteiros')

        except IndexError:
            # 7.6 - Trata erro caso o índice não exista
            print('índice não existente')

# 8 - Se a opção for mostrar o total, percorre os gastos somando os valores e exibe o resultado
    elif opcao == 't':

        # 8.1 - Inicializa a soma total
        total = 0

        # 8.2 - Percorre todos os gastos somando apenas os valores
        for gasto in gastos:
            total += gasto[1]

        # 8.3 - Mostra o total usando float normal
        print(f'Total (float): R$ {total}')

        # 8.4 - Mostra o total arredondado
        print(f'Total (round): R$ {round(total, 2)}')

        # 8.5 - Mostra o total usando decimal para maior precisão
        total_decimal = decimal.Decimal('0')
        for gasto in gastos:
            total_decimal += decimal.Decimal(str(gasto[1]))

        print(f'Total (decimal): R$ {total_decimal}')

# 9 - Se a opção for sair, o loop se encerra
    elif opcao == 's':
        # 9.1 - Encerra o laço e finaliza o programa
        print('Encerrando o programa')
        break

    else:
        # 9.2 - Informa que a opção digitada não é válida
        print('Opção inválida. Escolha i, l, r, t ou s')