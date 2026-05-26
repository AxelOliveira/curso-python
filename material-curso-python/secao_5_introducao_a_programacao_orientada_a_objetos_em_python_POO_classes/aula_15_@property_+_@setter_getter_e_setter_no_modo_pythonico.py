"""
@property + @setter - getter e setter no modo Pythônico

@property
- Getter no modo Pythônico
- Usado para obter um valor
- Permite executar ações ao acessar um atributo
- Ajuda a evitar quebrar código cliente

@setter
- Setter no modo Pythônico
- Usado para configurar um valor
- Permite validar ou restringir dados antes de salvar

Convenção do underline (_)
- Atributos que começam com _ou __ não devem ser usados fora da classe
- Indicam que o atributo é interno da classe
"""
class Caneta:
    # 1 - Método construtor
    def __init__(self, cor):
        # 2 - Chamando o setter diretamente
        #     Assim toda validação do setter também acontece no __init__
        self.cor = cor

        # 3 - Atributo interno da classe
        self._cor_tampa = None

    # 4 - Getter da cor
    @property
    def cor(self):
        print('ESTOU NO GETTER')
        return self._cor
    
    # 5 - Setter da cor
    @cor.setter
    def cor(self, valor):
        print('ESTOU NO SETTER')

        # 6 - Exemplo de validação
        if valor == 'Rosa':
            raise ValueError('Não aceito essa cor.')
        
        # 7 - Salvando o valor no atributo interno
        self._cor = valor

    # 8 - Getter da cor da tampa
    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    # 9 - Setter da cor da tampa
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor

# 10 - Criando o objeto
caneta = Caneta('Azul')

# 11 - Alterando a cor usando o setter
caneta.cor = 'Rosa'

# 12 - Alterando a cor da tampa
caneta.cor_tampa = 'Roxa'

# 13 - Obtendo os valores usando os getters
print(caneta.cor)
print(caneta.cor_tampa)