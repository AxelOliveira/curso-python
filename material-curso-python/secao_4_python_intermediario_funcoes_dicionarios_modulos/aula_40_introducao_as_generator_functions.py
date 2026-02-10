"""
Introdução às Generator Functions

Generator expression:
- cria um generator "rápido", sem precisar definir uma função
- Ele NÃO guarda todos os valores na memória, gera sob demanda.
    generator = (n for n in range(1000000))


O que é uma generator function?
- É uma função que pode PAUSAR e CONTINUAR a execução.
- Usa a palavra-chave yield.
- Sempre que encontra yield:
    1) devolve um valor
    2) pausa a função
    3) salva o estado interno (variáveis e posição do código)

Todo generator é um iterator:
- aceita __iter()__
- aceita __next()__
- funciona em for
"""

# 1 - Função generator: usa yield para pausar e continuar a execução
def generator(n=0, maximum=10):

    # 2 - Loop infinito (a parada é controlada por condição interna)
    while True:

        # 3 - Entrega o valor atual e pausa a função
        yield n

        # 4 - Quando o next() for chamado novamente, continua daqui
        n += 1

        # 5 - Condição de parada do generator
        #     quando atingir o máximo, encerra com StopIteration
        if n >= maximum:
            return


# 6 - Criação do generator (a função ainda não executou)
gen = generator(maximum=1000000)

# 7 - O for percorre o generator automaticamente usando next()
for n in gen:
    print(n)