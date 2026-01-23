# Exercício - sistema de perguntas e respostas

# 1 - Definir a estrutura de dados que armazenará todas as perguntas.
# Cada pergunta é um dicionário dentro de uma lista
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

# 2 - Criar um contador para armazenar a quantidade de acertos
qtd_acertos = 0

# 3 - Percorrer todas as perguntas da lista, uma por vez
for pergunta in perguntas:

    # 4 - Exibir a pergunta atual para o usuário
    print('Pergunta:', pergunta['Pergunta'])
    print()

    # 5 - Obter a lista de opções da pergunta atual
    opcoes = pergunta ['Opções']

    # 6 - Exibir todas as opções com seus respectivos índices
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    # 7 - Receber a escolha do usuário (sempre vem como string)
    escolha = input('Escolha uma opção: ')

    # 8 - Criar variáveis de controle para validação da resposta
    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    # 9 - Verificar se a escolha digitada é numérica
    if escolha.isdigit():
        escolha_int = int(escolha)

    # 10 - Verificar se a escolha é válida (existe dentro das opções)
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:

            # 11 - Comparar a opção escolhida com a resposta correta
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()

    # 12 - Atualizar o contador e exibir o resultado da pergunta
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()

# 13 - Exibir o resultado final após todas as perguntas serem respondidas
print('Você acertou', qtd_acertos, 'de', len(perguntas), 'perguntas')