"""
🔹 @staticmethod
- NÃO recebe "self"
- NÃO recebe "cls"
- Não tem acesso à instância nem à classe
- É basicamente uma função dentro da classe

💡 Ideia principal:
É uma função comum, mas organizada dentro da classe.

💡 Diferença principal:
- Função normal -> solta no código
- Static method -> "dentro" da classe (organização)

⚠️ Importante:
Ele não consegue acessar atributos da classe nem da instância.
"""
class Classe:
    @staticmethod
    # 1 - Função que NÃO usa self nem cls
    def funcao_que_esta_na_classe(*args, **kwargs):
        print('Oi', args, kwargs)

# 2 - Função normal fora da classe
def funcao(*args, **kwargs):
        print('Oi', args, kwargs)

# 3 - Criando objeto
c1 = Classe()

# 4 - Chamando statick method pela instância
c1.funcao_que_esta_na_classe(1, 2, 3)

# 5 - Chamando função normal
funcao(1, 2, 3)

# 6 - Chamando static method pela classe
Classe.funcao_que_esta_na_classe(nomeado=1)

# 7 - Chamando função normal novamente
funcao(nomeado=1)