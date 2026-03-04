"""
Decoradores com parâmetros

1) Decoradores simples:
    - Recebem apenas a função como argumento.

2) Decoradores com parâmetros:
    - Precisam de uma função EXTRA (nível a mais)
    - Estrutura fica com 3 níveis:
        - Fábrica de decoradores
        - Decorador
        - Função aninhada

3) Ordem mental:
    - Primeiro executa a fábrica (quando usa @)
    - Depois executa o decorador
    - Depois executa a função aninhada quando a função for chamada
"""

# ============================================================
# 1) Criar fábrica de decoradores
# ============================================================

# 1 - Criar função externa que recebe parâmetros do decorador
def fabrica_de_decoradores(a=None, b=None, c=None):

    # 2 - Criar função decoradora que recebe a função original
    def fabrica_de_funcoes(func):

        print('Decoradora 1')

        # 3 - Criar função aninhada que executará no momento da chamada
        def aninhada(*args, **kwargs):

            # 4 - Executar comportamento antes da função original
            print('Parâmetros do decorador, ', a, b, c)
            print('Aninhada')

            # 5 - Executar função original
            res = func(*args, **kwargs)

            # 6 - Retornar resultado original
            return res
        
        # 7 - Retornar função aninhada
        return aninhada
    
    # 8 - Retornar decorador
    return fabrica_de_funcoes

# ============================================================
# 2) Aplicar decorador com parâmetros usando @
# ============================================================

# 9 - Aqui acontece:
#     soma = fabrica_de_decoradores(1, 2, 3)(soma)
@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y

# ============================================================
# 3) Aplicação manual do decorador
# ============================================================

# 10 - Criar decorador sem parâmetros definidos
decoradora = fabrica_de_decoradores()

# 11 - Decorar função lambda manualmente
multiplica = decoradora(lambda x, y: x * y)

# ============================================================
# 4) Executar
# ============================================================

# 12 - Executar função decorada com @
dez_mais_cinco = soma(10, 5)

# 13 - Executar função decorada manualmente
dez_vezes_cinco = multiplica(10, 5)

# 14 - Exibir resultados
print(dez_mais_cinco)
print(dez_vezes_cinco)