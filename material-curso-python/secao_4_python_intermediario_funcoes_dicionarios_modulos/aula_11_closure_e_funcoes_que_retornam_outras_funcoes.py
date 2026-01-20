"""
Closure e funções que retornam outras funções

Closure é quando uma função interna continua tendo acesso às variáveis da função externa mesmo depois que essa função terminou.

Closure acontece quando:
- Uma função é criada dentro de outra
- A função interna usa variáveis da função externa
- Mesmo após a função externa terminar, a interna "lembra" desses valores
"""

def criar_saudacao(saudacao):
    # Função externa
    # O parâmetro 'saudaca' ficará armazenado na memória (closure)

    def saudar(nome):
        # Função interna
        # Usa a veriável 'saudacao' do escopo externo
        return f'{saudacao}, {nome}!'
    
    # Retorna a função interna, não o resultado dela
    return saudar

# Aqui criamos funções diferentes a partir da mesma função externa
# Cada uma "lembra" de um valor diferente de 'saudacao'
falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

# As funções retornadas continuam funcionando, porque o valor de 'saudacao' foi preservado (closure)
for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))