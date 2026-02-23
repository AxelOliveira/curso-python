"""
Como importar coisas do seu próprio módulo
(Ponto de vista do __main__)

CONCEITOS PRINCIPAIS:

1) O primeiro arquivo executado sempre se chama "__main__".

2) O Python conhece:
    - A pasta onde o __main__ está
    - As pastas abaixo dela

3) O Python NÃO reconhece automaticamente:
    - Pastas acima do __main__

4) Existem duas formas principais de importação:

    a) Importando o módulo inteiro:
       import modulo

       -> Para acessar algo: modulo.nome

    b) Importando partes específicas:
       from modulo import nome

       -> Pode usar direto: nome

5) O Python procura módulos dentro dos caminhos listados em sys.path.
"""
# 1) Importando o módulo inteiro
import aula_48_modulo

# 2) Importando partes específicas do módulo
from aula_48_modulo import soma, variavel_modulo

# 3) Este é o arquivo principal, então seu nome será "__main__"
print('Este módulo se chama', __name__)

# 4) Acessando variável pelo módulo inteiro
print(aula_48_modulo.variavel_modulo)

# 5) Acessando variável importada diretamente
print(variavel_modulo)

# 6) Chamando função importada diretamente
print(soma(2, 3))

# 7) Chamando função pelo módulo inteiro
print(aula_48_modulo.soma(2, 3))
