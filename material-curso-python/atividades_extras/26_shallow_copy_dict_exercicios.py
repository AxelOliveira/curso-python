"""
🧩 Exercício 1 — Criando e acessando dicionário (básico)
Crie um dicionário chamado carro com as chaves:
- marca
- modelo
- ano
Depois:
1-Imprima o valor da chave marca
2-Imprima o valor da chave modelo
3-Use um for para imprimir todas as chaves e valores
"""
# 1 - Dicionário na onde tem as chaves e os valores de cada um
carro = {
    'marca': 'Volkswagen',
    'modelo': 'Jetta',
    'ano': 2025
}

# 2 - Impressão do valor da chave marca
print(carro['marca'])

# 3 - Impressão do valor da chave modelo
print(carro['modelo'])

print()

# 4 - For irá percorrer todo o dicionário e irá imprimir todas as chaves e seus valores
for chave in carro:
    print(chave, carro[chave])

#-----------------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 2 — Alterando e removendo valores
Crie um dicionário chamado usuario com:
- nome
- idade
Depois:
1-Altere o valor da idade
2-Remova a chave idade usando pop
3-Imprima o dicionário final
"""
# 1 - Dicionário na onde tem as chaves e os valores de cada um
usuario = {
    'nome': 'Wonwoo',
    'idade': 27,
}

# 2 - alterar o valor da idade
usuario['idade'] = 32

# 3 - removendo a chave idade usando pop
idade = usuario.pop('idade')

# 4 - Impressão do dicionário final
print(usuario)

#-----------------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 3 — Verificando existência de chave
Crie um dicionário chamado produto com:
- nome
- preco
Depois:
1-Use get para tentar acessar a chave estoque
2-Se não existir, imprima: "Estoque não informado"
3-Se existir, imprima o valor do estoque
"""
# 1 - Dicionário na onde tem as chaves e os valores de cada um
produto = {
    'nome': 'chocolate',
    'preco': 2.78,
}

# 2 - Tentar obter o valor da chave estoque e retornar "Estoque não informado", caso não exista a chave 'estoque'
print(produto.get('estoque', 'Estoque não informado'))

#-----------------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 4 — Percorrendo dicionário
Crie um dicionário chamado aluno com:
- nome
- nota1
- nota2
Depois:
1-Use for para percorrer apenas os valores
2-Use outro for para percorrer chaves e valores juntos
"""
# 1 - Dicionário na onde tem as chaves e os valores de cada um
aluno = {
    'nome': 'Wonwoo',
    'nota1': 10,
    'nota2': 7,
}

# 2 - For percorre as chaves e imprime apenas os valores do dicionário
for valor in aluno:
    print(aluno[valor])

print()

# 3 - For irá percorrer chaves e valores
for chave, valor in aluno.items():
    print(chave, valor)
    
#-----------------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 5 — Shallow copy na prática
Crie um dicionário chamado dados com:
- nome
- valores → uma lista com 3 números
Depois:
1-Crie uma cópia usando .copy()
2-Altere um número dentro da lista da cópia
3-Imprima o dicionário original e a cópia
4-Observe o que aconteceu com o original
✍️ Escreva um comentário explicando o que aconteceu.
"""
# 1 - Dicionário na onde tem as chaves e a lista e os valores de cada um
dados = {
    'nome': 'Wonwoo',
    'valores': [5, 9, 8],
}

# 2 - Criando uma cópia usando .copy()
dados_copy = dados.copy()

# 3 - Alterando um número dentro da lista da cópia
dados_copy['valores'][2] = 85

# 4 - Imprimir o dicionário original e a cópia
print(dados)
print(dados_copy)

# 5 - Escrever o que aconteceu com a original
# R = A lista original foi alterada também, pois a cópia feita com .copy() é uma shallow copy. Objetos mutáveis (como listas) continuam apontando para o mesmo endereço de memória.