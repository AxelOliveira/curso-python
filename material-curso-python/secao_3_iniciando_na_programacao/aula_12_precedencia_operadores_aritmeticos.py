# Ordem Geral de Precedência (Maior para Menor)
# Parênteses (): O que estiver dentro parênteses tem prioridade absoluta e é executado primeiro.
# Expoentes/Potência ^ ou **: Calculados logo após os parênteses.
# Operadores Unários +, - (sinal), !, ++, --: Inclui negação lógica e incremento/decremento.
# Multiplicação *, Divisão /, Módulo % ou mod: Aritmética de alto nível.
# Adição + e Subtração -: Aritmética de baixo nível.
# Operadores Relacionais >, <, >=, <=, ==, !=: Comparações.
# Operadores Lógicos !, &&, || (ou NOT, AND, OR): Negação (!) é mais forte, seguida por E (&&), depois OU (||).
# Atribuição =, +=, -=, etc.: Geralmente é a última operação a ser realizada. 

conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)