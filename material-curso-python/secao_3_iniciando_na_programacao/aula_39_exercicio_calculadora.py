"""Calculadora com while"""
# starwith = começa com
# endwith = termina com

print('-' * 12, 'Calculadora', '-' * 12)                     # Exibe o título da calculadora
print('Digite os números que deseja calcular \n')            # Instrução inicial para o usuário

while True:                                                  # Loop principal da calculadora
    try:
        # Entrada de valores (string)
        numero1 = input('Digite um número: ')                # Primeiro número digitado pelo usuário
        numero2 = input('Digite outro número: ')             # Segundo número digitado pelo usuário

        # Conversão das entradas
        num1f = float(numero1)                               # Converte o primeiro número para float
        num2f = float(numero2)                               # Converte o segundo número para float
 
        # Menu de operações
        print('\nQual operação você deseja realizar?'
              '\n[1] Soma'
              '\n[2] Subtração'
              '\n[3] Multiplicação'
              '\n[4] Divisão'
              '\n[5] Sair do programa')
 
        operacao = input('Escolha a operação: ')               # Recebe a opção do menu

        # Conversão da escolha do menu
        operacao_int = int(operacao)                           # Converte a opção para inteiro
 
        # Condição de saída do programa
        if operacao_int == 5:
            print('\nAté mais!')                               # Mensagem de encerramento
            break                                              # Encerra o loop principal

        # Condição de soma
        elif operacao_int == 1:
            soma = num1f + num2f                                # Realiza a soma
            print(f'\nA soma dos números {num1f:.2f} e {num2f:.2f} é {soma:.2f} \n')

        # Condição de subtração
        elif operacao_int == 2:
            subtracao = num1f - num2f                            # Realiza a subtração
            print(f'\nA subtração dos números {num1f:.2f} e {num2f:.2f} é {subtracao:.2f} \n')

        # Condição de multiplicação
        elif operacao_int == 3:
            multiplicacao = num1f * num2f                         # Realiza a multiplicação
            print(f'\nA multiplicação dos números {num1f:.2f} e {num2f:.2f} é {multiplicacao:.2f} \n')
            
        # Condição de divisão
        elif operacao_int == 4:
            try:
                divisao = num1f / num2f                            # Tenta realizar a divisão
                print(f'\nA divisão dos números {num1f:.2f} e {num2f:.2f} é {divisao:.2f} \n')
            except:
                print('\nNão se divide por zero! \n')              # Trata erro de divisão por zero

    except:
        # Trata erro caso a conversão para float ou int falhe
        print('\nDigite apenas números! \n')
        continue                                                   # Volta para o início do loop
