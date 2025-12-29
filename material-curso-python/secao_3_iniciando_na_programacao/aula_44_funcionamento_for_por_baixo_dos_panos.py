"""
Iterável -> str, range, list, tuple (__iter__) é algo que pode ser percorrido, elemento por elemento
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
Todo for usa internamente inter() + next() + StopIteration
E
Todo while precisa de alguém que mude a condição
"""
# --------------------------------------------------------------------------------------------------------------------

# for letra in texto
texto = 'Luiz' # iterável

# iteratador = iter(texto)  # iterator

# while True:                               # Enquanto for possível pegar letra
#     try:
#         letra = next(iteratador)          # pega a próxima letra
#         print(letra)                      # imprime a letra
#     except StopIteration:                 # quando acabar as letras
#         break                             # para o loop


# ESSE CÓDIGO É EQUIVALENTE AO WHILE ACIMA
for letra in texto:                         
    print(letra)