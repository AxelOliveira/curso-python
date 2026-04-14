# Class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de classes.

class Pessoa:
    ...


p1 = Pessoa()
p1.nome = 'Jeon'
p1.sobrenome = 'Wonwoo'

p2 = Pessoa()
p2.nome = 'Kim'
p2.sobrenome = 'Mingyu'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)