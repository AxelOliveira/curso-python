"""
CONCEITOS PRINCIPAIS:

1) Um package (pacote) é uma pasta que contém módulos Python.

2) Para ser considerado um pacote tradicional, a pasta deve conter um arquivo chamado __init__.py

3) Quando usamos:
    import pacote.modulo
    -> estamos acessando um módulo dentro de um pacote

4) Podemos importar de três formas:
    
    a) import pacote.modulo
        -> acesso via pacote.modulo.nome
    
    b) from pacote import modulo
        -> acesso via modulo.nome

    c) from pacote.modulo import *
        -> importa tudo definido em __all__

5) A variável especial __all__ controla o que será importado quando usamos o operador *.
"""
# 1 - Apenas para mostrar que o Python trabalha com caminhos de importação
from sys import path

# 2 - Importando o módulo pelo caminho completo
import aula_50_package.modulo

# 3 - Importando o módulo direto do pacote
from aula_50_package import modulo

# 4 - Importando tudo definido em __all__
from aula_50_package.modulo import *

# 5 - Usando função importada via *
print(soma_do_modulo(1, 2))

# 6 - Usando função via caminho completo
print(aula_50_package.modulo.soma_do_modulo(1, 2))

# 7 - Usando função via módulo importado
print(modulo.soma_do_modulo(1, 2))

# 8 - Variáveis vindas do import *
print(variavel)
print(nova_variavel)