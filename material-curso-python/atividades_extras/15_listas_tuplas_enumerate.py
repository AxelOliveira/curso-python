"""
🧠 Exercícios
🟢 Exercício 1 - for in simples
Crie uma lista com 4 nomes.
Use for in para imprimir cada nome da lista.
"""
# 1 - Criação da lista
lista = ['Axel', 'Wonwoo', 'Vernon', 'Qi shin']

for nome in lista:
    print(nome)

#--------------------------------------------------------------------------------------------------------

"""
🟢 Exercício 2 - Tipo do valor
Usando a mesma lista do exercício anterior, imprima:
- o nome
- o tipo do nome
Exemplo de saída (modelo):
Maria <class 'str'>
"""
# 1 - Criação da lista
lista = ['Axel', 'Wonwoo', 'Vernon', 'Qi shin']

# 2 - Criar uma sequência de índices para percorrer a lista
indices = range(len(lista))                                  # Len retorna a quantidade e range cria os índices

for indice in indices:
    print(lista[indice], type(lista[indice]))

#--------------------------------------------------------------------------------------------------------

"""
🟢 Exercício 3 - Índices com range e len
Crie uma lista com 5 nomes.
Use range(len(lista)) para exibir:
- o índice
- o nome correspondente
"""
# 1 - Criação da lista
lista = ['Axel', 'Wonwoo', 'Vernon', 'Mingyu', 'S.Coups']

# 2 - Cria uma sequência de índices baseada no tamanho da lista
indices = range(len(lista))                                 # Len retorna a quantidade e range cria os índices

for indice in indices:
    print(indice, lista[indice])
    
#--------------------------------------------------------------------------------------------------------

"""
🟡 Exercício 4 - Índice + valor formatado
Usando range(len(lista)), imprima assim:
Índice 0: Maria
Índice 1: Helena
"""
# 1 - Criação da lista
lista = ['Axel', 'Wonwoo', 'Vernon', 'Mingyu', 'S.Coups']

# 2 - Cria uma sequência de índices para acessar os valores da lista
indices = range(len(lista))

for indice in indices:
    print('Índice ', indice, ': ', lista[indice])
    
#--------------------------------------------------------------------------------------------------------

"""
🟡 Exercício 5 - enumerate básico
Crie uma lista com nomes.
Use enumerate para imprimir:
- índice
- nome
"""
# 1 - Criação da lista 
lista = ['Axel', 'Wonwoo', 'Vernon', 'Mingyu', 'S.Coups']

for indice, nome in enumerate(lista):
    print(indice, nome)
    
#--------------------------------------------------------------------------------------------------------

"""
🟡 Exercício 6 - Comparando formas
Faça duas versões do mesmo laço:
1 - usando range(len(lista))
2 - usando enumerate
As duas devem mostrar o mesmo resultado.
"""
# 1 - Criação da lista
lista = ['Axel', 'Wonwoo', 'Vernon', 'Mingyu', 'S.Coups']

# 2 - Cria uma sequência de índices para percorrer a lista
indices = range(len(lista))

for indice in indices:
     print('Índice ', indice, ': ', lista[indice])

print()

for indice, nome in enumerate(lista):
     print(indice, nome)
    
#--------------------------------------------------------------------------------------------------------

"""
🟠 Exercício 7 - Desempacotamento simples
Crie uma lista com 3 nomes.
Use desempacotamento para:
- guardar o primeiro nome em uma variável
- guardar o segundo nome em outra variável
- ignorar o terceiro usando _
Depois, imprima apenas os dois nomes usados.
"""
# 1 - Criação da lista
nome1, nome2, _ = ['Axel', 'Wonwoo', 'Vernon']

# 2 - Impressão dos valores solicitados
print(nome1, nome2)
    
#--------------------------------------------------------------------------------------------------------

"""
🟠 Exercício 8 - *resto no desempacotamento
Crie uma lista com 5 nomes.
Use desempacotamento para:
- guardar o primeiro nome em uma variável
- guardar o restante da lista em resto
Imprima:
- o primeiro nome
- a lista resto
"""
# 1 - Desempacotamento dos valores em variáveis
nome1, *resto = ['Axel', 'Wonwoo', 'Vernon', 'Mingyu', 'S.Coups']

# 2 - Impressão dos valores solicitados
print(nome1)
print()
print(*resto)
    
#--------------------------------------------------------------------------------------------------------

"""
🔵 Exercício 9 - Lista → Tupla
Crie uma lista com nomes.
Converta essa lista para uma tupla.
Use for in para imprimir todos os valores da tupla.
"""
# 1 - Criação da lista
lista = ['Axel', 'Wonwoo', 'Vernon', 'Mingyu', 'S.Coups']                    # Lista

# 2 - Conversão para tupla
nomes = tuple(lista)                                                         # Converte a lista para tupla

# 3 - Laço para percorrer a tupla
for nome in nomes:
    print(nome)
    
#--------------------------------------------------------------------------------------------------------

"""
🔴 Exercício 10 - enumerate + tupla
Crie uma tupla com nomes.
Use enumerate para imprimir:
- Índice 0 -> Maria
- Índice 1 -> Helena
"""
# 1 - Criação da tupla
tupla = 'Axel', 'Wonwoo', 'Vernon', 'Mingyu', 'S.Coups'                  # Tupla

# 2 - Laço para percorrer a tupla com índice e valor
for indice, nome in enumerate(tupla):                                    # Verifica a informação do indice e do nome na tupla
      print('Índice ', indice, '-> ', tupla[indice])                     # Imprime o valor na tela