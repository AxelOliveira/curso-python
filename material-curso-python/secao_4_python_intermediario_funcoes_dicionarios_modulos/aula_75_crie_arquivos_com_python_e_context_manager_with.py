"""
TEORIA - CRIAÇÃO DE ARQUIVOS + CONTEXT MANAGER (WITH)

1. A função open()é usada para abrir ou criar arquivos em Python.
2. Modos principais:
    - 'r' -> leitura (erro se não existir)
    - 'w' -> escrita (cria ou sobrescreve)
    - 'a' -> adiciona conteúdo no final
    - 'x' -> cria arquivo (erro se já existir)
    - '+' -> leitura e escrita juntos

3. Problema:
    - Quando abrimos um arquivo manualmente, precisamos fechar com .clos()
    - Se esquecer, pode gerar erros ou consumir recursos

4. Solução:
    - Usar "with" (Context Manager)
    - Ele abre e FECHA automaticamente o arquivo, mesmo com erro

5. IMPORTANTE:
    - print() NÃO escreve no arquivo
    - Para escrever no arquivo usamos:
        arquivo.write("texto")

6. Caminho do arquivo:
    - Relativo: mesmo diretório do script
    - Absoluto: caminho completo do sistema
"""
caminho_arquivo = 'aula75.txt'

# 1 - Abrindo o arquivo em modo escrita (cria ou sobrescreve)
with open(caminho_arquivo, 'w') as arquivo:

    # 2 - Tentando escrever no arquivo (FORMA CORRETA)
    arquivo.write('Olá mundo\n')

    # 3 - Escrevendo outra linha
    arquivo.write('Arquivo vai ser fechado\n')

    # 4 - Esse print NÃO vai para o arquivo (vai para o terminal)
    print('Isso aparece no terminal, não no arquivo')