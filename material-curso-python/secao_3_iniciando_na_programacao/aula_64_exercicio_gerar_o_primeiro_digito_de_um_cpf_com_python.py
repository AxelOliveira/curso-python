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


cpf = '74682489070'                      
nove_digitos = cpf[:9]                      # Fatiamento do cpf para ficar com 9 digitos
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)
# 1 - Informo cpf
# 2 - faço a multiplicação
# 3 - coleto o resultado da multiplicação e faço a soma
# 4 - multiplico o resultado da soma por 10
# 5 - faço a divisão do resultado da segunda multiplicação por 11 e obtenho o resto da divisao
# 6 - Verifico se o resultado é maior que 9 ou não

