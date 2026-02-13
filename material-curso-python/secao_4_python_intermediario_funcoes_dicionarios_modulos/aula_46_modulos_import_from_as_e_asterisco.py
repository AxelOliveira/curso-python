"""
Módulos no Python - import, from, as e *

O que são ,ódulos?
- São arquivos Python pronto com funções, variáveis e classes.
- Servem para reutilizar código já existente

Formas de importar:

1) import modulo
    - Mantém o namespace (ex: sys.platform)
    - Mais seguro e explícito

2) from modulo import objero
    - Importa somente partes específicas.
    - Nomes ficam menores, mas perde o namespace.

3) as (alias)
    - Cria apelidos para módulos ou objetos
    - Evita conflitos de nomes

4) from modulo import *
    - Importa tudo no escopo atual
    ⚠️ Considerado má prática na maioria dos casos.   

Documentação oficial:
https://docs.python.org/3/py-modindex.html

Ordem mental:
1) Python carrega o módulo
2) Cria nomes no escopo atual
3) Podemos acessar funções/atributos importados
"""

#----------------------------------------------------------------------------------
# 1 - Importando o módulo inteiro (mantém namespace)
import sys

# 2 - Criando variável com mesmo nome de algo do módulo
platform = 'A MINHA'

# 3 - Acessando atributo pelo namespace do módulo
print(sys.platform)

# 4 - Veriável local não interfere no módulo
print(platform)

#----------------------------------------------------------------------------------

"""
from modulo import pares específicas

Vantagem:
- nomes menores

Desvantagem:
- perde o namespace (não usa mais sys.algo)
"""

# 5 - Importando apenas objetos específicos
from sys import exit, platform

# 6 - Agora platform vem direto do módulo
print(platform)

#----------------------------------------------------------------------------------

"""
Alias com as

Serve para:
- evitar conflitos
- encurtar nomes
"""

# 7 - Criando apelido para o módulo
import sys as s

# 8 - Sobrescrevendo o nome sys localmente (não afeta o alias)
sys = 'alguma coisa'

# 9 - Acessando pelo alias continua funcionando
print(s.platform)

# 10 - Mostrando valor da variável local
print(sys)


# 11 - Alias em importações específicas
from sys import exit as ex
from sys import platform as pf

# 12 - Usando apelido do atributo
print(pf)

"""
Má prática - import *

Problemas:
- Polui o escopo
- Pode sobrescrever variáveis sem perceber
- Dificulta leitura do código
"""

# 13 - Importação explítica novamente (evitando *)
from sys import exit, platform

# 14 - Uso do objeto importado
print(platform)

# 15 - Encerra o programa
exit()