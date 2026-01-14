"""
Argumento nomeados e não nomeados em funções Python
Argumento nomeado: Você fala exatamente qual valor vai para qual parâmetro, usando =
soma(x=1, y=2, z=3)

Argumento não nomeado: Você passa só os valores, e o python coloca cada valor na ordem dos parâmetros, exemplo:
def soma(x, y, z):
    print(x + y + z)

soma(1, 2, 3)    O python entende assim: x=1 ; y=2; z=3

# Depois que um parametro é nomeado, todos os proximos precisam ser nomeados tambem:
    Exemplo (1, y=2 , (depois do y, todos precisam ser nomeados)) tudo nomeado ou nada nomeado

Não pode enviar argumentos posicionais após argumentos nomeados
"""

# 1 - Criação da função, não executa
def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y +z)

# 2 - Argumentos não nomeados e seguem a ordem x, y, z
soma(1, 2, 3)

soma(1, y=2, z=5)

print(1, 2, 3, sep='-')