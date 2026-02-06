"""
🧩 Exercício 1 — Dict comprehension básico
Crie um novo dicionário:

Regras:
- Strings em MAIÚSCULO
- Não incluir a chave 'senha'

usuario = {
    'nome': 'wonwoo',
    'idade': 25,
    'senha': '123',
}
"""
# 1 - Dicionário original
usuario = {
    'nome': 'wonwoo',
    'idade': 27,
    'senha': '123',
}

# 2 - Novo dicionário usando comprehension
usuario_dict = {
    # 3 - Verifica se o valor é string, se for transforma em MAIÚSCULO
    chave: valor.upper() if isinstance(valor, str) else valor 
    # 4 - Percore chave e valor com items()
    for chave, valor in usuario.items()
    # 5 - Ignora a chave senha
    if chave != 'senha'
}

print(usuario_dict)

# ------------------------------------------------------------------------------------

"""
🧩 Exercício 2 — Dict a partir de lista
Use dictionary comprehension para transformar:

dados = [('a', 1), ('b', 2), ('c', 3)]

em um dicionário.
"""
# 1 - Lista de tuplas
dados = [('a', 1), ('b', 2), ('c', 3)]

# 2 - Transformando em dicionário
dados_dict = {
    # 3 - Cada tupla vira chave e valor
    chave: valor 
    # 4 - Desempacota a tupla
    for chave, valor in dados
}

print(dados_dict)

# ------------------------------------------------------------------------------------

"""
🧩 Exercício 3 — Set comprehension
Crie um set usando comprehension:

Regras:
- range(10)
- Apenas números pares
- Cada número elevado ao quadrado
"""
# 1 - Eleva ao quadrado apenas números pares
s1 = {
    i ** 2
    # 2 - Percorre todo o range até o número 9                      
    for i in range(10) 
    # 3 - Filtra apenas pares
    if i % 2 == 0
}

print(s1)

# ------------------------------------------------------------------------------------

"""
🧩 Exercício 4 — isinstance avançado
Percorra a lista:

dados = ['Python', 10, 2.5, [1,2], {'a':1}, (1,2), {1,2}]

Regras:
- str → print em upper()
- int/float → multiplicar por 3
- list/tuple/set → print tamanho
- dict → print apenas chaves
"""
# 1 - Lista
dados = ['Python', 10, 2.5, [1,2], {'a':1}, (1,2), {1,2}]

# 2 - Percore todos os items da lista
for item in dados:
    
    # 3 - Verifica se é string
    if isinstance(item, str):
        # 3.1 Se for string, transforma em maiúsculo
        print(item.upper())
    
    # 4 - Verifica se é int ou float
    elif isinstance(item, (int, float)):
        # 4.1 - Se for int ou float, multiplica por 3
        print(item * 3)
    
    # 5 - Verifica se é uma lista, tupla ou set
    elif isinstance(item, (list, tuple, set)):
        # 5.1 - Se for uma lista, tupla ou set, retorna o tamanho dela
        print(len(item))
    
    # 6 - Verifica se é um dicionario
    elif isinstance(item, dict):
        # 6.1 - Se for um dicionario, retornar a chave
        print(item.keys())

# ------------------------------------------------------------------------------------

"""
🧩 Exercício 5 — Truthy e Falsy real
Crie uma função validar(valor):

- Se for falsy → retornar 'Valor vazio'
- Se for truthy → retornar 'Valor ok'

Teste com:
['', [], {}, 0, None, 'oi', [1]]
"""
# 1 - Variaveis mutáveis
lista = []
dicionario = {}
lista_2 = [2]

# 2 - Variaveis imutáveis
string = ''
inteiro = 0
nada = None
string_2 = 'oi'

# 3 - Função que irá verificar se um valor é truthy ou falsy
def validar(valor):
    # 4 - Retorna falsy se não tiver valor, caso tenha valor retorna truthy
    return 'Valor vazio' if not valor else 'Valor ok'

print(f'{lista= }', validar(lista))
print(f'{dicionario= }', validar(dicionario))
print(f'{lista_2= }', validar(lista_2))
print(f'{string= }', validar(string))
print(f'{inteiro= }', validar(inteiro))
print(f'{nada= }', validar(nada))
print(f'{string_2= }', validar(string_2))

# ------------------------------------------------------------------------------------

"""
🧩 Exercício 6 — getattr dinâmico
texto = 'python'

metodos = ['upper', 'capitalize', 'swapcase', 'inexistente']

Percorra a lista:
- Se o método existir → execute
- Senão → print('Método inválido')
"""
# 1 - String com a palavra
string = 'python'

# 2 - Lista com métodos
metodos = ['upper', 'capitalize', 'swapcase', 'inexistente']

# 3 - Percorre todos os itens dentro de metodos
for item in metodos:
    # 4 - Se o método existe dentro da string
    if hasattr(string, item):
        # 5 - Executa o método retornado
        print(getattr(string, item)())
    # 6 - Se não existe o método retorna    
    else:
        print('Não existe o método', item)

# ------------------------------------------------------------------------------------

"""
🧩 Exercício 7 — Iterator vs Generator (🔥)

Crie:

lista = [0..9]
iterator = iter(lista)
generator = (n for n in lista)

Faça:

1) Mostre type() dos três
2) Use next() duas vezes no iterator
3) Percorra o generator com for
4) Tente usar next() no generator depois do for
   (observe o comportamento)
"""

lista = range(10)
iterator = iter(lista)
generator = (n for n in lista)

print(type(lista))
print(type(iterator))
print(type(generator))

print()

print(next(iterator))
print(next(iterator))

print()

for valor in generator:
    print(valor)

print()

print(next(generator))