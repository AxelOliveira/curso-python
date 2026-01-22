# Metodos geralmente estão dentro dos objetos.

"""
Métodos úteis dos dicionários em Python

len()               -> quantidade de chaves no dicionário
keys()              -> retorna um iterável com as chaves
values()            -> retorna um iterável com os valores
items()             -> retorna um iterável com pares(chave, valor)
setdefault()        -> adiciona um valor caso a chave não exista
copy()              -> retorna uma cópia rasa (shallow copy)
get()               -> obtém o valor de uma chave
pop()               -> remove um item usando a chave
popitem()           -> remove o último item adicionado
update()            -> atualiza um dicionário com outro
"""
pessoa = {
    'nome': 'Jeon',
    'sobrenome': 'Wonwoo',
    'idade': 27,
}

# setdefault só cria a chave se ela NÃO existir
pessoa.setdefault('idade', 0)
print(pessoa['idade'])

print()

# Quantidade de chaves no dicionário
print(len(pessoa))

# Obtendo chaves, valores e itens
print(list(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))

print()

# Percorrendo apenas os valores
for valor in pessoa.values():
    print(valor)

# Percorrendo chaves e valores ao mesmo tempo
for chave, valor in pessoa.items():
    print(chave, valor)