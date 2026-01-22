"""
Métodos úteis dos dicionários em Python

get()               -> obtém o valor de uma chave (sem gerar erro)
pop()               -> remove uma chave e retorna seu valor
popitem()           -> remove e retorna o último item adicionado
update()            -> atualiza o dicionário com outro dicionário ou com um iterável de pares (chave, valor)
"""
p1 = {
    'nome': 'Jeon',
    'sobrenome': 'Wonwoo',
}

# Acessando valores
print(p1['nome'])
print(p1.get('nome', 'Não existe'))

print()

# Removendo uma chave específica
nome = p1.pop('nome')
print(nome)
print(p1)

print()

# Removendo o último item inserido
ultima_chave = p1.popitem()
print(ultima_chave)
print(p1)

print()

# Atualizando o dicionário usando outro dicionário
p1.update({
    'nome': 'novo valor',
    'idade': 30,
})

print(p1)

print()

# Atualizando usando argumentos nomeados
p1.update(nome='novo valor', idade=30)

print(p1)

print()

# Atualizando usando iteráveis de pares (chave, valor)
tupla = (('nome', 'novo valor'),('idade', 30))
lista = [['nome', 'novo valor'], ['idade', 30]]

p1.update(tupla)
p1.update(lista)

print(p1)