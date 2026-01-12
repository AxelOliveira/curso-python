import random

# 1 - Repete o processo 100 vezes para gerar 100 CPFs válidos
for _ in range(100):

    # 2 - Inicializa uma string vazia para armazenar os 9 primeiros dígitos do CPF
    nove_digitos = ''

    # 3 - Gera 9 números aleatórios para formar a base do CPF
    for i in range(9):
        # 3.1 - Gera um número aleatório entre 0 e 9
        # 3.2 - Converte para string
        # 3.3 - Concatena ao CPF parcial
        nove_digitos += str(random.randint(0, 9))

    # 4 - Inicializa o contador regressivo para o cálculo do primeiro dígito
    contador_regressivo_1 = 10

    # 5 - Inicializa o acumulador do resultado da soma
    resultado_digito_1 = 0

    # 6 - Percorre cada dígito dos 9 primeiros números
    for digito in nove_digitos:
        # 6.1 - Multiplica o dígito atual pelo contador regressivo
        # 6.2 - Soma o resultado ao total acumulado
        resultado_digito_1 += int(digito) * contador_regressivo_1

        # 6.3 - Decrementa o contador para a próxima multiplicação
        contador_regressivo_1 -= 1

    # 7 - Calcula o primeiro dígito verificador
    digito_1 = (resultado_digito_1 * 10) % 11

    # 8 - Se o resultado for maior que 9, o dígito vira 0
    digito_1 = digito_1 if digito_1 <= 9 else 0

    # 9 - Junta os 9 dígitos iniciais com o primeiro dígito verificador
    dez_digitos = nove_digitos + str(digito_1)

    # 10 - Inicializa o contador regressivo para o segundo dígito
    contador_regressivo_2 = 11

    # 11 - Inicializa o acumulador do segundo cálculo
    resultado_digito_2 = 0

    # 12 - Percorre os 10 dígitos para calcular o segundo verificador
    for digito in dez_digitos:
        # 12.1 - Multiplica o dígito pelo contador
        # 12.2 - Soma ao resultado acumulado
        resultado_digito_2 += int(digito) * contador_regressivo_2

        # 12.3 - Decrementa o contador
        contador_regressivo_2 -= 1
    
    # 13 - Calcula o segundo dígito verificador
    digito_2 = (resultado_digito_2 * 10) % 11

    # 14 - Ajusta para 0 se o valor for maior que 9
    digito_2 = digito_2 if digito_2 <= 9 else 0

    # 15 - Monta o CPF final com 11 dígitos
    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

    # 16 - Exibe o CPF gerado
    print(cpf_gerado_pelo_calculo)