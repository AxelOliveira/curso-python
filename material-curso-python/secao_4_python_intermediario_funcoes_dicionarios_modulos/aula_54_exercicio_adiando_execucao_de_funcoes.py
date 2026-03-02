# ============================================================
# 1) Funções base
# ============================================================

# 1 - Função que soma dois valores
def soma(x, y):
    return x + y

# 2 - Função que multiplica dois valores
def multiplica(x, y):
    return x * y

# ============================================================
# 2) Função que cria nova função (Closure)
# ============================================================

# 3 - Recebe uma função e um valor fixo (x)
def criar_funcao(funcao, x):

    # 4 - Função interna que recebe o segundo valor (y)
    def interna(y):

        # 5 - Executa a função original usando:
        #    - x fixo(do escopo externo)
        #    - y recebido depois
        return funcao(x, y)
    
    # 6 - Retorna a função interna sem executá-la
    return interna

# ============================================================
# 3) Criando novas funções com execução adiada
# ============================================================

# 7 - Cria função que sempre soma 5 ao valor recebido
soma_com_cinco = criar_funcao(soma, 5)

# 8 - Cria função que sempre multiplica por 10
multiplica_por_dez = criar_funcao(multiplica, 10)

# ============================================================
# 4) Executando as funções criadas
# ============================================================

# 9 - Agora a execução acontece
print(soma_com_cinco(10))
print(multiplica_por_dez(10))