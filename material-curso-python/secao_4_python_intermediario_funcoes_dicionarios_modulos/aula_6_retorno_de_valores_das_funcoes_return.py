"""
Retorno de valores das funções (return)
Toda função pode executar ações e retornar valores.
A diferença é se ela usa ou não o return

return: devolve um valor e encerra a função
print: apenas mostra algo na tela

Quando o Python encontra um return, a função é encerrada imediatamente
Qualquer código depois do return não será executado

return não mostra nada na tela, ele apenas devolve um valor para quem chamou a função

return pode retornar qualquer tipo de dado
"""

def soma(x, y):
    # Se x for maior que 10, a função é encerrada aqui e retorna uma lista
    if x > 10:
        return [10, 20]
    
    # Se o if não for verdadeiro, a função retorna a soma de x + y
    return x + y

# variavel = soma(1, 2)
# variavel = int('1')

# Aqui estamos chamando a função e guardando o valore retornada em variáveis
soma1 = soma(2, 2)
soma2 = soma(3, 3)

# print mostra na tela o valor que a função retornou
print(soma1)
print(soma2)

# Aqui o x é maior que 10, então o retorno será a lista
print(soma(11, 55))