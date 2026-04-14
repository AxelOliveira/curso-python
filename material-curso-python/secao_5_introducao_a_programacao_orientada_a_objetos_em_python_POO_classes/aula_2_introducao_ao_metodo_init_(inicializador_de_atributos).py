"""
Aula 2 - Método __init__ (Inicializador de atributos)

O método __init__ é executado automaticamente quando um objeto é criado.

Objetivo:
Inicializar (criar) os atributos do objeto no momento da criação.

Conceitos importantes:
- __init__: método especial chamado automaticamente
- self: referência ao objeto que está sendo criado
- Parâmetros: Valores recebidos na criação do objeto

Fluxo:
Pesso('Jeon', 'Wonwoo')
↓
1. Cria o objeto
2. Chama __init__
3. self recebe o objeto criado
4. nome e sobrenome recebem os valores passados
5. atributos são criados dentro do objeto
"""

# 1 - Cirando a classe
class Pessoa:

    # 2 - Método inicializador
    def __init__(self, nome, sobrenome):

        # 3 - Criando atributos dentro do objeto (self)
        self.nome = nome
        self.sobrenome = sobrenome


# 4 - Criando objetos já com dados
p1 = Pessoa('Jeon','Wonwoo')
p2 = Pessoa('Kim', 'Mingyu')

# 5 - Acessando os dados
print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)