"""
Quando você vê esse nome Singleton, quer dizer que só pode existir uma instância daquela coisa no programa inteiro Enquanto o programa está executando
"""
import importlib

import aula_49_modulo

print(aula_49_modulo.variavel)

for i in range(10):
    importlib.reload(aula_49_modulo)
    print(i)

print('Fim')