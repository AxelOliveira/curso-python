"""
CONCEITOS PRINCIPAIS:

1) O Python sempre executa um arquivo principal.
   Esse arquivo recebe o nome especial "__main__"

2) O Python monta o sys.path a partir da pasta onde o __main__ está

3) Todas as importações do programa devem ser pensadas a partir do ponto de vista do __main__

4) Se você executar um módulo interno diretamente, o ponto de vista muda - e os imports podem quebrar

5) Em pacotes, imports absolutos devem considerar o caminho completo a partir da raiz do projeto
"""

# 1 - O Python começa a execução por este arquivo(__main__)
from sys import path

# 2 - Importando o módulo pelo caminho completo do pacote
import aula_51_package.modulo

# 3 - Importando o módulo diretamente do pacote
from aula_51_package import modulo

# 4 - Importando tudo do módulo
from aula_51_package.modulo import *

# 5 - Usando função via import *
print(soma_do_modulo(1, 2))

# 6 - Usando função pelo caminho completo
print(aula_51_package.modulo.soma_do_modulo(1, 2))

# 7 - Variáveis vindas do módulo
print(variavel)
print(nova_variavel)

# 8 - Importando funções específicas
from aula_51_package.modulo import fala_oi, soma_do_modulo

# 9 - Mostrando o nome do módulo atual
print(__name__)

# 10 - Executando função que veio do modulo_b
fala_oi()