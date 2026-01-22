# Manipulando chaves e valores em dicionários

# Criando um dicionário vazio
pessoa = {}

# Definindo uma chave em uma variável
chave = 'nome'

# Criando e atribuindo valores usando chaves
pessoa[chave] = 'Jeon'
pessoa['sobrenome'] = 'Miranda'

# Acessando o valor através da chave armazenada na variável
print(pessoa[chave])

# Alterando o valor de uma chave existente
pessoa[chave] = 'Vernon'

# Removendo uma chave do dicionário
del pessoa['sobrenome']

# Exibindo o dicionário completo
print(pessoa)

# Acessando diretamente o valor da chave 'nome'
print(pessoa['nome'])

# Verificando se a chave existe usando o método get
# get retorna None caso a chave não exista
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')

else:
    print(pessoa['sobrenome'])