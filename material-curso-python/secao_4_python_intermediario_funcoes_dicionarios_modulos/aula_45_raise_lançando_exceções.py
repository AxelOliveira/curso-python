"""
Raise - Lançando Exceções Manualmente

O que é raise?
- Serve para LANÇAR uma exceção manualmente.
- Interrompe a execução normal do programa.
- Muito usado para validação de regras de negócio.

Quando usar raise?
1) Quando um valor é inválido
2) Quando um tipo não é permitido
3) Quando quer criar erros personalizados

Built-in Exceptions:
https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

Ordem mental:
1) Funções de validação verificam os dados
2) Se algo estiver errado -> raise dispara o erro
3) A execução para imediatamente
4) Se estiver tudo certo -> continua normalmente
"""

# 1 - Função que valida se o divisor é diferente de zero
def nao_aceito_zero(d):

    # 2 - Se for zero, lança exceção manualmente
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')
    
    # 3 - Retorna True se passar na validação
    return True

# 4 - Função que valida o tipo do número
def deve_ser_int_ou_float(n):

    # 5 - Guarda o tipo recebido
    tipo_n = type(n)

    # 6 - Verifica se NÃO é int nem float
    if not isinstance(n, (float, int)):

        # 7 - Lança erro informando o tipo incorreto
        raise TypeError(
            f'"{n}" deve ser int ou float'
            f'"{tipo_n.__name__}" enviado'
        )
    
    # 8 - Retorna True se estiver correto
    return True

# 9 - Função principal que realiza a divisão
def divide(n, d):

    # 10 - Valida o numerador
    deve_ser_int_ou_float(n)

    # 11 - Valida o denominador
    deve_ser_int_ou_float(d)

    # 12 - Verifica se o denominador é zero
    nao_aceito_zero(d)

    # 13 - Executa a divisão somente se tudo estiver válido
    return n / d

# 14 - Teste: aqui vai gerar TypeError antes mesmo de dividir
print(divide(8, '0'))