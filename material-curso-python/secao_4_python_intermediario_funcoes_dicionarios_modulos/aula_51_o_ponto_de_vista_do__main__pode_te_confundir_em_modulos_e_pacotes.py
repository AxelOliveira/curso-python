"""
Então se eu executo este programa, o ponto de vista é deste main.
Se eu executo este módulo, o ponto de vista deste módulo.

E aí ele não vai encontrar o módulo B porque ele está olhando pelo ponto de vista do Aula 51.


Toda vez que você tiver um main 
todas as importações do programa inteiro precisam ser relacionadas com o seu main.

Ou seja, essa importação aqui do From módulo B import fala oi, tem

que ser como se eu tivesse fazendo essa importação do aula 51

então se eu vir aqui eu teria que falar o nome do packet.
"""

from sys import path

import aula_51_package.modulo
from aula_51_package import modulo
from aula_51_package.modulo import *

print(soma_do_modulo(1, 2))
print(aula_51_package.modulo.soma_do_modulo(1, 2))
print(variavel)
print(nova_variavel)

from aula_51_package.modulo import fala_oi, soma_do_modulo

print(__name__)
fala_oi()