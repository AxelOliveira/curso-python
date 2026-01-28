"""
🧩 Exercício 26 — Ordenação com lambda
Enunciado
Você possui uma lista de dicionários representando produtos:
produtos = [
    {'nome': 'Teclado', 'preco': 120},
    {'nome': 'Mouse', 'preco': 80},
    {'nome': 'Monitor', 'preco': 900},
    {'nome': 'Cadeira', 'preco': 700},
]
Crie um código que:
1. Gere uma nova lista ordenada pelo preço (crescente)
2. Gere outra nova lista ordenada pelo nome (ordem alfabética)
3. Não modifique a lista original
4. Use sorted e lambda
Exiba os resultados usando uma função exibir
📌 Dica: use key=lambda produto: produto['preco']
"""
produtos = [
    {'nome': 'Teclado', 'preco': 120},
    {'nome': 'Mouse', 'preco': 80},
    {'nome': 'Monitor', 'preco': 900},
    {'nome': 'Cadeira', 'preco': 700},
]

def exibir(produtos):
    # 1 - Percorre todos os elementos da lista recebida
    for item in produtos:
        print(item)

# Percorre toda a lista, para cada item a função lambda é executada e retorna o valor de item [preco]
preco = sorted(produtos, key=lambda produto: produto['preco'])
exibir(preco)

print()

# Percorre toda a lista, para cada item a função lambda é executada e retorna o valor de item [nome]
nome = sorted(produtos, key=lambda produto: produto['nome'])
exibir(nome)

#-----------------------------------------------------------------------------------------------------------------

"""
🧠 Aula 27 — Funções lambda mais complexas
🧩 Exercício 27 — Função que retorna função
Enunciado
Crie uma função chamada executa que:
- receba uma função como parâmetro
- receba um valor
- retorne o resultado da execução
Em seguida:
1. Use lambda para criar uma função que receba um número m
2. Essa função deve retornar outra função que multiplica qualquer número por m
3. Crie uma função triplica usando esse mecanismo
4. Teste com pelo menos dois valores diferentes
📌 Dica: pense em lambda retornando lambda
"""
def executa(funcao, valor):
    # Executa a fun~c"ao recebida passando o valor informado
    return funcao(valor)

# Lambda recebe me retorna outra função que multiplica por m
triplica = executa(lambda m: lambda n: n * m, 3)

# Teste com dois valores diferentes
print(triplica(2))
print(triplica(5))

#-----------------------------------------------------------------------------------------------------------------

"""
🧠 Aula 28 — Empacotamento e desempacotamento (*args e **kwargs)
🧩 Exercício 28 — Trabalhando com *args e **kwargs
Enunciado
Crie uma função chamada mostra_dados que:
1. Receba qualquer quantidade de argumentos não nomeados (*args)
2. Receba qualquer quantidade de argumentos nomeados (**kwargs)
3. Exiba primeiro todos os argumentos não nomeados
4. Em seguida, exiba os argumentos nomeados no formato:
chave: valor
Depois:
- Crie um dicionário com dados de configuração
- Passe esse dicionário para a função usando **
📌 Dica: percorra kwargs.items()
"""
def mostra_dados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

configuracoes = {
    'tema': 'dark',
    'idioma': 'pt-br',
    'versao': 1.0
}

mostra_dados(1, 2, 3, **configuracoes)