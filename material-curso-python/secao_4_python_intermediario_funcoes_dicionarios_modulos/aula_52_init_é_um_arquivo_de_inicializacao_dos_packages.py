"""
CONCEITOS PRINCIPAIS:

1) Um package é uma pasta que organiza módulos Python.

2) O arquivo __init__.py é executado automaticamente quando o package é importado.

3) O __init__.py pode:
    - Inicializar algo
    - Organizar exports
    - Controlar o namespace do package

4) Quando fazemos:
    from pacote import algo
    O Python executa o __init__.py primeiro.

5) O package funciona como um namespace, usando o nome da pasta como referência.
"""
# 1 - Importando diretamente do package (na prática estamos importando do __init__.py)
from aula_52_package import fala_oi, soma_do_modulo

# 2 - Usando função que veio do módulo via __init__
print(soma_do_modulo(2, 3))

# 3 - Usando função que veio de outro módulo via __init__
fala_oi()