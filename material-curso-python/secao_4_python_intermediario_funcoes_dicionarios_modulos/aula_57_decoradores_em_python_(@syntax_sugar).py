"""
Decoradores em Python (@ - Syntax Sugar)

1) Decoradores continuam sendo funções que recebem outra função e retornam uma nova função modificada.

2) @decorador é apenas "syntax sugar":
    - É uma forma mais limpa de escrever:
        func = decorador(func)

3) O Python executa o decorador no momento da definição da função, não no momento da chamada.

4) Single Responsibility Principle:
    - Separação entre:
        - Lógica principal
        - Validação
        - Comportamento adicional
"""

# ============================================================
# 1) Criar função decoradora
# ============================================================

# 1 - Criar função que recebe outra função
def criar_funcao(func):

    # 2 - Criar função interna que executa a decoração
    def interna(*args, **kwargs):

        # 3 - Executar comportamento antes
        print('Vou te decorar')

        # 4 - Validar argumentos posicionais
        for arg in args:
            e_string(arg)

        # 5 - Executar função original
        resultado = func(*args, **kwargs)

        # 6 - Executar comportamento depois
        print(f'O seu resultado foi {resultado}')
        print('Ok, agora você foi decorada')

        # 7 - Retornar resultado original
        return resultado
    
    # 8 - Retornar função interna
    return interna

# ============================================================
# 2) Aplicar decorador com @ (Syntax Sugar)
# ============================================================

# 9 - O @criar_funcao significa:
#     inverte_string = criar_funcao(inverte_string)
@criar_funcao
def inverte_string(string):

    # 10 - Mostrar o nome da função
    # (Aqui você verá que o nome vira "interna", pois o decorator substitui a função original)
    print(f'{inverte_string.__name__}')

    # 11 - Lógica principal
    return string[::-1]

# ============================================================
# 3) Função de validação
# ============================================================

# 12 - Função responsável apenas por validar tipo
def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

# ============================================================
# 4) Executar
# ============================================================
  
# 13 - Executar função decorada
invertida = inverte_string('123')

# 14 - Mostrar resultado final
print(invertida)