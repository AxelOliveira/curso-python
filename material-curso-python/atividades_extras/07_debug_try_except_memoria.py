"""1. Tratamento de erro simples
Crie um programa que:
Peça um número ao usuário
Converta para int
Use try/except para tratar erro caso o usuário digite texto
🔍 Debug:
Coloque breakpoint na linha do int()
Observe o erro no except
""" 
numero = input('Digite um número: ')       # Entrada do usuário (string)

try:
    numero_int = int(numero)               # Conversão para inteiro
    print('Você digitou um número')        # Conversão bem-sucedida
except:
    print('Isso não é um número')          # Erro ao converter texto para int

"""
🧠 2. Divisão segura
Peça dois números.
Divida o primeiro pelo segundo
Use try/except para evitar divisão por zero
🔍 Debug:
Breakpoint antes da divisão
Veja o valor das variáveis no painel Variables
"""
primeiro_num = input('Digite o primeiro número: ') # Entrada do usuário (string)
segundo_num = input('Digite o segundo número: ')   # Entrada do usuário (string)

try:
    primeiro = float(primeiro_num)       # Converte o primeiro valor
    segundo = float(segundo_num)         # Converte o segundo valor

    if segundo != 0:                            # Verifica se o divisor é diferente de zero
        resultado = primeiro / segundo          # Realiza a divisão
        print(f'Resultado: {resultado:.2f}')    # Exibe o resultado formatado
    else: 
        print('Não é possível dividir por zero') # Trata divisão por zero

except ValueError:
    print('Digite apenas números válidos')       # Trata erro de conversão

"""
🧠 3. Múltiplos except
Peça um valor ao usuário e tente:
Converter para int
Fazer 10 / valor
Use:
um except ValueError
um except ZeroDivisionError
🔍 Debug:
Execute com valores diferentes
Veja qual except é acionado
"""
numero_usuario = input('Digite um valor para ser dividido por 10: ')      # Entrada do usuário (string)

try: 
    numero = int(numero_usuario)                                          # Converte o valor
    divisao = 10 / numero                                                 # Faz a divisão de 10 com o valor informado

except ValueError:
    print('Digite apenas números inteiros')                               # Trata erro de conversão

except ZeroDivisionError:
    print('Não é possível dividir por zero')                              # Trata divisão por zero

else:
    print(f'Resultado: {divisao:.2f}')                                   # Exibe o resultado formatado

"""
🧠 4. Constante de sistema
Crie uma constante:
IDADE_MINIMA = 18
Peça a idade do usuário
Compare com a constante
Use try/except para erro de conversão
🔍 Debug:
Breakpoint na comparação
Observe o valor da constante
"""
IDADE_MINIMA = 18                                                # Constante

idade_usuario = input('Digite sua idade: ')                      # Entrada do usuário (string)

try:
    idade = int(idade_usuario)                                   # Converte o valor
    if idade == IDADE_MINIMA:                                    # Compara entrada com a constante
        print('Sua idade é igual à idade mínina')                # Exibe o resultado
    else:
        print('Sua idade é diferente da idade mínima')           # Exibe resultado de diferença entre a entrada e a constante
except ValueError:
    print('Digite apenas números inteiros')                               # Trata erro de conversão

"""
🧠 5. Alteração indevida de constante
Crie uma constante:
PI = 3.14
Faça um cálculo
Depois tente alterar PI
Mostre por que isso não é uma boa prática
🔍 Debug:
Observe o valor de PI antes e depois
Entenda que Python não bloqueia, é convenção
"""
PI = 3.14                                   # Constante (convenção)
print(f'PI antes: {PI}')                    # Debug visual

PI = 5.3                                    # Alteração indevida
print(f'PI depois: {PI}')                   # Debug visual

calculo = 27 * PI                           # Cálculo incorreto
print(f'Resultado: {calculo}')

"""
🧠 6. Identidade de valor na memória (id)
Crie duas variáveis:
a = 10
b = 10
Mostre id(a) e id(b)
Explique o resultado em comentário
🔍 Debug:
Veja o id no painel de variáveis
"""
a = 10
b = 10

print(id(a))     # O Python reutiliza objetos de pequenos inteiros, por isso o id é o mesmo
print(id(b))     # O Python reutiliza objetos de pequenos inteiros, por isso o id é o mesmo
print(a is b)    # is compara identidade na memória

"""
🧠 7. Mudança de valor e memória
Crie:
x = 5
y = x
Altere x
Mostre id(x) e id(y)
Explique o que aconteceu
🔍 Debug:
Step Over (F10) linha por linha
Observe quando o id muda
"""
x = 5
y = x

print(x is y) # True

x = 6

print(x is y) # False

print(id(x)) # x aponta para um novo objeto (6)
print(id(y)) # y continua apontando para o objeto original (5)

"""
🧠 8. Comparação: == vs is
Crie duas variáveis com o mesmo valor.
Compare usando ==
Compare usando is
Explique a diferença em comentário
🔍 Debug:
Veja o valor e o id das variáveis
"""
a = 2000
b = 2000

print(a == b) # True -> compara apenas o valor
print(a is b) # True -> ambos apontam para o mesmo objeto (cache de inteiros)

"""
🧠 9. Complexidade simples (legibilidade)
Crie dois códigos que fazem a mesma coisa:
Um com if aninhado
Outro com variáveis auxiliares (mais limpo)
Compare:
Qual é mais fácil de debugar?
Qual é mais legível?
🔍 Debug:
Debug nos dois
Compare quantidade de passos
"""
idade = int(input('Digite sua idade: '))
nota = float(input('Digite sua nota: '))

# # CÓDIGO 1 - IF ANINHADO (MENOS LEGÍVEL)
# if idade >= 18:
#     if nota >= 6:
#         print('Aprovado e maior de idade')
#     else:
#         print('Reprovado e maior de idade')
# else:
#     if nota >= 6:
#         print('Aprovado e menor de idade')
#     else:
#         print('Reprovado e menor de idade')

# CÓDIGO 2 - VARIÁVEIS AUXILIARES (MAIS LIMPO)
maior_idade = idade >= 18  # Variável auxiliar facilita leitura e debug
aprovado = nota >= 6       # Variável auxiliar facilita leitura e debug

if maior_idade and aprovado:
    print('Reprovado e maior de idade')
elif maior_idade and not aprovado:
    print('Aprovado e menor de idade')
else:
    print('Reprovado e menor de idade')

"""
🧠 10. Try/Except bem usado
Crie um programa que:
Peça idade
Use try/except
Não coloque tudo dentro do try
Apenas a linha que pode dar erro
🔍 Debug:
Veja como o fluxo muda
Observe que código limpo é mais fácil de depurar
"""

idade_usuario = input('Digite sua idade: ') # Entrada do usuário (string)

try:
    idade = int(idade_usuario)              # ÚNICA linha que pode dar erro
except ValueError:
    print('Digite apenas números')

else:
    if idade >= 18:
        print('Maior de idade')
    else:
        print('Menor de idade')  