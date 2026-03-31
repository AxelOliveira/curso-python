"""
TEORIA - PARÂMETROS MUTÁVEIS EM FUNÇÕES

1. Problema:
    - Valores padrão são criados UMA ÚNICA VEZ (na definição da função)
    - Se for mutável (lista, dict, set), ele será reutilizado

2. Consequência:
    - Dados "vazam" entre chamadas da função
    - Comportamento inesperado

3. Regra de ouro:
    - NUNCA usar mutáveis como valor padrão

4. Solução:
    - usar None como padrão
    - criar o objeto dentro da função

5. Fluxo correto:
    - se lista for None -> cria nova lista
    - senão -> usa a lista passada
"""
def adiciona_clientes(nome, lista=None):

    # 1 - Verifica se não foi passada lista
    if lista is None:
        lista = []     # 2 - Cria nova lista

    # 3 - Adiciona o nome
    lista.append(nome)

    # 4 - Retorna a lista
    return lista

# 5 - Primeira lista
cliente1 = adiciona_clientes('Jeon')

# 6 - Reutilizando a mesma lista
adiciona_clientes('Wonwoo', cliente1)
adiciona_clientes('Vernon', cliente1)

# 7 - Alterando diretamente
cliente1.append('Mingyu')

# 8 - Nova lista independente
cliente2 = adiciona_clientes('The8')
adiciona_clientes('Seungkwan', cliente2)

# 9 - Outra lista independente
cliente3 = adiciona_clientes('Dino')
adiciona_clientes('Chan', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)