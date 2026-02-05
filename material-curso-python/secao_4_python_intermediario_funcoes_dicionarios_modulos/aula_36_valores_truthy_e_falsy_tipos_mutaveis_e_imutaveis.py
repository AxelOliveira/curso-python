"""
Valores Truthy e Falsy | Tipos mutáveis e imutáveis

Em Python, todo valor pode ser interpretado como:
- truthy  -> considerado verdadeiro em um if
- falsy   -> considerado falso em um if

Isso é muito usado em estruturas condicionais.

-----------------------------------------------------------------------------
📌 Valores Falsy mais comuns:

- []        lista vazia
- {}        dicionário vazio
- set()     conjunto vazio
- ()        tupla vazia
- ''        string vazia
- 0         inteiro zero
- 0.0       float zero
- None
- False
- range(0)

Qualquer outro valor, em geral, é considerado truthy.
"""

# Tipos mutáveis (podem ser alterados depois de criados)
lista = []
dicionario = {}
conjunto = set()

# Tipos imutáveis (não podem ser alterados)
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)


# Função para testar se um valor é truthy ou falsy
def falsy(valor):
    return 'falsy' if not valor else 'truthy'


# Testes
print(f'TESTE', falsy('TESTE'))

print(f'{lista= }', falsy(lista))
print(f'{dicionario= }', falsy(dicionario))
print(f'{conjunto= }', falsy(conjunto))

print(f'{tupla= }', falsy(tupla))
print(f'{string= }', falsy(string))
print(f'{inteiro= }', falsy(inteiro))
print(f'{flutuante= }', falsy(flutuante))
print(f'{nada= }', falsy(nada))
print(f'{falso= }', falsy(falso))
print(f'{intervalo= }', falsy(intervalo))