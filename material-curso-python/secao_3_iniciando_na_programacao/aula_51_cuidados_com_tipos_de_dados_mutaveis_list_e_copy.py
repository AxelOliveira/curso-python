"""
Cuidados com dados mutáveis
= - quando usa o = copiado o valor (imutáveis)
= - quando usa o = aponta para o mesmo valor na memória (mutável)
.copy faz uma copia da lista
imutáveis = não muda o valor
mutável = muda o valor
= não copia listas, cria ligação
.copy() copia a lista, mas não copia listas internas
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)