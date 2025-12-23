# Crie duas variáveis nome e sobrenome como strings.
# Use print() para exibir o nome completo concatenado.
nome = 'Axel'
sobrenome = 'Oliveira'

print(nome + " " + sobrenome)

# Peça ao usuário (input) dois números como string.
# Converta para float e exiba a soma.
num1 = "10"
num2 = "5.5"
soma = float(num1) + float(num2)
print(soma)

# Crie uma variável boolean maior_de_idade que deve ser True se a idade for maior ou igual a 18.
# Use print() para mostrar o resultado.

idade = 27
maior_de_idade = idade >= 18

print(maior_de_idade)

"""Crie três variáveis numéricas e calcule:
soma
subtração
multiplicação
divisão
Mostre tudo com print()."""

a = 2
b = 3
c = 5

print(a + b + c)
print(a - b - c)
print(a * b * c)
print(a / b / c)

"""Calcule e exiba o resultado das expressões:
3 + 5 * 2
(3 + 5) * 2
Explique (em comentário) por que são diferentes."""

resultado1 = 3 + 5 * 2 # = 13 (multiplicação vem antes)
resultado2 = (3 + 5) * 2 # = 16 (parênteses mudam a ordem)
print(resultado1)
print(resultado2)

# Crie um valor float representando um preço.
# Exiba no formato: "O preço é R$ X.XX" usando formatação.
preco = 56.35
print(f"O preço é R$ {preco:.2f}")

"""Crie as variáveis:
idade = 20
texto = " anos"
Use coerção para concatenar o número com a string e exibir "20 anos"."""
idade = 20
texto = " anos"
print(str(idade) + texto)

"""Crie uma variável nota = 7.5.
Crie a variável aprovado que deve ser True se a nota for >= 6.
Exiba: "Aprovado: True"."""
nota = 7.5
aprovado = nota >= 6
print("Aprovado:", aprovado)

"""Crie uma expressão matemática que envolva:
adição
multiplicação
divisão
subtração
E imprima o resultado, mostrando o efeito da precedência.
Ex.: resultado = 10 + 2 * 3 / 2 - 5"""
conta1 = 10 + 2 * 3 / 2 - 5 # = 10 + 6 / 2 - 5 = 10 + 3 - 5 = 8
print(conta1)

"""Crie uma string com uma frase.
Mostre:
o tamanho da frase (len())
a frase em maiúsculas
a frase em minúsculas
os 5 primeiros caracteres"""
frase = "Python é muito legal!"

print(len(frase))            # tamanho
print(frase.upper())         # maiúsculas
print(frase.lower())         # minúsculas
print(frase[:5])             # primeiros 5 caracteres

# ------------------------------------------------------------------------------------------------------------------------------------