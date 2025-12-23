"""
Fatiamento de strings
012345678 - Indices positivos começa pelo 0
Olá mundo
-987654321 - Indices negativos começa pelo -1
Espaço é considerado caractere
Fatiamento [i:f:p] [::]
Se omitir o indice inicial ou final, ele vai ler até o final da frase ou desde o começo da frase
Obs.: a função len retorna a quatidade de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[4:]) # Aqui ele vai iniciar do indice 4 e ir até o final da frase, pois não coloquei um indice final
print(variavel[4:7]) # Aqui ele vai iniciar do indice 4 e ir só até o indice 6
print(variavel[0:5]) # Aqui ele vai iniciar do indice 0 e ir só até o indice 4
print(variavel[-8:-2]) # Aqui ele vai iniciar do indice -8 e ir só até o indice -2
print(10 * '-')
print(len(variavel)) # Aqui irá o mostrar a quantidade de caracteres da string
print(variavel[0:9:1]) # Aqui ele está iniciando no indice 0 indo até o 9 e contando/pulando de 1 em 1
print(variavel[0:9:2]) # Aqui ele está iniciando no indice 0 indo até o 9 e contando/pulando de 2 em 2 (pega um, pula o outro, pega um pula o outro...)
print(variavel[::-1]) # Aqui ele irá ler de trás para frente (invertido)
print(variavel[-1:-10:-2])