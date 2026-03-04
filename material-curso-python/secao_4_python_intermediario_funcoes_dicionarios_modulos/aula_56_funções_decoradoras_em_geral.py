"""
Funções decoradoras em geral

1) Decorar = Adicionar / Remover / Restringir / Alterar comportamento.

2) Função decoradora:
    - É uma função que recebe outra função como argumento e retorna uma nova função modificada.

3) Decoradores:
    - São uma forma mais elegante de aplicar funções decoradoras.

4) *args e **kwargs:
    - Permitem que a função interna aceite qualquer quantidade de argumentos posicionais e nomeados.

5) Single Responsibility Principle (SRP):
    - Cada função deve ter apenas uma responsabilidade.
    - Aqui, separamos:
        - Validação (e_string)
        - Lógica principal (inverte_string)
        - Comportamento extra (decorador)
"""

# ============================================================
# 1) Criar função decoradora
# ============================================================

# 1 - Criar função que recebe outra função como argumento
def criar_funcao(func):

    # 2 - Criar função interna que executará a decoração
    def interna(*args, **kwargs):

        # 3 - Executar comportamento antes da função original
        print('Vou te decorar')

        # 4 - Validar todos os argumentos posicionais
        for arg in args:
            e_string(arg)

        # 5 - Executar função original
        resultado = func(*args, **kwargs)

        # 6 - Executar comportamento depois da função original
        print(f'O seu resultado foi {resultado}')
        print('Ok, agora você foi decorada')

        # 7 - Retornar resultado original
        return resultado
    
    # 8 - Retornar a função interna sem executá-la
    return interna

# ============================================================
# 2) Criar função principal
# ============================================================

# 9 - Função com responsabilidade única: inverter string
def inverte_string(string):
    return string[::-1]

# ============================================================
# 3) Criar função de validação (SRP)
# ============================================================

# 10 - Função responsável apenas por validar tipo
def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')
    
# ============================================================
# 4) Aplicar a decoração manualmente
# ============================================================

# 11 - Criar nova função decorada
inverte_string_checando_parametro = criar_funcao(inverte_string)

# 12 - Executar função decorada
invertida = inverte_string_checando_parametro('123')

# 13 - Exibir resultado final
print(invertida)