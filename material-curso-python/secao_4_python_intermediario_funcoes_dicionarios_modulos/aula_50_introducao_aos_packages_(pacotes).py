from sys import path

import aula_50_package.modulo

from aula_50_package import modulo
from aula_50_package.modulo import *

print(soma_do_modulo(1, 2))
print(aula_50_package.modulo.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))
print(variavel)
print(nova_variavel)