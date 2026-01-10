"""
split e join com list e str
split - divide uma string
join - une uma string
Objetivo:
Transformar uma string desorganizada em uma string limpa e bem formatada.

Lógica:
1. Quebrar a string em partes (split)
2. Limpar espaços extras de cada parte (strip)
3. Reunir tudo novamente em uma única string (join)
.split(), dentro do parenteses eu posso informar em qual caractere eu quero que quebre a separação
.strip(), corta os espaços do começo e do fim
.rstrip (), corta só o espaço da direita
.lstrip(), corta só o espaço da esquerda
.join(), adicio algo na frase
"""
frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frase)

frases_unidas = ', '.join(lista_frases)
print(frases_unidas)