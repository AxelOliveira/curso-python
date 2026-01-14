"""
Escopo de funções em Python
Escopo é a região do código onde uma variável existe e pode ser usada.
Em Python, existem dois escopos principais:
- Escopo global → fora das funções
- Escopo local → dentro das funções
Uma variável criada:
- No escopo global → pode ser usada no código global
- No escopo local → só existe dentro daquela função
Um escopo externo não enxerga variáveis de escopos internos.
global deve ser evitado sempre que possível
"""

# Essa variável pode ser lida dentro de funções, mas não pode ser alterada, a menos que você use global
x = 1

def escopo():
    global x                                                    # Essa variável NÃO é local, é a mesma que existe fora da função
    x = 10

    def outra_funcao():
        global x
        x = 11
        y = 2                                                    # A variável y não existe fora da função
        print(x, y)

    outra_funcao()
    print(x)

print(x)
escopo()
print(x)