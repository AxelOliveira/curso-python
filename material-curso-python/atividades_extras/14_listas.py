"""
🧩 Exercício 1 — criando e acessando lista
Crie uma lista com 5 valores diferentes (tipos mistos).
Depois:
- imprima a lista inteira
- imprima o primeiro elemento
- imprima o último elemento usando índice negativo
🎯 Treinar:
- criação de lista
- índices positivos e negativos
"""
# 1 - Criação da lista
lista = [1, 'Axel', 1.2, True, -27]

# 2 - Impressão dos valores
print(lista)
print(lista[0])
print(lista[-1])

# ---------------------------------------------------------------------------------------

"""
🧩 Exercício 2 — alterando valor por índice
Dada a lista:
lista = [10, 20, 30, 40]
Altere:
- o valor 20 para 200
- o valor 40 para 400
Depois imprima a lista.
🎯 Treinar:
- mutabilidade
- atualização por índice
"""
# 1 - Criação da lista
lista = [10, 20, 30, 40]

# 2 - Alteração dos indices da lista
lista[1] = 200                              # Alteração do indice 1 para 200
lista[3] = 400                              # Alteração do indice 3 para 400

# 3 - Impressão dos valores
print(lista)

# ---------------------------------------------------------------------------------------

"""
🧩 Exercício 3 — usando append
Crie uma lista vazia.
Depois:
- adicione 3 valores usando append
- imprima a lista final
🎯 Treinar:
- append
- lista vazia
"""
# 1 - Criação da lista vazia
lista = []

# 2 - Adição de indices dentro da lista
lista.append(27)
lista.append('Axel')
lista.append(2.58)

# 3 - Impressão dos valores
print(lista)

# ---------------------------------------------------------------------------------------

"""
🧩 Exercício 4 — usando pop
Dada a lista:
- lista = [5, 10, 15, 20]
Faça:
- remova o último elemento usando pop
- guarde esse valor em uma variável
- imprima a lista
- imprima o valor removido
🎯 Treinar:
- pop
- retorno do método
"""
# 1 - Criação da lista
lista = [5, 10, 15, 20]

# 2 - Remoção do ultimo indice e guardando em um variável
ultimo_valor = lista.pop(-1)

# 3 - Impressão dos valores
print(lista)
print(ultimo_valor)

# ---------------------------------------------------------------------------------------

"""
🧩 Exercício 5 — pop com índice
Dada a lista:
- lista = ['a', 'b', 'c', 'd']
Faça:
- remova o elemento 'c' usando pop
- imprima a lista final
🎯 Treinar:
- pop(indice)
- controle de índice
"""
# 1 - Criação da lista
lista = ['a', 'b', 'c', 'd']

# 2 - Remoção do segundo indice
lista.pop(2)

# 3 - Impressão dos valores
print(lista)

# ---------------------------------------------------------------------------------------

"""
🧩 Exercício 6 — del em índice específico
Dada a lista:
- lista = [100, 200, 300, 400, 500]
Faça:
- apague o valor 300 usando del
- imprima a lista
🎯 Treinar:
- del
- remoção sem retorno
"""
# 1 - Criação da lista
lista = [100, 200, 300, 400, 500]

# 2 - Remoção do segundo indice
del lista[2]

# 3 - Impressão dos valores
print(lista)

# ---------------------------------------------------------------------------------------

"""
🧩 Exercício 7 — insert
Dada a lista:
- lista = [1, 2, 3, 4]
Faça:
- insira o número 99 na posição 1
- imprima a lista
🎯 Treinar:
- insert
- deslocamento de índices
"""
# 1 - Criação da lista
lista = [1, 2, 3, 4]

# 2 - Inclusão do valor no primeiro indice
lista.insert(1, 99)

# 3 - Impressão dos valores
print(lista)

# ---------------------------------------------------------------------------------------

"""
🧩 Exercício 8 — extend vs +
Crie duas listas:
- lista_a = [1, 2, 3]
- lista_b = [4, 5, 6]
Faça:
- crie uma terceira lista usando +
- estenda lista_a usando extend
- imprima todas as listas
🎯 Treinar:
- concatenação
- extensão
- diferença de comportamento
"""
# 1 - Criação das duas listas
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

# 2 - Concatenação das duas listas
lista_c = lista_a + lista_b
lista_a.extend(lista_b)

# 3 - Impressão dos valores
print(lista_a)
print(lista_b)
print(lista_c)

# ---------------------------------------------------------------------------------------

"""
🧩 Exercício 9 — cuidado com mutabilidade
Crie uma lista:
- lista_a = ['Python', 'Java', 'C']
Faça:
- crie lista_b usando =
- altere o primeiro valor de lista_a
- imprima lista_a e lista_b
🎯 Treinar:
- referência na memória
- efeito colateral
"""
# 1 - Criação das duas listas
lista_a = ['Python', 'Java', 'C']
lista_b = lista_a

# 2 - Troca do valor do primeiro indice
lista_a[0] = "Axel"

# 3 - Impressão dos valores
print(lista_a)
print(lista_b)

# ---------------------------------------------------------------------------------------

"""
🧩 Exercício 10 — copy
Use a lista:
- lista_a = ['Luiz', 'Maria', 'João']
Faça:
- crie lista_b usando .copy()
- altere um valor de lista_a
- imprima as duas listas
🎯 Treinar:
- cópia de listas
- independência de valores
"""
# 1 - Criação das duas listas
lista_a = ['Luiz', 'Maria', 'João']
lista_b = lista_a.copy()

# 2 - Troca do valor do primeiro indice
lista_a[0] = 'Axel'

# 3 - Impressão dos valores
print(lista_a)
print(lista_b)