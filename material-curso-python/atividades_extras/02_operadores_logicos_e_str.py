# 1 - Crie uma variável com uma palavra e mostre essa palavra repetida 3 vezes usando o operador *.
palavra = "Axel" * 3
print(palavra)

# 2 - Receba três valores como string (sem usar input, apenas declare).
# Converta para float e mostre a soma.
valor1 = '10'
valor2 = '5.5'
valor3 = '3.2'

soma = float(valor1) + float(valor2) + float(valor3)
print(soma)

# 3 - Crie as variáveis:
# idade = 22
# tem_carteira = True
# Crie a variável pode_dirigir que só será True se idade ≥ 18 e tem_carteira for True.
idade = 22
tem_carteira = True
pode_dirigir = idade >= 18 and tem_carteira
print(pode_dirigir)

# 4 - Dada uma frase, exiba o caractere presente na posição 4 da string
frase = "Aprendendo Python"
print(frase[4]) 


# 5 - Calcule: (10 + 2) ** 2 / 4 + 3 * 2 - 5 e mostre o resultado.
print((10 + 2) ** 2 / 4 + 3 * 2 - 5)

# 6 - Crie duas strings com nomes diferentes. Exiba True se forem iguais e False caso contrário.
a = "Axel"
b = "Axel"
print(a == b)

""" 7 - Usando:
nota1 = 8
peso1 = 2
nota2 = 6
peso2 = 3
Calcule a média ponderada usando operadores aritméticos."""

nota1 = 8
peso1 = 2
nota2 = 6
peso2 = 3

media = (nota1 * peso1 + nota2 * peso2) / (nota1 + nota2)

print(media)

# 8 - Dada a string "Programação Python", exiba somente "Python" usando slice.
frase = "Programação Python"
print(frase[12:])

"""9 - Crie:
produto = "Café"
preco = 7.5
quantidade = 3
Mostre a frase:
"Você comprou 3 unidades de Café. Total: R$ 22.50"
Use coerção e operadores aritméticos."""

produto = "Café"
preco = 7.5
quantidade = 3

total = preco * quantidade
print("Você comprou" + str(quantidade) + "unidades de" + produto + ". Total: R$" + f"{total:.2f}")

"""10 - Crie:
x = 10
y = 20
z = 5
Exiba o resultado da expressão booleana:
(x < y) or (z > y and x == 10)"""
x = 10
y = 20
z = 5
resultado = (x < y) or (z > y and x == 10)

print(resultado)