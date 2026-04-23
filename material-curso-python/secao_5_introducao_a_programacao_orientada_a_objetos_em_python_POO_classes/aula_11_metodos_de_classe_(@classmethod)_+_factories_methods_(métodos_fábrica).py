"""
🔹 Método de instância (normal)
- Recebe "self"
- Trabalha com os dados da instância (objeto)
- Precisa de um objeto para ser chamado

🔹 Método de classe (@classmethod)
- Recebe "cls" (a classe)
- Não precisa de instância para ser chamado
- Pode acessar/modificar dados da classe
- Pode criar novos objetos

🔹 Factory Method (método fábrica)
- É um método (geralmente de classe) que CRIA objetos
- Serve para padronizar ou facilitar a criação de instâncias

💡 Ideia principal:
Você usa @classmethod quando quer trabalhar com a CLASSE e não com um objeto específico.

💡 Uso comum:
- Criar objetos com valores padrão
- Criar objetos com regras específicas
- Evitar repetição de código
"""
class Pessoa:

    # 1 - Atributo da classe (compartilhado por todos)
    ano = 2026    

    def __init__(self, nome, idade):
        # 2 - Dado da instância
        self.nome = nome
        # 3 - Dado da instância
        self.idade = idade

    @classmethod
    # 4 - Recebe a classe ao invés da instância
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    # 5 - Cria um novo objeto com idade fixa
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    # 6 - Cria um novo objeto com nome padrão
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)

# 7 - Criando objeto normal   
p1 = Pessoa('João', 34)

# 8 - Criando objeto via factory method
p2 = Pessoa.criar_com_50_anos('Helena')

# 9 - Criando manualmente
p3 = Pessoa('Anônima', 23)

# 10 - Criando via factory method
p4 = Pessoa.criar_sem_nome(25)

# 11 - Exibindo resultados
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)