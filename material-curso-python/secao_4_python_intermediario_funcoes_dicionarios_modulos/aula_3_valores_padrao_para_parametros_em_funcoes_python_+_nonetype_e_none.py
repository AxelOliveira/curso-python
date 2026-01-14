"""
Valores padrão para parâmetros
Quando você cria uma função, pode deixar um valor "pré-definifo" para algum parâmetro:
    - Se você não enviar um valor, o Python usa o valor padrão
    - Se você enviar um valor, o valor enviado substitui o padrão

Refatorar: editar o seu código para melhorar, sem mudar o que ele faz
"""

# 1 - Se ninguém mandar z, ele será None
def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)
soma(y=9, z=0, x=7)