# For é usado quando você quer percorrer algo que tem fim -> controla a repetição
# In significa "para cada item dentro de" -> indica de onde vêm os valores

texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')