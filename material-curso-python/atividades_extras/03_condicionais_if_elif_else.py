"""
1. Maioridade
Peça a idade do usuário usando input() e diga:
"Maior de idade" se for ≥ 18
"Menor de idade" caso contrário
Use format() para exibir a mensagem.
"""
idade_usuario = input('Digite sua idade: ')

if idade_usuario >= "18":
   print('Resultado: {}'.format('maior de idade'))

else:
   print('Resultado: {}'.format('menor de idade'))

print("-------------------------------------------------------------------------------------------------------------")
"""
2. Comparação de nomes
Peça dois nomes.
Exiba:
"Os nomes são iguais" se forem iguais
"Os nomes são diferentes" caso contrário
"""
nome_1 = input('Insira o primeiro nome: ')
nome_2 = input('Insira o segundo nome: ')

if nome_1 == nome_2:
    print("Resultado: {}".format("Os nomes são iguais"))
else:
    print("Resultado: {}".format("Os nomes são diferentes"))
print("-------------------------------------------------------------------------------------------------------------")
"""
3. Número positivo, negativo ou zero
Peça um número.
Exiba:
"Número positivo"
"Número negativo"
"Número zero"
"""
numero = input("Insira um número: ")

if numero > "0":
   print("Resultado: {}".format("Número positivo"))
elif numero < "0":
   print("Resultado: {}".format("Número negativo"))
else:
   print("Resultado: {}".format("Número zero"))
print("-------------------------------------------------------------------------------------------------------------")
"""
4. Login simples
Peça um nome de usuário.
Se for "admin", exiba "Acesso permitido", senão "Acesso negado".
"""
usuario = input('Insira o nome do seu usuário: ')

if usuario == "admin":
    print("Resultado: {}".format("Acesso permitido"))
else:
    print("Resultado: {}".format("Acesso negado"))
print("-------------------------------------------------------------------------------------------------------------")
"""
5. Classificação por nota
Peça uma nota (0 a 10).
Exiba:
"Aprovado" se ≥ 6
"Recuperação" se ≥ 4 e < 6
"Reprovado" se < 4
"""
nota = input("Insira a nota")

if nota >= "6":
    print("Resultado: {}".format("Aprovado"))
elif nota >= "4":
    print("Resultado: {}".format("Recuperação"))
else:
    print("Resultado: {}".format("Reprovado"))
print("-------------------------------------------------------------------------------------------------------------")
"""
6. Comparação de idades
Peça duas idades.
Exiba qual idade é maior ou se são iguais.
"""
idade_1 = input('Insira a primeira idade: ')
idade_2 = input('Insira a segunda idade: ')

if idade_1 > idade_2:
    print("Resultado: {}".format("A primeira idade é maior"))
elif idade_2 > idade_1:
    print("Resultado: {}".format("A segunda idade é maior"))
else:
    print("Resultado: {}".format("As idades são iguais"))
print("-------------------------------------------------------------------------------------------------------------")
"""
7. Verificação de senha
Peça uma senha.
Se for "1234", mostre "Senha correta", senão "Senha incorreta".
"""
senha = input('Insira sua senha: ')

if senha == '1234':
    print("Resultado: {}".format("Senha correta"))
else:
    print("Resultado: {}".format("Senha incorreta"))
print("-------------------------------------------------------------------------------------------------------------")
"""
8. Turno escolar
Peça o turno (M, T ou N).
Exiba:
"Bom dia"
"Boa tarde"
"Boa noite"
Ou "Turno inválido".
"""
turno = input('Insira seu turno (M = Matutino, T = Vespertino ou N = Noturno): ')

if turno == "M":
    print("Resultado: {}".format("Bom dia"))
elif turno == "T":
    print("Resultado: {}".format("Boa tarde"))
elif turno == "N":
    print("Resultado: {}".format("Boa noite"))
else:
    print("Resultado: {}".format("Turno inválido"))
print("-------------------------------------------------------------------------------------------------------------")
"""
9. Estado civil
Peça o estado civil (solteiro, casado, divorciado).
Exiba uma mensagem correspondente.
"""
estado_civil = input('Insira seu estado civil: ')

if estado_civil == "solteiro":
    print("Resultado: {}".format("Você é solteiro"))
elif estado_civil == "casado":
    print("Resultado: {}".format("Você é casado"))
elif estado_civil == "divorciado":
    print("Resultado: {}".format("Você é divorciado"))
else:
    print("Resultado: {}".format("Estado civil inválido"))
print("-------------------------------------------------------------------------------------------------------------")
"""
10. Comparação de textos
Peça duas palavras.
Exiba qual delas vem primeiro em ordem alfabética ou se são iguais.
"""
palavra_1 = input('Insira a primeira palavra: ')
palavra_2 = input('Insira a segunda palavra: ')

if palavra_1 < palavra_2:
    print("Resultado: {}".format("A primeira palavra vem primeiro"))
elif palavra_2 < palavra_1:
    print("Resultado: {}".format("A segunda palavra vem primeiro"))
else:
    print("Resultado: {}".format("As palavras são iguais"))
