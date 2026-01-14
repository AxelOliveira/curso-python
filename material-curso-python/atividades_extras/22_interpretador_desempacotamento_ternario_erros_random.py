"""
🧠 Exercício 1 — Interpretador (aula 61)
Crie um arquivo Python que:
1. Imprima uma frase qualquer
2. Imprima o Zen of Python
3. Rode corretamente usando:
    python arquivo.py
    python -c "código_python"
    python -i arquivo.py

📌 Objetivo: entender formas de execução do interpretador.
"""
print('Frase qualquer')

#--------------------------------------------------------------------------------------------------------

"""
🧠 Exercício 2 — Desempacotamento simples (aula 62)
Dada a lista:
dados = ['Ana', 25, 'Brasil']
1. Desempacote os valores em variáveis
2. Imprima uma frase usando essas variáveis
3. Use _ para ignorar algum valor
📌 Objetivo: controle de variáveis no desempacotamento.
"""
# 1 - lista com as informações
dados = ['Ana', 25, 'Brasil']

# 2 - Imprime os dados linha por linha
print(*dados, sep='\n')

# 3 - Faz a identificação dos dados
nome, idade, pais = dados

# 4 - Imprime uma frase com os dados da lista
print(f"O nome dela é {nome}, tem {idade} anos e é do {pais}")

#--------------------------------------------------------------------------------------------------------

"""
🧠 Exercício 3 — Desempacotamento com * (aula 62)
Dada a lista:
numeros = [1, 2, 3, 4, 5, 6]
1. Guarde o primeiro número
2. Guarde o último número
3. Ignore todos os valores do meio usando *
📌 Objetivo: entender coleta flexível de valores.
"""
# 1 - Criação da lista
numeros = [1, 2, 3, 4, 5, 6]

# 2 - Guardando os números nas variáveis
primeiro, *_, ultimo = numeros

# 3 - Imprime somente os dois números guardados
print(primeiro, ultimo)

#--------------------------------------------------------------------------------------------------------

"""
🧠 Exercício 4 — print(*iterável) (aula 62)
Dada a lista:
nomes = ['João', 'Maria', 'Carlos']
1. Imprima os nomes em uma linha
2. Imprima os nomes um por linha, usando apenas print
📌 Objetivo: uso real do * em chamadas de função.
"""
# 1 - Criação da lista
nomes = ['João', 'Maria', 'Carlos']

# 2 - Impressão dos nomes em uma linha
print(*nomes)

# 3 - Impressão dos nomes um por linha, usando apenas print
print(*nomes, sep='\n')

#--------------------------------------------------------------------------------------------------------

"""
🧠 Exercício 5 — Operador ternário básico (aula 63)
Crie uma variável numero.
1. Se o número for par, armazene 'par'
2. Caso contrário, armazene 'ímpar'
3. Faça isso em uma única linha
📌 Objetivo: tomar decisão simples com ternário.
"""
# 1 - Criação da variável
numero = 25

# 2 - Verificação se o número é par ou impar
resultado = 'par' if numero % 2 == 0 else 'ímpar'

# 3 - Impressão do valor
print(resultado)

#--------------------------------------------------------------------------------------------------------

"""
🧠 Exercício 6 — Ternário com validação (aula 63)
Dado um número:
1. Se for maior que 9, transforme em 0
2. Caso contrário, mantenha o valor
3. Use operador ternário
📌 Objetivo: mesma lógica usada no CPF.
"""
# 1 - Variavel informando o número
numero = 2

# 2 - Verifica se o número digitado é maior ou menor que 9
novo_numero = numero if numero <= 9 else 0

print(novo_numero)

#--------------------------------------------------------------------------------------------------------

"""
🧠 Exercício 7 — try / except básico (aula 64)
Peça ao usuário um número:
1. Tente converter para int
2. Se der erro, mostre uma mensagem clara
3. O programa não deve quebrar
📌 Objetivo: entender fluxo normal x fluxo de erro.
"""
# 1 - Pedir número ao usuario 
numero_usuario = input('Insira um número: ')

# 2 - Usa try para tentar converter o número
try:
    numero_int = int(numero_usuario)
    print(f'Número digitado: {numero_int}')

except ValueError:
    # 3 - Caso não seja um número digitado, irá gerar a mensagem ao usuário
    print('Por favor, digite apenas números.')

#--------------------------------------------------------------------------------------------------------

"""
🧠 Exercício 8 — try / except + lógica (aula 65)
Peça dois números ao usuário e:
1. Tente dividir o primeiro pelo segundo
2. Trate:
    valor não numérico
    divisão por zero
3. Mostre o resultado apenas se for válido
📌 Objetivo: múltiplos erros possíveis.
"""
# 1 - Solicita ao usuario o primeiro numero
numero_usuario_1 = input('Insira um número: ')

# 2 - Solicita ao usuario o segundo numero
numero_usuario_2 = input('Insira outro número: ')

# 3 - Faz a conversão dos valores
try:
    num1_int = int(numero_usuario_1)
    num2_int = int(numero_usuario_2)

# 4 - Tenta fazer a divisão
    divisao = num1_int / num2_int
    print(f'Resultado da divisão: {divisao}')

# 5 - Trata erro de valor não numérico
except ValueError:
    print('Digite apenas números')

# 6 - Trata erro de divisão por zero
except ZeroDivisionError:
    print('Não é possível dividir um valor por 0')

#--------------------------------------------------------------------------------------------------------

"""
🧠 Exercício 9 — random + lógica (aula 66)
Crie um programa que:
1. Gere um número aleatório entre 1 e 100
2. Diga se ele é:
    menor que 50
    igual a 50
    maior que 50
3. Use operador ternário pelo menos uma vez
📌 Objetivo: integrar random + decisão.
"""
# 1 - Importar o modulo random
import random

# 2 - Gera um número aletório entre 1 e 100
numero = random.randint(0, 100)

# 3 - Classifica usando ternário encadeado
resultado = (
    'menor que 50' if numero < 50
    else 'igual a 50' if numero == 50
    else 'maior que 50'
)

print(f'Número gerado: {numero}')
print(f'Resultado: {resultado}')

#--------------------------------------------------------------------------------------------------------

"""
🧠 Exercício 10 — Desafio final (todas as aulas)
Crie um programa que:
1. Gere uma lista com 5 números aleatórios
2. Desempacote:
    primeiro número
    último número
3. Some todos os valores
4. Mostre:
    lista completa
    soma
    se a soma é maior ou menor que 100 (ternário)
5. Use try / except em pelo menos um ponto
📌 Objetivo: integrar tudo que você aprendeu.
"""
import random

try:
    # 1 - Gera lista com 5 números aleatórios
    lista = [random.randint(1, 50) for _ in range(5)]

    # 2 - Desempacota primeiro e último valor
    primeiro, *_, ultimo = lista

    # 3 - Soma todos os valores
    soma = sum(lista)

    # 4 - Classifica a soma usando ternário
    resultado = 'maior que 100' if soma > 100 else 'menor ou igual a 100'

    # 5 - Exibe os dados
    print(f'Lista completa: {lista}')
    print(f'Primeiro número: {primeiro}')
    print(f'Último número: {ultimo}')
    print(f'Soma: {soma}')
    print(f'Resultado da soma: {resultado}')

except TypeError:
    print('Erro ao processar os valores da lista')