"""Criar um programa que analisa os dados de um usuário e exibe um relatório final formatado.
📌 Requisitos (use tudo que você já aprendeu)
1️⃣ Entrada de dados (input)
Peça ao usuário:
Nome (string)
Idade (string → converter para int)
Palavra-chave (string)
Nota 1 (string → converter para float)
Nota 2 (string → converter para float)

2️⃣ Processamentos
Calcule a média das notas
lembre da precedência: (nota1 + nota2) / 2
Verifique se o usuário é maior de idade (≥ 18)
Verifique se a palavra-chave:
tem mais de 3 caracteres (len)
não contém a palavra "123" (not in)

3️⃣ Condições lógicas
O usuário será considerado APTO se:
for maior de idade AND
média ≥ 6 AND
a palavra-chave for válida
Caso contrário, será NÃO APTO
Use:
and
or
not
in / not in

4️⃣ Exibição final (formatação)
Mostre no terminal exatamente nesse modelo, usando f-string OU .format():

Nome: X
Idade: Y
Média: Z
Situação: Aprovado / Recuperação / Reprovado
Palavra-chave válida: True / False
Status final: APTO / NÃO APTO"""
nome = input('Insira seu nome: ')
idade = input('Insira sua idade: ')
palavra_chave = input('Insira a palavra chave: ')
nota_1 = input('Insira a primeira nota: ')
nota_2 = input('Insira a segunda nota: ')

print()

# Conversões
int_idade = int(idade)
float_nota_1 = float(nota_1)
float_nota_2 = float(nota_2)

# Cálculos
media_notas = (float_nota_1 + float_nota_2) / 2

# Verificações
maior_de_idade = int_idade >= 18
media_aprovada = media_notas >= 6
palavra_valida = len(palavra_chave) > 3 and "123" not in palavra_chave

# Situação acadêmica
if media_notas >= 6:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

# Status final
apto = maior_de_idade and media_aprovada and palavra_valida

# Saída
print(f"Nome: {nome}")
print(f"Idade: {int_idade}")
print(f"Média: {media_notas}")
print(f"Situação: {situacao}")
print(f"Palavra-Chave válida: {palavra_valida}")

if apto:
    print("Status final: APTO")
else:
    print("Status final: Não APTO")