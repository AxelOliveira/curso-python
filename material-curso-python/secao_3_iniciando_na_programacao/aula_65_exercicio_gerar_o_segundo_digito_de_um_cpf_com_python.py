"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF, MAIS O PRIMEIRO DIGITO, multiplicando cada um dos valores por uma contagem regressiva começando de 11

EX.: 746.824.890-70 (746824890)
    11  10  9   8   7   6   5   4   3   2
  *
    7   4   6   8   2   4   8   9   0   7      <--- PRIMEIRO DIGITO
  =
    77  40  54  64  14  24  40  36  0   14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
Contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
import re
import sys

# cpf_enviado_usuario = '746.824.890-70' \
#     .replace('.', '') \
#     .replace(' ', '') \
#     .replace('-', '')    

# 1 - Solicita ao usuário um CPF, permitindo pontuação   
entrada = input('CPF [746.824.890-70]: ')

# 2 - Remove qualquer caractere que NÃO seja número
#     Isso garante que o CPF fique apenas com dígitos
cpf_enviado_usuario = re.sub(
    r'[^0-9]',
    '',
    entrada
)   

# 3 - Verifica se o cpf é formado por número repetidos
#     Exemplo inválido: 1111111111
entrada_e_sequencial = entrada == entrada[0] * len(entrada)

# 4 - Se for sequencial, encerra o programa imediatamente
if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

# ================= PRIMEIRO DÍGITO =================

# 5 - Separa os 9 primeiros dígitos do CPF
nove_digitos = cpf_enviado_usuario[:9]    

# 6 - Inicializa o contador regressivo do primeiro dígito
contador_regressivo_1 = 10

# 7 - Inicializa o acumulador da soma
resultado_digito_1 = 0

# 8 - Percorre cada dígito multiplicando pelo contador
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

# 9 - Calcula o primeiro dígito verificador
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

# ================= SEGUNDO DÍGITO =================

# 10 - Junta os 9 dígitos com o primeiro dígito calculado
dez_digitos = nove_digitos + str(digito_1)

# 11 - Inicializa o contador regressivo do segundo dígito
contador_regressivo_2 = 11

# 12 - Inicializa o acumulador do segundo cálculo
resultado_digito_2 = 0

# 13 - Percorre os 10 dígitos multiplicando pelo contador
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

# 14 - Calcula o segundo dígito verificador    
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

# ================= VALIDAÇÃO FINAL =================

# 15 - Monta o CPF gerado pelo cálculo
cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

# 16 - Compara o CPF informado com o CPF calculado
if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} é válido')
else:
    print('CPF inválido')