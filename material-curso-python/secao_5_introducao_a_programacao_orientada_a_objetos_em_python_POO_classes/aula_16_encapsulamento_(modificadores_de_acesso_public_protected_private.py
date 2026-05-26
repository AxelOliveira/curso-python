"""
Encapsulamento (modificadores de acesso)

Python NÃO possui modificadores de acesso reais, mas seguimos convenções da comunidade.

Public
- Sem underline
- Pode ser acessando em qualquer lugar

Protected
- Um underline (_)
- Não DEVE ser acessado fora da classe
- Pode ser usado dentro da classe e subclasses

Private
- Dois underlines (__)
- Sofre name mangling (desfiguração de nomes)
- Só DEVE ser usado dentro da própria classe

Name Mangling
- Python altera o nome internamente:
    _NomeDaClasse__nome
"""

class Foo:
    # 1 - Método construtor
    def __init__(self):
        # 2 - Atributo público
        self.public = 'isso é público'

        # 3 - Atributo protected
        self._protected = 'isso é protegido'

        # 4 - Atributo private
        self.__private = 'isso é private'

    # 5 - Método público
    def metodo_publico(self):
        print('MÉTODO PÚBLICO')

        # 6 - Acessando atributo private dentro da classe
        print(self.__private)

        # 7 - Chamando método protected
        self.__metodo_private()

        # 8 - Chamando método private
        self.__metodo_private()

        return 'metodo_publico'
    
    # 9 - Método protected
    def _metodo_protected(self):
        print('_metodo_protected')

        # 10 - Protected pode acessar outros atributos da classe
        print(self._protected)

        return '_metodo_protected'
    
    # 11 - Método private
    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_private'

# 12 - Criando o objeto    
f = Foo()

# ---------------- PUBLIC ----------------

# 13 - Atributos e métodos públicos
#      podem ser acessados fora da classe
print(f.public)
print(f.metodo_publico())

# ---------------- PROTECTED ----------------

# 14 - Isso FUNCIONA, mas NÃO DEVE ser feito
#      porque é um atributo protected
print(f._protected)

# 15 - Isso também FUNCIONA,
#      mas NÃO DEVE ser usado fora da classe
print(f._metodo_protected())

# ---------------- PRIVATE ----------------

# 16 - Isso gera erro:
# print(f.__private)

# 17 - Isso também gera erro:
# print(f.__metodo_private())

# 18 - Name Mangling
#      Python altera o nome internamente
print(f._Foo__private)

# 19 - Também é possível acessar
#      o método private dessa forma
print(f._Foo__metodo_private())