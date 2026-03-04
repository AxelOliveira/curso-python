"""
Variáveis livres + nonlocal (locals e globals)

1) Variável livre:
    - É uma variável usada dentro de uma função interna, mas que foi criada no escopo da função externa.

2) Closure:
    - A função interna "lembra" das variáveis do escopo externo.

3) nonlocal:
    - Permite modificar uma variável do escopo imediatamente externo.
    - Sem nonlocal, só podrámos ler a variável, não alterar.

4) locals():
    - Retorna um dicionário com variáveis locais do escopo atual.

5) globals():
    - Retorna um dicionário com variáveis globais do arquivo.
"""
# ============================================================
# 1) Criando a função externa
# ============================================================

# 1 - Criar função que recebe uma string inicial
def concatenar(string_inicial):
    
    # 2 - Criar variável no escopo externo (variável livre)
    valor_final = string_inicial

    # ========================================================
    # 2) Criando função interna (closure)
    # ========================================================

    # 3 - Criar função interna que recebe valor opcional
    def interna(valor_a_concatenar=''):

        # 4 - Informar que queremos modificar a variável do escopo externo
        nonlocal valor_final

        # 5 - Concatenar o novo valor ao valor já existente
        valor_final += valor_a_concatenar

        # 6 - Retornar o valor atualizado
        return valor_final
    
    # 7 - Retornar a função interna sem executá-la
    return interna

# ============================================================
# 3) Criando a closure
# ============================================================

# 8 - Criar função especializada iniciando com "a"
c = concatenar('a')

# ============================================================
# 4) Executando
# ============================================================

# 9 - Executar múltiplas vezes para observar o "estado interno"
print(c('b'))
print(c('c'))
print(c('d'))

# 10 - Executar sem passar valor (usa padrão '')
final = c()
print(final)