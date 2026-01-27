"""
Exemplo prático de uso do tipo set

Objetivo:
- Armazenar letras digitadas pelo usuário
- Evitar letras repetidas automaticamente
- Verificar se uma letra específica já foi digitada
"""

# Criando um set vazio para armazenar letras únicas
letras = set()

# Loop infinito para receber entradas do usuário
while True:
    letra = input('Digite: ')

    # Normaliza a letras para minúscula e adiciona ao set
    letras.add(letra.lower())

    # Verifica se a letra 'l já foi digitada
    if 'l' in letras:
        print('PARABÉNS')
        break

    # Mostra todas as letras digitadas até agora
    print(letras)