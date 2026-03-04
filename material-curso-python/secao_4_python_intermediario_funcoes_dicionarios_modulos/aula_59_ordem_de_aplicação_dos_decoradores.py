"""
Ordem de aplicação dos decoradores

1) Quando usamos vários decoradores, o Python aplica de baixo para cima.

2) Porém, na execução da função, o comportamento acontece de fora para dentro.

3) A regra mental:
    - O decorador mais próximo da função é aplicado primeiro.
    - O decorador mais distante é o último a envolver a função.

4) É como "camadas de cebola":
    - Cada decorador envolve o anterior.
"""

# ============================================================
# 1) Criar fábrica de decoradores
# ============================================================

# 1 - Criar função que recebe o nome do decorador
def parametros_decorador(nome):

    # 2 - Criar decorador que recebe a função original
    def decorador(func):

        # 3 - Executa no momento da definição da função
        print('Decorador:', nome)

        # 4 - Criar nova função que substituirá a original
        def sua_nova_funcao(*args, **kwargs):

            # 5 - Executar função anterior (já decorada)
            res = func(*args, **kwargs)

            # 6 - Adicionar identificação ao resultado
            final = f'{res} {nome}'

            # 7 - Retornar novo resultado
            return final
        
        # 8 - Retornar função modificada
        return sua_nova_funcao
    
    # 9 - Retornar decorador
    return decorador

# ============================================================
# 2) Aplicar múltiplos decoradores
# ============================================================

# 10 - Ordem real que o Python executa na definição:
#       soma = d5(d4(d3(d2(d1(soma)))))
@parametros_decorador(nome='5')
@parametros_decorador(nome='4')
@parametros_decorador(nome='3')
@parametros_decorador(nome='2')
@parametros_decorador(nome='1')
def soma(x, y):

    # 11 - Função original
    return x + y

# ============================================================
# 3) Executar
# ============================================================

# 12 - Executar função já envolvida por todas as camadas
dez_mais_cinco = soma(10, 5)

# 13 - Mostrar resultado final
print(dez_mais_cinco)