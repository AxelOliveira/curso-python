"""
Aula 4 - Entendendo o self em classes

Conceitos importantes:
- Classe -> molde (define estrutura)
- Objeto -> instância com dados
- self -> referência ao objeto que está usando o método

Ideia principal:
Quando um objeto chama um método, ele mesmo é passado automaticamente como primeiro argumento (self).

Exemplo:
fusca.acelerar()

Internamente vira:
Carro.acelerar(fusca)
"""

# 1 - Criando a classe
class Carro:

    # 2 - Inicializando o objeto
    def __init__(self, nome):
        self.nome = nome

    # 3 - Método que usa os dados do objeto
    def acelerar(self):
        print(f'{self.nome} está acelerando...')

# 4 - Criando objeto
fusca = Carro('Fusca')

# 5 - Chamando método (forma comum)
fusca.acelerar()

# 6 - Chamando método pela classe (forma explícita)
Carro.acelerar(fusca)

# 7 - Outro objeto
celta = Carro(nome='Celta')

celta.acelerar()
Carro.acelerar(celta)