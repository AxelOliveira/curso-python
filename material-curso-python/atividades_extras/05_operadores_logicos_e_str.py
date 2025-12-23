"""1. Verificação dupla de idade
Peça a idade do usuário.
Mostre "Acesso permitido" se a idade for maior ou igual a 18 e menor ou igual a 65.
Caso contrário, mostre "Acesso negado".
"""
idade = input('Insira sua idade: ')
int_idade = int(idade)

if int_idade >= 18 and int_idade <= 65:
   print('Acesso permitido')
else:
   print('Acesso negado')
#------------------------------------------------------------------------------------------------------

"""2. Login com duas condições
Peça usuário e senha.
Mostre "Login válido" se:
usuário for "admin" e
senha for "123"
Senão, mostre "Login inválido".
"""
usuario = input('Insira seu usuário: ')
senha = input('Insira sua senha: ')

if usuario == "admin" and senha == "123":
   print('Login válido')
else:
   print('Login inválido')
#------------------------------------------------------------------------------------------------------

"""3. Verificação de palavra proibida
Peça uma frase.
Mostre "Conteúdo impróprio" se a palavra "spam" estiver na frase.
Caso contrário, "Conteúdo permitido".
(use in)"""
frase = input('Insira uma frase: ')

if "spam" in frase:
    print('Conteúdo impróprio')
else:
    print('Conteúdo permitido')
#------------------------------------------------------------------------------------------------------

"""4. Palavra ausente
Peça uma frase.
Mostre "Palavra não encontrada" se "python" não estiver na frase.
(use not in)"""
frase = input('Insira uma frase: ')

if 'python' not in frase:
    print('Palavra não encontrada')
else:
    print('Palavra encontrada')
#------------------------------------------------------------------------------------------------------

"""5. Negação lógica
Peça uma palavra.
Mostre "Palavra inválida" se não tiver mais de 3 caracteres.
(use not e len())"""
palavra = input('Insira uma palavra: ')

if not len(palavra) > 3:
    print('Palavra inválida')
else:
    print('Palavra válida')
#------------------------------------------------------------------------------------------------------

"""6. Fatiamento simples
Peça uma palavra.
Mostre:
os 3 primeiros caracteres
os 3 últimos caracteres"""
palavra = input('Insira uma palavra: ')

print(palavra[:3])
print(palavra[-3:]) # 3 últimos
#------------------------------------------------------------------------------------------------------

"""7. Comparação com or
Peça um dia da semana.
Mostre "Final de semana" se for "sábado" ou "domingo"."""
dia_da_semana = input('Insira um dia da semana: ')

if (dia_da_semana == 'sábado' or dia_da_semana == 'domingo'):
    print('Final de semana')
else:
    print('Dia da semana')
#------------------------------------------------------------------------------------------------------

"""8. Interpolação com %
Peça nome e idade.
Mostre a frase:
Nome: X - Idade: Y
usando apenas %."""
nome = input('Insira seu nome: ')
idade = input('Insira sua idade: ')

int_idade = int(idade)

variavel = 'Nome: %s - Idade: %d' % (nome, int_idade) # aqui foi utilizado o %d para idade
print(variavel)
#------------------------------------------------------------------------------------------------------

"""9. F-string com comprimento
Peça uma palavra.
Mostre:
A palavra "X" tem Y caracteres
usando f-string e len()."""
palavra = input('Insira uma palavra: ')

print(f'A palavra "{palavra}" tem {len(palavra)} caracteres')
#------------------------------------------------------------------------------------------------------

"""10. Verificação composta
Peça uma senha.
Mostre "Senha forte" se:
tiver 8 ou mais caracteres e
não contiver "123"
Senão, "Senha fraca".
(use and, not in, len())"""
senha = input('Insira a senha: ')

if len(senha) >= 8 and "123" not in senha:
    print('Senha forte')
else:
    print('Senha fraca')