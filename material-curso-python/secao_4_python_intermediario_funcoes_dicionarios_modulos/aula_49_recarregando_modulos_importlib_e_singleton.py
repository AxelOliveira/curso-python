"""
CONCEITOS PRINCIPAIS:

1) Quando um módulo é importado, o Python o executa apenas UMA vez.

2) Depois de importado, o módulo fica armazenado em memória dentro de sys.modules

3) Se você importar novamente o mesmo módulo, o Python NÃO executa o código de novo. Ele reaproveita a mesma instância (Singleton).

4) Singleton significa:
    - Durante a execução do programa, existe apenas uma instância daquele módulo em memória.

5) Para forçar a reexecução do módulo, usamos: importlib.reload(modulo)
"""
# 1 - Importamos a biblioteca responsável por recarregar módulos
import importlib

# 2 - Importamos o módulo normalmente (executa apenas uma vez)
import aula_49_modulo

# 3 - Acessamos uma variável do módulo
print(aula_49_modulo.variavel)

# 4 - Recarregamos o módulo 10 vezes
for i in range(10):

    # 5 - Forçamos o Python a executar novamente o código do módulo
    importlib.reload(aula_49_modulo)

    # 6 - Mostramos o número da iteração
    print(i)

# 7 - Final do programa
print('Fim')