"""
🧩 Exercício 1 — for “por baixo dos panos”
Dado o texto abaixo:
- texto = 'Python'
👉 Faça duas versões que imprimem cada letra:
1. Usando for
2. Usando iter() + next() + while + try/except
🎯 Treinar:
 * iterável
 * iterador
 * StopIteration
 * entender o que o for faz internamente
"""
# 1. Definição do interável (string é iterável)
texto = 'Python'

# 2 - Versão simples usando for (python cuida do iterador internamente)
for letra in texto:                                      # Percorre cada caractere da string
    print(letra)                                         # imprime a letra atual

print()

# 3 - Criação manual do iterador 
iterador = iter(texto)                                    # transforma o iterável em iterador

# 4 - Loop infinito para simular o for
while True:                                               
    try:    
        # 5 - Pega o próximo valor do iterador                                              
        letra = next(iterador)
        print(letra)
    except StopIteration: 
        # 6 - Quando acabar, sai do loop
        break                                             

#-------------------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 2 — simulando o for com while
Sem usar for, percorra um range(5) usando:
- iter()
- next()
- while True
- try/except
Saída esperada:
0
1
2
3
4
🎯 Treinar:
- range como iterável
- controle manual do loop
"""
# 1 - Criação do iterável range (5)
contador = range(0, 4)

# 2 - Criação do iterador manual
iterador = iter(contador)

# 3 - Loop infinito simulando o for
while True:
    try: 
        # 4 - Obtém o próximo número
        numero = next(iterador)
        print(numero)
    except StopIteration:
        # 5 - Final do iterador
        break

#-------------------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 3 — while com condição controlada
Crie um while que:
- Peça um número ao usuário
- Continue pedindo enquanto o número for menor que 10
- Quando sair naturalmente do while, exiba:
- Número válido!
🎯 Treinar:
- while com condição
- saída natural do loop
"""
# 1 - Entrada inicial do usuário
numero_usuario = float(input('Digite um número: '))

# 2 - Enquanto o número for menor que 10, continua pedindo
while numero_usuario < 10:
    print('Número inválido, tente novamente')
    numero_usuario = float(input('Digite um número: '))

else: 
    # 3 - Executa quando o while termina SEM break
    print('Número válido informado')

#-------------------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 4 — while + break
Crie um programa que:
- Peça números ao usuário                        (condição inicial)
- Se digitar 0, use break                        (condição para encerrar o loop)
- Caso contrário, continue pedindo               (condição para continuar)
Depois do loop, mostre:
- Loop encerrado
🎯 Treinar:
- diferença entre condição e break
"""
# 1 - Loop infinito
while True:
    # 2 - Entrada do usuário
    numero_usuario = float(input('Digite um número: '))

    # 3 - Condição de parada
    if numero_usuario == 0:
        print('Loop encerrado')
        break

#-------------------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 5 — for + continue
Use for com range(10) e:                            
- Pule o número 5 usando continue                   
- Imprima os demais números                         
🎯 Treinar:
- continue no for
- fluxo do loop
"""
# 1 - Loop de 1 até 10
for i in range(1, 11):
    # 2 - Se for 5, pula
    if i == 5:
        print('i é 5, pulando...')
        continue
    
    # 3 - Imprime os demais
    print(i)

#-------------------------------------------------------------------------------------------------------------------
        
"""
🧩 Exercício 6 — for + break + else
Use for com range(1, 6):                            (condição inicial)
- Se encontrar o número 4, use break                (condição final)
- Se NÃO encontrar, o else deve executar            (condição para continuar)
🎯 Treinar:
- for + else
- impacto do break no else
"""
# 1 - Loop de 1 até 5
for i in range(1, 6):
    # 2 - Se encontrar o número 4
    if i == 4:
        print('Número encontrado')
        break
    print(i)
else:
    # 3 - Executa somente se NÃO houve break
    print('Número não encontrado')

#-------------------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 7 — exibindo letras ou *
Dada a palavra secreta:
- palavra_secreta = 'python'
- letras_acertadas = 'pt'
Mostre na tela:
- p*t*** 
🎯 Treinar:
- for em string
- comparação letra por letra
- estado (letras_acertadas)
"""
PALAVRA_SECRETA = 'python'
letras_acertadas = 'pt'

# 1 - Percorre a palavra secreta
for letra in PALAVRA_SECRETA:
    # 2 - Se a letra foi acertada
    if letra in letras_acertadas:
        print(letra, end='')
    else:
        # 3 - Caso contrário, imprime *
        print('*', end='')

#-------------------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 8 — contagem de tentativas
Crie um while que:
- Peça letras ao usuário                                    (condição inicial)
- Conte quantas tentativas foram feitas                     (condição para continuar)                   
- Pare após 5 tentativas usando break                       (condição final)
🎯 Treinar:
- while infinito
- controle manual de parada
"""

# 1 - Contador de tentativas
tentativas = 0

# 2 - Loop infinito
while True:
    letra_usuario = input('Insira uma letra: ')
    tentativas += 1

    # 3 - Condição de parada
    if tentativas == 5:
        print('Limite de tentativas atingido')
        break

#-------------------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 9 — validação de entrada
Peça uma letra ao usuário:                                              (condição inicial)
- Se digitar mais de uma letra → mostre erro e use continue             (condição para erro)
- Caso contrário, prossiga normalmente                                  (conição para encerrar)
🎯 Treinar:
- continue
- validação antes de executar o resto do loop
"""
while True:
    # 1 - Entrada do usuário
    letra_usuario = input('Digite uma letra: ')

    # 2 - Validação
    if len(letra_usuario) > 1:
        print('Erro: digite apenas uma letra')
        continue

    # 3 - Entrada válida
    print('Letra válida: ', letra_usuario)

#-------------------------------------------------------------------------------------------------------------------

"""
🧩 Exercício 10 — mini jogo da palavra (versão guiada)
Faça um jogo que:
- Tenha uma palavra secreta
- Mostre * para letras não acertadas
- Conte tentativas
- Use while True
- Pare quando a palavra estiver completa
⚠️ Não copie o jogo pronto
👉 Reescreva seguindo esta ordem:
1. variáveis fora do loop
2. loop principal
3. entrada
4. atualização de estado
5. verificação
6. exibição
7. condição de parada
🎯 Treinar:
- tudo que você estudou até agora
"""

# 1. Variáveis fora do loop
PALAVRA_SECRETA = 'wonwoo'
tentativas = 0
letras_acertadas = ''

# 2. Inicio do loop
while True:

    # 3. entrada do usuario
    letra_usuario = input('Digite uma letra: ')

    # 4. atualização de estado
    tentativas += 1

    # 5. Verificação da letra
    if letra_usuario in PALAVRA_SECRETA:
        if letra_usuario not in letras_acertadas:
            letras_acertadas += letra_usuario
    
    # 6. Exibição do progresso
    palavra_formada = ''

    for letra in PALAVRA_SECRETA:
        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += '*'

    print('Palavra: ', palavra_formada)

    # 7. Condição de parada
    if palavra_formada == PALAVRA_SECRETA:
        print('\nVOCÊ GANHOU PARABÉNS!!!')
        print(f'A palavra era: {PALAVRA_SECRETA}')                             # Mostra a palavra secreta
        print(f'Tentativas: {tentativas}')                                     # Mostra quantas tentativas o usuário fez
        break