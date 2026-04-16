"""
Aula 5 - Escopo da classe e dos métodos

Conceitos importantes:
- Classe tem seu próprio escopo (namespace)
- Cada método também tem seu próprio escopo
- Variáveis criadas dentro de um método NÃO existem fora dele
- Atributos com self podem ser acessados em qualquer método da classe

Regra principal:
- variável normal -> só existe dentro do método
- self.atributo -> existe no objeto (pode ser usado em outros métodos)
"""

# 1 - Criando a classe
class Animal:

    # 2 - Método inicializador
    def __init__(self, nome):
        self.nome = nome        # atributo da instância

        # variável local (só existe aqui dentro)
        variavel = 'valor'
        print(variavel)

    # 3 - Método que usa atributo da instância
    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'
    
    # 4 - Método chamando outro método
    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)

# 5 - Criando objeto    
leao = Animal(nome='Leão')

# 6 - Acessando atributo
print(leao.nome)

# 7 - Chamando método
print(leao.executar('maçã'))