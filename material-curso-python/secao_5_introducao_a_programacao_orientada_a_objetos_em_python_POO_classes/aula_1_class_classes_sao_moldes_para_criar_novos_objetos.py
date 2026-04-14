"""
Aula 1 - Classes (Classes são moldes para criar objetos)

Uma classe é como um "molde" que usamos para criar objetos (instâncias).

Conceitos importantes:
- Classe: molde (ex: Pessoa)
- Objeto/Instância: algo criado a partir da classe (ex: p1, p2)
- Atributos: dados do objeto (ex: nome, sobrenome)
- Métodos: ações do objeto (veremos depois)

Exemplo mental:
Classe Pessoa -> molde
p1 = Pessoa() -> pessoa criada a partir do molde

Cada objeto tem seus próprios dados.
"""

# 1 - Criando a classe (molde)
class Pessoa:
    ...


# 2 - Criando o primeiro objeto (instância)
p1 = Pessoa()

# 3 - Atribuindo dados (atributos) ao objeto p1
p1.nome = 'Jeon'
p1.sobrenome = 'Wonwoo'

# 4 - Criando outro objeto (nova instância independente)
p2 = Pessoa()

# 5 - Atribuindo dados ao segundo objeto
p2.nome = 'Kim'
p2.sobrenome = 'Mingyu'

# 6 - Acesssando os dados do primeiro objeto
print(p1.nome)
print(p1.sobrenome)

# 7 - Acessando os dados do segundo objeto
print(p2.nome)
print(p2.sobrenome)