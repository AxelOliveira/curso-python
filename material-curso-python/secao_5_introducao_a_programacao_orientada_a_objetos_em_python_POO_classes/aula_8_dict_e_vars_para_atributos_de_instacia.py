"""
Aula 8 - __dict__ e vars para atributos de instância

Conceito principal:
Todo objeto em Python armazena seus atributos em um dicionário interno.

Esse dicionário é:
- __dicct__ (atributo interno)
- vars(obj) (forma recomendada de acessar)

Para que serve?
- Inspecionar dados do objeto
- Converter para JSON
- Recriar objetos
"""

# 1 - Criando a classe
class Pessoa:
    ano_atual = 2026

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
# 2 - Criando objeto com desempacotamento
dados = {'nome': 'João', 'idade': 35}
p1 = Pessoa(**dados)

# 3 - Visualizando atributos da instância
print(vars(p1))             # {'nome': 'João', 'idade': 35}
print(p1.__dict__)          # mesma coisa

# 4 - Acessando normalmente
print(p1.nome)

# 5 - Alterando via __dict__
p1.__dict__['nome'] = 'Maria'
print(p1.nome)