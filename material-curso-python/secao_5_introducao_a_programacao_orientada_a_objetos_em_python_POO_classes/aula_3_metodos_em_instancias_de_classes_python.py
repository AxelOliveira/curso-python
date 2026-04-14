"""
Aula 3 - Métodos em instâncias de classes

Métodos são funções que ficam dentro da classe e representam ações (comportamentos).

Conceitos importantes:
- Método: função dentro da classe
- self: referência ao objeto que está chamando o método
- Cada objeto usa o mesmo método, mas com seus próprios dados

Exemplo mental:
Carro -> classe (molde)
fusca -> objeto
fusca.acelerar() -> ação do objeto
"""

# 1 - Criando a classe
class Carro:

    # 2 - Inicializando o objeto com atributo nome
    def __init__(self, nome):
        self.nome = nome

    # 3 - Criando um método (ação do objeto)
    def acelerar(self):
        print(f'{self.nome} está acelerando...')

# 4 - Exemplo com string (classe pronta do Python)
string = 'Wonwoo'
print(string.upper())        # método da classe str

# 5 - Criando objetos
fusca = Carro('Fusca')

# 6 - Acessando atributos
print(fusca.nome)
fusca.acelerar()

# 7 - Criando objeto
celta = Carro(nome='Celta')

# 8 - Acessando atributos
print(celta.nome)
celta.acelerar