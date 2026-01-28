"""
🟢 FUNDAMENTOS INICIAIS
📄 01_print_variaveis_tipos_basicos
🧩 Exercício
Crie variáveis para:
- nome (string)
- idade (int)
- altura (float)
- maior_de_idade (bool)
Imprima todas em uma única frase formatada.
🎯 Tipos primitivos e saída de dados
"""
# 1 - Criação de variáveis com tipos primitivos
nome = 'Wonwoo'
idade = 18
altura = 1.82
maior_de_idade = idade >= 18

# 2 - Retorno da frase com os valores das váriaveis e com formatação
print(f'Seu nome é {nome}, você tem {idade} anos, sua altura é {altura} metros. Maior de idade? {maior_de_idade}')

#-----------------------------------------------------------------------------------------------------------------

"""
📄 02_operadores_aritmeticos_e_precedencia
🧩 Exercício
Crie um código que calcule:
- soma
- subtração
- multiplicação
- divisão
- potência
Usando precedência correta de operadores.
🎯 Ordem de execução matemática
"""
# 1 - Expressão matemática utilizando operadores e precedência
soma = 31 + 7
subtracao = soma - 44
multiplicacao = subtracao * 19
divisao = multiplicacao / 52
potencia = divisao ** 13

# 2 - Exibição do resultado respeitando a precedência dos operadores
print(potencia)

#-----------------------------------------------------------------------------------------------------------------

"""
📄 03_condicionais_if_elif_else
🧩 Exercício
Receba um número e informe:
- se é par ou ímpar
- se é maior, menor ou igual a 50
🎯 Tomada de decisão
"""
# 1 - Recebe o valor do usúario e converte para inteiro
numero_usuario = int(input('Digite um número: '))

# 2 - Se o número do usuario for divido por 2 e não sobrar, esse número é par
if numero_usuario % 2 == 0:
    # 2.1 - Retorna que o número é par
    print(f'O número {numero_usuario} é par')
# 3 - Se o número do usuario for divido por e sobrar algo, esse número é ímpar    
else:
    # 3. - Retorna que o número é ímpar
    print(f'O número {numero_usuario} é ímpar')

# 4 - Verificação da relação com o número 50
if numero_usuario > 50:
    print('O número é maior que 50')
elif numero_usuario < 50:
    print('O número é menor que 50')
else:
    print('O número é igual a 50')
    
#-----------------------------------------------------------------------------------------------------------------

"""
📄 04_operadores_logicos_e_relacionais
🧩 Exercício
Crie um sistema que:
- verifique se a pessoa pode entrar (idade ≥ 18 e documento válido)
🎯 AND / OR / NOT
"""
documento_valido = True

# 1 - Entrada do usuario com a idade e conversão para um número inteiro
idade_usuario = int(input('Digite sua idade: '))

# 2 - Verificação se é maior de idade e se o documento é válido
if idade_usuario >= 18 and documento_valido == True:
    # 2.1 - Retorna que o usuario foi autorizado
    print('Usuario autorizado, pode entrar')
# 3 - Verifica se o usuario é maior de idade ou se o documento não é válido
elif idade_usuario >= 18 and not documento_valido == False:
    # 3.1 - Retorna que o usuario não foi autorizado
    print('Usuario não autorizado, pois o documento não é válido')
# 4 - Verifica se o usuario é menor de idade e se o documento é válido    
elif idade_usuario <= 18 and documento_valido == True:
    # 4.1 - Retorna que o usuario não foi autorizado
    print('Usuario não autorizado, pois o usuario é menor de idade')
# 5 - Verifica se o usuario é menor de idada e se o documento é inválido
else:
    # 5.1 - Retorna que o usuario nao foi autorizado
    print('Usuario não autorizado, pois o usuario é menor de idade e o documento não é válido')
    
#-----------------------------------------------------------------------------------------------------------------

"""
🟢 STRINGS
📄 05_strings_indices_fatiamento_len
🧩 Exercício
Receba uma frase e:
- imprima o primeiro caractere
- o último caractere
- o tamanho da frase
🎯 Índices e fatiamento
"""
# 1 - Recebe a frase do usuario
frase_usuario = input('Digite uma frase: ')

# 2 - Retorna ao usuario o primeiro caractere da frase
print(f'O primeiro caractere da frase é: {frase_usuario[0]}')
# 3 - Retorna ao usuario o ultimo caractere
print(f'O último caractere da frase é: {frase_usuario[-1]}')
# 4 - Retorna ao usuario o tamanho da frase
print(f'O tamnho da frase é: {len(frase_usuario)}')
    
