"""
Módulo interno

Este módulo será acessado pelo arquivo principal.
A variável __all__ define o que será exportado quando usamos: from modulo import *
"""
# 1 - Controla o que será exportado com import*
__all__ = [
    'variavel',
    'soma_do_modulo',
    'nova_variavel',
]

# 2 - Variável do módulo
variavel = 'Alguma coisa'

# 3 - Função do módulo
def soma_do_modulo(x, y):
    return x + y

# 4 - Outra variável exportada
nova_variavel = 'OK'