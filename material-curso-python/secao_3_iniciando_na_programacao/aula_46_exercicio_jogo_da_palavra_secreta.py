"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""
# CheckList
# O que o programa precisa fazer? Verificar se a letra digitada está na palavra secreta.
# O que o usuário vai digitar? O usuário vai precisar digitar letra (string).
# O que o programa deve decidir? Verificar se a letra informada está correta dentro da palavra secreta.
# O que deve ser exibido no final? A palavra secreta.
# O código precisa repetir? Sim, até o usuário acertar a palavra secreta.
# O que vai ficar em loop? As tentativas do usuário.
# Quando o loop deve parar? Quando todas as letras necessárias forem descobertas.
# Quais variáveis precisam existir fora do loop? * Palavra secreta; * Tentativas; * Letras já acertadas
# Qual é a condição principal? Letra está ou não está na palavra
# Qual variável controla a condição? A entra do usuário influencia a condição, mas quem realmente controla o loop é o estado da palavra(letras acertadas)
# A condição é True ou False quando? A condiçao final é True quando a palavra foi completamente revelada
# Onde pode dar erro? Na entrada do usuário, pois ele pode inserir mais de uma letra, números ou caracteres
# Onde colocar o breakpoints? Na primeira linha do while, na linha do input, na condição princial(if letra in palavra), onde você atualiza as letras acertadas, na condição de parada do jogo, no break

"""O programa repete até o usuário acertar a palavra.
Em cada repetição, ele pede uma letra, verifica se está certa, mostra o resultado e conta a tentativa."""

# 1 - Definição de valores fixos
PALAVRA_SECRETA = 'seventeen'                                                  # Define a palavra que o usuário precisa adivinhar
tentativas = 0                                                                 # Conta quantas tentativas o usuário já fez
letras_acertadas = ''                                                          # Guarda todas as letras corretas já digitadas

# 2 - Início do loop principal
while True:                                                                    # Loop infinito: o jogo continua até o break

    # 3 - Entrada do usuário
    letra_usuario = input('Digite uma letra: ').lower()
                                                                               # Pede uma letra ao usuário e converte para minúscula

    # 4 - Atualização de estado
    tentativas += 1                                                            # Incrementa o número de tentativas a cada jogada

    # 5 - Verificação da letra
    if letra_usuario in PALAVRA_SECRETA:                                       # Verifica se a letra digitada existe na palavra secreta
        if letra_usuario not in letras_acertadas:
            letras_acertadas += letra_usuario                                  # Salva a letra correta (evita repetir a mesma letra)

    # 6 - Exibição do progresso
    palavra_formada = ''                                                       # Variável que vai montar a palavra com letras ou '*'

    for letra in PALAVRA_SECRETA:                                              # Percorre cada letra da palavra secreta
        if letra in letras_acertadas:                                          # Se a letra já foi acertada
            palavra_formada += letra                                           # Adiciona a letra real na palavra formada
        else:                                                                  # Se a letra ainda não foi acertada
            palavra_formada += '*'                                             # Adiciona um * no lugar da letra

    print('Palavra:', palavra_formada)                                         # Mostra o progresso atual da palavra ao usuário

    # 7 - Condição de parada
    if palavra_formada == PALAVRA_SECRETA:                                     # Verifica se todas as letras já foram descobertas
        print('\nVOCÊ GANHOU PARABÉNS!!!')                                     # Mensagem de vitória
        print(f'A palavra era: {PALAVRA_SECRETA}')                             # Mostra a palavra secreta
        print(f'Tentativas: {tentativas}')                                     # Mostra quantas tentativas o usuário fez
        break                                                                  # Encerra o loop e finaliza o jogo
    
#------------------------------------------------------------------------------------------------------------------------------------

#RESPOSTA DO PROFESSOR

import os                                                                    # Importa o módulo os para executar comandos do sistema (ex: limpar a tela)

palavra_secreta = 'perfume'                                                  # Define a palavra que o usuário precisa adivinhar
letras_acertadas = ''                                                        # Guarda as letras que o usuário acertou
numero_tentativas = 0                                                        # Conta quantas tentativas o usuário já fez

while True:                                                                  # Loop principal do jogo (só para quando houver break ou reset lógico)
    letra_digitada = input('Digite uma letra: ')                             # Pede uma letra ao usuário
    numero_tentativas += 1                                                   # Incrementa o contador de tentativas

    if len(letra_digitada) > 1:                                              # Verifica se o usuário digitou mais de um caractere
        print('Digite apenas uma letra.')                                    # Mostra mensagem de erro
        continue                                                             # Volta para o início do loop sem executar o restante do código

    if letra_digitada in palavra_secreta:                                    # Verifica se a letra está na palavra secreta
        letras_acertadas += letra_digitada                                   # Salva a letra correta no histórico

    palavra_formada = ''                                                     # Variável que vai montar a palavra com letras e '*'

    for letra_secreta in palavra_secreta:                                    # Percorre cada letra da palavra secreta
        if letra_secreta in letras_acertadas:                                # Se a letra já foi acertada
            palavra_formada += letra_secreta                                 # Mostra a letra real
        else:                                                                # Se ainda não foi acertada
            palavra_formada += '*'                                           # Mostra '*'

    print('Palavra formada:', palavra_formada)                               # Exibe o progresso atual do jogador

    if palavra_formada == palavra_secreta:                                   # Verifica se o jogador acertou a palavra inteira
        os.system('clear')                                                   # Limpa a tela do terminal
        print('VOCÊ GANHOU!! PARABÉNS!')                                     # Mensagem de vitória
        print('A palavra era', palavra_secreta)                              # Mostra a palavra correta
        print('Tentativas:', numero_tentativas)                              # Mostra o total de tentativas
        letras_acertadas = ''                                                # Reseta as letras acertadas
        numero_tentativas = 0                                                # Reseta o contador de tentativas