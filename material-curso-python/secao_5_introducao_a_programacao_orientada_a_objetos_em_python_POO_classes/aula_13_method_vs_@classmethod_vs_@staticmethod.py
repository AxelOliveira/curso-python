"""
🔹 method (método de instância)
- Recebe: self
- Acessa: dados do objeto
- Uso: trabalhar com atributos da instância

🔹 @classmethod
- Recebe: cls
- Acessa: a classe
- Uso: criar objetos (factory) ou trabalhar com a classe

🔹 @staticmethod
- Recebe: nada
- Acessa: nada (nem instância nem classe)
- Uso: organização (função dentro da classe)

💡 REGRA DE OURO:

Precisa de self? -> method
Precisa de cls? -> classmethod
Não precisa de nada? - função ou staticmethod
"""
class Connection:
    def __init__(self, host='localhost'):
        # 1 - Atributo da instância
        self.host = host

        # 2 - Ainda nãp definifo
        self.user = None

        # 3 - Ainda não definido
        self.password = None

    # 4 - Método de instância -> usa self
    def set_use(self, user):
        self.user = user

    # 5 - Método de instância -> usa self
    def set_password(self, password):
        self.password = password

    # 6 - Cria nova instância (factory)
    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    # 7 - Não usa self nem cls   
    @staticmethod
    def log(msg):
        print('LOG:', msg)

# 8 - Criando conexão via factory
c1 = Connection.create_with_auth('Jeon', '1234')

# 9 - Usando método estático
print(Connection.log('Essa é a mensagem de log'))

# 10 - Acessando dados da instância
print(c1.user)
print(c1.password)