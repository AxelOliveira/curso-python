"""
🧠 Exercício 1 — Escopo global vs local (observação)
Leia o código abaixo sem executar e responda:
x = 5
def funcao():
    x = 10
    print(x)
funcao()
print(x)
O que será impresso dentro da função?
O que será impresso fora da função?
A variável x da função é a mesma do escopo global? Explique com suas palavras.
"""
# RESPOSTA

"""
1 - Dentro da função será impresso o valor de 10 que é referente ao X do escopo local
2 - Fora da função será impresso o valor de 5 que é referente ao X do escopo global
3 - Não, porque a variável x criada dentro da função é outra variável, diferente da global
"""

#--------------------------------------------------------------------------------------------------------

"""
🧠 Exercício 2 — Variável local não existe fora
Leia o código e diga se funciona ou não.
Se não funcionar, explique o motivo.
def teste():
    y = 3
    print(y)
teste()
print(y)
"""
# RESPOSTA = Não irá funcionar, pois o y só existe dentro da função teste(), fora da função, y não existe em nenhum escopo

#--------------------------------------------------------------------------------------------------------

"""
🧠 Exercício 3 — Usando global
Observe o código:
contador = 0
def aumentar():
    global contador
    contador = contador + 1
    print(contador)
aumentar()
aumentar()
aumentar()
O código funciona?
O que será impresso em cada chamada?
Por que o uso de global foi necessário?
"""
# RESPOSTA:
# 1 - O código funciona
# 2 - Será impresso (1, 2, 3)
# 3 - O global foi necessário para que a função pudesse modificar a variável contador que está no escopo global.

#--------------------------------------------------------------------------------------------------------

"""
🧠 Exercício 4 — Função dentro de função (call stack)
Leia o código abaixo e descreva a ordem de execução:
x = 1
def funcao_principal():
    print('Início da função principal')

    def funcao_interna():
        print('Dentro da função interna')

    funcao_interna()
    print('Fim da função principal')

print('Início do código')
funcao_principal()
print('Fim do código')

Explique a ordem em que as mensagens aparecem na tela.
"""

# RESPOSTA:
# A ordem em que as mensagens vão aparecer na tela será a seguinte: Início do código > Início da função principal > Dentro da função interna > Fim da função principal > Fim do código

#--------------------------------------------------------------------------------------------------------

"""
🧠 Exercício 5 — Analisando global em funções aninhadas
Observe o código:
x = 10
def funcao_a():
    global x
    x = 20

    def funcao_b():
        global x
        x = 30
        print(x)

    funcao_b()
    print(x)

print(x)
funcao_a()
print(x)

Quais valores de x serão impressos?
Em qual momento o valor de x muda?
Por que x muda mesmo estando dentro de duas funções?
"""

# RESPOSTA

# 1 - Serão impressos os valores de 10, 30, 30, 30
# 2 - O valor de X muda na linha x = 20 e depois para a linha x = 30
# 3 - O valor de x muda porque a palavra global faz com que todas as atribuições alterem a mesma variável global, mesmo estando dentro de funções diferentes.