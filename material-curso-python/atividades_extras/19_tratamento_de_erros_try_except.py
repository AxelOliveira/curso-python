"""
🧩 Exercício 1
Use try / except para:
- tentar dividir dois números
- tratar o erro de divisão por zero
"""
# 1 - Define os valores que serão usados na divisão
a = 0
b = 1

try:
    # 2 - Tenta executar a divisão
    divisao = a / b

    # 3 - Se a divisão funcionar, imprime o resultado
    print(divisao)

except ZeroDivisionError:
    # 4 - Se ocorrer erro de divisão por zero, entra aqui
    # 5 - Exibe uma mensagem informando o erro
    print('Nenhum número pode ser divido por zero')
    
#--------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 2
Use try / except para:
- converter um valor para int
- tratar erro caso não seja possível converter
"""
# 1 - Define um valor que será convertido
num = 'a'

try:
    # 2 - Tenta converter o valor para inteiro
    numero = int(num)

    # 3 - Se a conversão funcionar, imprime o valor convertido
    print('Conversão', numero)

except:
    # 4 - Se a conversào falhar, entra no except
    # 5 - Exibe uma mensagem de erro
    print('Não foi possivel converter')
    
#--------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 3
Crie uma lista.
Use try / except para:
- acessar um índice inválido
- tratar o erro
"""
# 1 - Cria uma lista com alguns valores
lista = ['Axel', 'Wonwoo', 'Vernon']

try:
    # 2 - Tenta acessar um índice que não existe na lista
    print(lista[5])
except IndexError:
    # 3 - O erro de índice inválido é capturado aqui
    # 4 - Exibe uma mensagem informando o problema
    print('índice inválido')
    
#--------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 4
Use try / except para:
- acessar uma chave inexistente em um dicionário
- tratar o erro
"""
# 1 - Cria um dicionário com uma chave válida
dados = {'nome': 'Axel'}

try:
    # 2 - Tenta acessar uma chave que não existe
    print(dados['idade'])
except KeyError:
    # 3 - O erro de chave inexistente é capturado
    # 4 - Exibe uma mensagem informando o erro
    print('Chave inexistente')
    
#--------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 5
Combine try / except com else para:
- executar um código somente se nenhum erro ocorrer
"""
# 1 - Define um valor que será convertido
valor = '10'

try:
    # 2 - Tenta converter o valor para inteiro
    numero = int(valor)
except:
    # 3 - Se ocorrer erro na conversão, entra no except
    print('Erro na conversão')

else:
    # 4 - O else só executa se nenhum erro ocorrer
    # 5 - Exibe o resultado da conversão bem-sucedida
    print('Conversão realizada com sucesso:', numero)