#-----------------------------------------------------------------------------------------------------------------

"""
📄 06_strings_metodos_upper_lower_replace
🧩 Exercício
Receba um texto e:
- transforme em maiúsculo
- substitua uma palavra específica
🎯 Manipulação de strings
"""
# 1 - Recebe a frase do usuario
texto_usuario = input('Digite um texto: ')

# 2 - Altera todas as letras do texto para maiúsculo
maiusculo = texto_usuario.upper()
print(maiusculo)

print()

# 3 - Substituição de uma palavra específica
palavra_antiga = input('Digite a palavra que deseja substituir: ')
palavra_nova = input('Digite a nova palavra: ')

print(texto_usuario.replace(palavra_antiga, palavra_nova))
#-----------------------------------------------------------------------------------------------------------------

"""
📄 07_strings_split_join
🧩 Exercício
Receba uma frase:
- transforme em lista com split
- una novamente com join usando -
🎯 Conversão string ↔ lista
"""
# 1 - Recebe uma frase do usuario
frase_usuario = input('Digite uma frase: ')

# 2 - Transforma a frase em lista
lista_frase = frase_usuario.split(' ')
print(lista_frase)

print()

# 3 - Junta a frase utilizando "-" para cada caractere
frase_unidas = '-'.join(frase_usuario)
print(frase_unidas)
   
#-----------------------------------------------------------------------------------------------------------------

"""
🟢 LISTAS
📄 08_listas_criacao_indices_append_pop
🧩 Exercício
Crie uma lista de números:
- adicione 2 números
- remova o último
- imprima a lista final
🎯 Manipulação básica de listas
"""
# 1 - Lista inicial de números 
lista_numeros = [15, 72, 4, 89, 33, 57, 21, 66]

# 2 - Inclusão de mais um número na lista
lista_numeros.append(18)

# 3 - Inclusão de mais um número na lista
lista_numeros.append(91)

# 4 - Remoção do último número da lista
lista_numeros.pop()
print(lista_numeros)
   
#-----------------------------------------------------------------------------------------------------------------

"""
📄 09_listas_for_iteracao
🧩 Exercício
Percorra uma lista de nomes e imprima cada um.
🎯 Iteração com for
"""
# 1 - Lista de nomes
lista_nomes = ['Wonwoo', 'Vernon', 'Mingyu', 'San', 'Jaemin']

# 2 - Para cada nome na lista, imprima nome por nome
for nome in lista_nomes:
    print(nome)
   
#-----------------------------------------------------------------------------------------------------------------

"""
📄 10_listas_aninhadas
🧩 Exercício
Crie uma lista de listas com números e:
- imprima todos os valores usando dois for
🎯 Laços aninhados
"""
# 1 - Lista com outras listas dentro da principal
lista_numeros = [
    [3, 27, 44, 12, 38],
    [7, 19, 50, 23, 41],
]

# 2 - Percorre a lista principal
for sublista in lista_numeros:
    # 3 - Percorre as listas dentro da lista principal
    for numero in sublista:
        print(numero)
   
#-----------------------------------------------------------------------------------------------------------------

"""
🟢 TUPLAS E SETS
📄 11_tuplas_imutabilidade
🧩 Exercício
Crie uma tupla e:
- tente alterar um valor
- explique o erro em comentário
🎯 Conceito de imutabilidade
"""
# 1 - Criação da tupla com os nomes
tupla_nomes = ('Wonwoo', 'Vernon', 'Jaemin', 'Jeno', 'San')

# 2 - Tentativa de incluir um valor na tupla
tupla_nomes.append('Mingyu')

# Não é possível alterar ou adicionar algum valor novo na tupla, pois ela é imutavel
print(tupla_nomes)
   
#-----------------------------------------------------------------------------------------------------------------

"""
📄 12_sets_criacao_e_remocao
🧩 Exercício
Crie um set:
- adicione valores duplicados
- imprima o resultado
🎯 Valores únicos
"""
# 1 - Criação da lista com o números e alguns duplicados
numeros = [14, 7, 22, 7, 30, 14, 18, 5, 22, 9]

# 2 - Passando a lista para o set que irá remover automaticamente os repetidos
n1 = set(numeros)

print(n1)
  
#-----------------------------------------------------------------------------------------------------------------

