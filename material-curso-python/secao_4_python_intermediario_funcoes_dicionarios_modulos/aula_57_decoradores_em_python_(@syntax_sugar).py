"""
Funções decoradoras e decoradores
Decorar = Adicionar / Remover / Restringir / Alterar
Funções decoradoras são funções que decoram outras funções
Decoradores são usados para fazer o Python usar as funções decoradoras em outras funções.
Single Responsibility Principle = Se um objeto está fazendo mais do que necessário, quer dizer que está errado e tem que dividir esse objeto e fazer ele fazer várias coisas.
Decoradores são 'Syntax Sugar' (Açúcar sintático), Isso significa que a liguagem tem um recurso que facilita o uso das funções decoradoras, sem que a gente tem que escrever e reescrever o nosso código
"""
def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}')
        print('Ok, agora você foi decorada')
        return resultado
    return interna

@criar_funcao
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')
    
invertida = inverte_string('123')
print(invertida)