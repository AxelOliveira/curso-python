"""
dir(), hasattr() e getattr() em Python

Essa funções ajudam a inspecionar e acessar atributos e métodos dos objetos de forma dinâmica.

dir(objeto):
- Mostra todos os atributos e métodos disponíveis no objeto

hasattr(objeto, 'nome'):
- Verifica se o objeto possui determinado atributo ou método
- Retorna True ou False

getattr(objeto, 'nome'):
- Pega o atributo ou método pelo nome (em string)
- Muito usado quando o nome do método vem de variável
"""
string = 'Wonwoo'
metodo = 'upper'

# Verifica se o método existe dentro da string
if hasattr(string, metodo):
    print('Existe upper')

    # getattr pega o método dinamicamente
    # () executa o método retornado
    print(getattr(string, metodo)())
    
else:
    print('Não existe o método', metodo)