"""
📄 13_sets_operadores_matematicos
🧩 Exercício
Utilize:
- união
- interseção
- diferença
- diferença simétrica
🎯 Operações matemáticas em sets
"""
# 1 - Criação do set
n1 = {11, 25, 2}
n2 = {17, 2, 28}

# 2 - União dos dois sets (retira repetidos)
n3 = n1 | n2
print('União:', n3)

print()

# 3 - Interseção dos dois sets (mostra somente os repetidos em ambos sets)
n4 = n1 & n2
print('Interseção:', n4)

print()

# 4 - Diferença dos dois sets (mostra somente os números que estão a esquerda)
n5 = n1 - n2
print('Diferença:', n5)

print()

# 5 - Diferença simmétrica dos dois sets (mostra somente os não repetidos em ambos sets)
n6 = n1 ^ n2
print('Diferença simétrica:', n6)
  
#-----------------------------------------------------------------------------------------------------------------

"""
🟢 DICIONÁRIOS
📄 14_dicionarios_criacao_e_acesso
🧩 Exercício
Crie um dicionário com dados de uma pessoa e imprima cada valor.
🎯 Estrutura chave → valor
"""
# 1 - Criação do dicionario com os dados da pessoa
pessoa = {
    'nome': 'Jeon Wonwoo',
    'idade': 29,
    'altura': 1.82,
    'signo': 'bonito',
}

for valor in pessoa.values():
    print(valor)

#-----------------------------------------------------------------------------------------------------------------
 
"""
📄 15_dicionarios_iteracao_items
🧩 Exercício
Percorra um dicionário e imprima:
chave: valor
🎯 Iteração com .items()
"""
# 1 - Criação do dicionario com os dados da pessoa
pessoa = {
    'nome': 'Vernon',
    'idade': 27,
    'altura': 1.82,
    'signo': 'bonito',
}

# 2 - Para cada chave e valor em pessoa ele irá retornar o item
for chave, valor in pessoa.items():
    print(chave, valor)
    
#-----------------------------------------------------------------------------------------------------------------
  
"""
🟢 FUNÇÕES
📄 16_funcoes_definicao_retorno
🧩 Exercício
Crie uma função que receba dois números e retorne a soma.
🎯 Entrada → processamento → saída
"""
# 1 - Criação da função
def soma(a, b):
    # 1.1 - Retorno da função
    return a + b

# 2 - Recebe o primeiro valor do usuario
valor_usuario_1 = int(input('Digite o primeiro número: '))
# 3 - Recebe o segundo valor do usuario
valor_usuario_2 = int(input('Digite o segundo número: '))

# 4 - Passando os valores para a função
resultado = soma(valor_usuario_1, valor_usuario_2)

print(f'O resultado da soma do primeiro valor {valor_usuario_1} com o segundo valor {valor_usuario_2} é {resultado}')
    
#-----------------------------------------------------------------------------------------------------------------
 
"""
📄 17_funcoes_parametros_e_argumentos
🧩 Exercício
Crie uma função que receba nome e idade e exiba uma frase.
🎯 Passagem de dados para funções
"""

"""
📄 18_funcoes_com_args
🧩 Exercício
Crie uma função que receba vários números com *args e retorne a soma.
🎯 Empacotamento
"""

"""
🟢 ESCOPO E LÓGICA
📄 19_escopo_variaveis
🧩 Exercício
Crie uma variável global e uma local e mostre a diferença.
🎯 Escopo de variáveis
"""

"""
📄 20_logica_primeiro_duplicado
🧩 Exercício
Crie uma função que encontre o primeiro número duplicado, considerando a segunda ocorrência.
🎯 Lógica sequencial + controle de fluxo
"""

"""
🟢 LAMBDA, SORT, SORTED
📄 26_lambda_sort_sorted
🧩 Exercício
Ordene uma lista de dicionários:
- por nome
- por preço
  Sem modificar a lista original.
🎯 Funções anônimas + ordenação
"""

"""
📄 27_lambda_retorna_funcao
🧩 Exercício
Crie uma função que:
- receba um número
- retorne outra função que multiplica por esse número
🎯 Closures + lambda
"""

"""
🟢 *ARGS E **KWARGS
📄 28_args_kwargs_empacotamento_dicionarios
🧩 Exercício
Crie uma função que:
- receba *args
- receba **kwargs
- exiba todos os dados corretamente
🎯 Empacotamento e desempacotamento
"""