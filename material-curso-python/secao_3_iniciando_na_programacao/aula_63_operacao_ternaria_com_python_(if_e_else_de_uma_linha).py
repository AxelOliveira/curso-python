"""
Operação ternária (condicional de uma linha)
Faz o if e else em uma linha só
<valor> if <condicao> else <outro valor>

Usada quando:
- a decisão é simples
- o código fica mais legível
Não usar quando a lógica for complexa
"""
# condicao = 10 == 11
# variavel = 'Valor' if condicao else 'Outro valor'
# print(variavel)

"""Dois ultimos digitos do cpf"""
digito = 9         
novo_digito = digito if digito <= 9 else 0       # Se o digito for maior que 9 ele vira 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)