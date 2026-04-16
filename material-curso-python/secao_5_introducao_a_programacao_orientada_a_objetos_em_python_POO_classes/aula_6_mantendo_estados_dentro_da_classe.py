"""
Aula 6 - Mantendo estado dentro da classe

Conceito principal:
Estado é a informação atual do objeto que pode mudar ao longo do tempo.

Exemplo:
Uma câmera pode:
- estar filmando
- não estar filmando

Esse "estado" fica salvo no objeto (self).

Regra:
- O estado é armazenado em atributos (self.atributo)
- Métodos alteram esse estado
"""

# 1 - Criando a classe
class Camera:

    # 2 - Estado inicial do objeto
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    # 3 - Método que altera o estado
    def filmar(self):
        if self.filmando:
            print(f'{self.nome} JÁ está filmando...')
            return
        
        print(f'{self.nome} está filmando...')
        self.filmando = True        # muda estado

    # 4 - Método que altera o estado
    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} NÃO está filmando...')
            return
        
        print(f'{self.nome} está parando de filmar...')
        self.filmando = False

    # 5 - Método que depende do estado
    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando')
            return
        
        print(f'{self.nome} está fotografando...')

# 6 - Criando objetos
c1 = Camera('Canon')
c2 = Camera('Sony')

# 7 - Testando comportamento do c1
c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()

print()

# 8 - Testando comportamento do c2
c2.parar_filmar()
c2.filmar()
c2.filmar()
c2.fotografar()
c2.parar_filmar()
c2.fotografar()