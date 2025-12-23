"""Crie um programa que:
1️⃣ Peça ao usuário
Nome (string)
Idade (string → converter para int)
Nota 1 (string → converter para float)
Nota 2 (string → converter para float)

2️⃣ Calcule
A média das duas notas
lembre da precedência: (nota1 + nota2) / 2

3️⃣ Verifique
Se a idade é maior ou igual a 18
Se a média é:
≥ 6 → "Aprovado"
≥ 4 e < 6 → "Recuperação"
< 4 → "Reprovado"

4️⃣ Exiba no final

Uma mensagem formatada, usando .format(), no seguinte modelo:
Aluno: NOME
Idade: IDADE
Média: MEDIA
Situação: RESULTADO
Status de idade: Maior de idade / Menor de idade
"""
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
nota1 = input('Digite sua primeira nota: ')
nota2 = input('Digite sua segunda nota: ')

print()

int_idade = int(idade)
float_nota1 = float(nota1)
float_nota2 = float(nota2)

media = (float_nota1 + float_nota2) / 2

print('Aluno: {}'.format(nome))
print('Idade: {}'.format(idade))

if media >= 6:
    situacao = 'Aprovado'
elif media < 4:
    situacao = 'Reprovado'
else:
    situacao = 'Recuperação'

print('Média: {}\nSituação: {}'.format(media, situacao))

if int_idade >= 18:
    print('Status de idade: Maior de idade')
else:
    print('Status de idade: Menor de idade')