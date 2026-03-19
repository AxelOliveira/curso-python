"""
Funções recursivas em Python podem ser usadas de forma parecida com loops (fo/while).

Na prática, muitas vezes não faz sentido usar recursão em Python, porque loops costumam ser mais simples e seguros.

Mas é importante entender recursão porque:
- Existe na linguagem
- É muito usada em programação funcional
- Pode aparecer em entrevistas e problemas mais complexos

Cuidaod importante:

Mesmo com a lógica correta, você pode quebrar seu programa.

Exemplo:
Se você fizer uma recursão muito grande (ex: de 0 até 1000), vai atingir o limite de recursão do Pyhton.

Isso acontece porque:
- Cada chamada da função é salva na call stack (memória)
- Não é só sua função -> também tem módulo, execução inicial, etc.
- O limite padrão é por volta de 1000 chamadas

Por isso, às vezes o erro aparece antes (ex: 996).

Esse erro é o mesmo de uma recursão sem caso base:
RecursionError (estouro da pilha / stack overflow)

É possível alterar esse limite:

import sys
sys.setrecursionlimit(1004)

Mas isso NÃO é recomendado na maioria dos casos, porque você pode consumir muita memória.

Ou sej:
- Recursão funciona
- Mas deve ser usada com cuidado
- Em alguns casos, loops são melhores

Agora vamos ver um exemplo clássico: fatorial
"""

def factorial(n):
    # 1 - Caso base: quando o número for 1 ou menor
    if n <= 1:
        return 1
    
    # 2 - Caso recursivo: multiplica o número atual pelo fatorial do número anterior
    return n * factorial(n - 1)

# 3 - Testes
print(factorial(5))
print(factorial(10))
print(factorial(100))