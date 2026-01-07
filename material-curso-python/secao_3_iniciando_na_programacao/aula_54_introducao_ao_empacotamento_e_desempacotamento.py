"""
Introdução ao desempacotamento
* - faz empacotamento (Guarda o que sobrar numa lista)
O _ (anderline) significa: Eu sei que existe um valor auqi, mas não vou usar
"""
_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome)