# while é usado para quando não sabe exatamente quando termina
# for é usado para quando sabe exatamente quando termina

for i in range(10):                                             # Loop externo: i vai de 0 até 9
    if i == 2:                                                  # Verifica se o valor atual de i é 2
        print('i é 2, pulando...')                              # Informa que i é 2 e que essa volta será ignorada
        continue                                                # Pula o resto do código dessa iteração e volta para o início do for com o próximo i
    
    if i == 8:                                                  # Verifica se o valor atual de i é 8
        print('i é 8, seu else não executará')                  # Mostra mensagem avisando que o break será usado
        break                                                   # Encerra o loop for imediatamente e impede a execução do else do for

    for j in range(1, 3):                                       # Loop interno: j vai de 1 até 2
        print(i, j)                                             # Mostra o valor atual de i (externo) e o valor atual de j (interno)

else:                                                           # Esse else só executa se o for terminar sem usar break
    print('For completo com sucesso!')                          # Mensagem exibida apenas se NÃO houver break