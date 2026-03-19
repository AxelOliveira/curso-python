"""
Funções recursivas e recursividade
- funções que chamam a si mesmas
- úteis para dividir um problema grande em partes menores

Toda função recursiva deve ter:
- Um problema que possa ser dividido em partes menores
- Um caso recursivo (continua a execução)
- Um caso base (condição de parada)

Exemplo: fatorial
n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
"""
def recursiva(inicio=0, fim=4):

    print(inicio, fim)

    # Caso base: para quando atingir ou ultrapassar o gim
    if inicio >= fim:
        return fim
    
    # Caso recursivo: aproxima do fim incrementando o valor
    inicio += 1
    return recursiva(inicio, fim)


print(recursiva())