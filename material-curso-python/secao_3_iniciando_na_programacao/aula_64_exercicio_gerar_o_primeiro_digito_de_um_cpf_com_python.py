"""
Cálculo do primeiro digito do CPF

CPF : 746.824.890-70 (os 3 primeiros digitos gera o penultimo digito, enquanto os outros 6 gera o ultimo digito)
Colete a soma dos 9 primeiro dígitos do CPF multiplicando cada um dos valores por uma contagem regressiva começando de 10

EX.: 746.824.890-70 (74682489070)
    10  9   8   7   6   5   4   3   2
 *   
    7   4   6   8   2   4   8   9   0
 =    
    70  36  48  56  12  20  32  27  0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
Contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

# 1 - Informa o CPF como string para permitir fatiamento
cpf = '74682489070'   

# 2 - Separa apenas os 9 primeiros dígitos do CPF
nove_digitos = cpf[:9]  

# 3 - Inicializa o contador regressivo que será usado nas multiplicações
contador_regressivo_1 = 10

# 4 - Inicializa o acumulador que guardará a soma dos resultados
resultado_digito_1 = 0

# 5 - Percorre cada dígito dos 9 dígitos do cpf
for digito in nove_digitos:
    # 6 - Converte o dígito para inteiro e multiplica pelo contador atual
    resultado_digito_1 += int(digito) * contador_regressivo_1
    # 7 - Decrementa o contador para a próxima multiplicação
    contador_regressivo_1 -= 1

# 8 - Multiplica o resultado total da soma por 10
digito_1 = (resultado_digito_1 * 10) % 11

# 9 - Calcula o resto da divisão por 11
#     Se o resultado for maior que 9, o dígito final é 0
digito_1 = digito_1 if digito_1 <= 9 else 0

# 10 - Exibe o primeiro dígito verificador
print(digito_1)