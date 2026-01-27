"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
# 1. Criar uma função que recebe uma lista com varias listas dentro
def lista(lista_de_listas_de_inteiros):
    resultados = []

    # 2. Percorrer a lista em ordem, do início ao fim
    for listas in lista_de_listas_de_inteiros:
        numeros_repetidos = set()
        duplicado = -1

        # 3. Para cada numero dentro de cada lista
        for numero in listas:

            # 4. Para cada valor:
            # - Verificar se o valor já está no set
            if numero in numeros_repetidos:
                duplicado = numero

                # - Se estiver, retornar esse valor e encerrar a função
                break

            # 5. Adiciona o número ao conjunto de números já vistos
            numeros_repetidos.add(numero)

        # 6. Adiciona o resultado da lista atual à lista de resultados
        resultados.append(duplicado)

    # 7. Retorna a lista com os duplicados encontrados
    return resultados

# LISTA
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

print(lista(lista_de_listas_de_inteiros))

print()


# --------------------------------------------------------------------------------------------------------------
# Resposta do professor

def encontra_primeiro_duplicado(lista_de_inteiros):
    # Criar uma estrutura para armazenar os valores já encontrados,
    # permitindo consulta rápida para saber se um valor já apareceu
    numeros_checados = set()

    # Definir um valor padrão que será retornado caso nenhuma duplicação seja encontrada
    primeiro_duplicado = -1

    # Percorrer a lista sequencialmente, respeitando a ordem original dos dados
    for numero in lista_de_inteiros:

        # Verificar se o valor atual já foi processado anteriormente
        if numero in numeros_checados:

            # Se o valor já existir, significa que esta é a segunda ocorrência,
            # portanto este valor é considerado o primeiro duplicado
            primeiro_duplicado = numero

            # Encerrar o processamento imediatamente, pois o primeiro duplicado já foi encontrado
            break
        
        # Caso o valor ainda não tenha sido encontrado,
        # armazená-lo para futuras comparações
        numeros_checados.add(numero)

    # Retornar o valor do primeiro número duplicado encontrado
    # ou -1 se nenhuma duplicação existir
    return primeiro_duplicado

# Percorrer cada sublista existente na lista principal
for lista in lista_de_listas_de_inteiros:
    # Para cada sublista, executar a função de busca do primeiro duplicado
    # e exibir o resultado correspondente
    print(
        lista,
        encontra_primeiro_duplicado(lista)
    )