"""
AULA: Positional-only e Keyword-only

IDEIA PRINCIPAL:
Controlar COMO os argumentos podem ser passados para uma função.

REGRAS:
1. Tudo antes de / -> somente POSICIONAL
2. Tudo depois de * -> somente NOMEADO
3. **kwargs -> captura argumentos nomeados extras

- a, b -> só posição
- c -> só nome
"""
def soma(a, b, /, *, c, **kwargs):

    # 1 - Mostrar argumentos extras nomeados
    print(kwargs)

    # 2 - Somar os valores obrigatórios
    print(a + b + c)

# 3 - Chamada correta da função
# a e b -> posicionais
# c -> nomeado
# nome -> vai para kwargs
soma(1, 2, c=3, nome='teste')