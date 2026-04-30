"""
@property - Getter no modo Pythonico

O que é:
- @property transforma um método em um "atributo"
- Você acessa sem parênteses

Diferença:
- Método comum -> obj.metodo()
- Property -> obj.atributo

Por que usar:
1. Evitar quebrar código (encapsulamento)
2. Esconder lógica interna
3. Executar ações ao acessar um valor
4. Tornar o código mais Pythonico

Regra importante:
- property NÃO usa ()
- é um método que se comporta como atributo

Quando usar:
- quando algo "parece um dado", não uma ação
"""

# =========================
# EXEMPLO 1 (SEM PROPERTY)
# =========================

class Pen:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color
    
pen = Pen('Blue')

# 1 - Chamando como método (forma tradicional)
print(pen.get_color())
print(pen.get_color())

# =========================
# EXEMPLO 2 (COM PROPERTY)
# =========================

class Pen:
    def __init__(self, color):
        self._color = color       # 1 - atributo interno (convencao)

    @property
    def color(self):
        # 2 - executa ação ao acessar
        print('ACCESSING COLOR')
        return self._color
    
pen = Pen('Orange')

# 3 - Chamando como atributo (sem parênteses)
print(pen.color)
print(pen.color)

# =========================
# EXEMPLO 3 (PROTEGENDO O CÓDIGO)
# =========================

class Pen:
    def __init__(self, color):
        self._ink_color = color       # 1 - nome interno mudou

    @property
    def color(self):
        # 2 - código externo continua funcionando
        return self._ink_color
    
pen = Pen('Black')

# 3 - Código cliente NÃO quebra
print(pen.color)

# =========================
# EXEMPLO 4 (APLICANDO NO SEU CONTEXTO)
# =========================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def is_adult(self):
        # 1 - lógica escondida
        return self.age >= 18
    
person = Person('Wonwoo', 20)

# 2 - uso como atributo
print(person.is_adult)