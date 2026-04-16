"""
Aula 7 - Atributos de classe

Conceito principal:
Atributos de classe pertencem à classe (molde), não ao objeto.

Características:
- São compartilhados entre todas as instâncias
- Têm o mesmo valor para todos (a menos que alterados)
- São acessados preferencialmente pela classe

Diferença:
- self.atributo -> pertence ao objeto
- Classe.atributo -> pertence à classe
"""

# 1 - Criando a classe
class Pessoa:
    ano_atual = 2026        # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome        # atributo de instância
        self.idade = idade      # atributo de instância

    # 2 - Método usando atributo de classe
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

# 3 - Criando objetos    
p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 12)

# 4 - Acessando atributo de classe
print(Pessoa.ano_atual)

# 5 - Usando método
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())