"""
AULA 81 - Lista de tarefas com desfazer e refazer

Conceitos principais:

1. PILHA (STACK)
- Usamos listas como pilha:
    append() -> adiciona no final
    pop() -> remove o último elemento (LIFO)

2. DESFAZER (UNDO)
- Remove a última tarefa da lista principal
- Guarda essa tarefa em outra lista (histórico de refazer)

3. REFAZER (REDO)
- Remove da lista de refazer
- Volta para a lista principal

4. REGRA IMPORTANTE (lógica real de sistemas):
- Se o usuário adiciona uma nova tarefa após desfazer, o histórico de refazer deve ser apagado

5. ORGANIZAÇÃO
- Separar responsabilidades em funções
- Melhor leitura e manutenção do código

6. EXPERIÊNCIA DO USUÁRIO
- Mensagens claras
- Tratamento de erros (lista vazia, input vazio)
"""

import os

def limpar():
    # 1 - Limpa o terminal dependendo do sistema operacional
    os.system('cls' if os.name == 'nt' else 'clear')

def listar(tarefas):
    # 2 - Mostra todas as tarefas
    print()

    # 2.1 - Verifica se a lista está vazia
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return
    
    # 2.2 - Exibe tarefas
    print('Tarefas:')
    for i, tarefa in enumerate(tarefas, start=1):
        print(f'{i}. {tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    # 3 - Remove a última tarefa (efeito CTRL + Z)
    print()

    # 3.1 - Verifica se há tarefas
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return
    
    # 3.2 - Remove a última tarefa
    tarefa = tarefas.pop()

    # 3.3 - Guarda para possível refazer
    tarefas_refazer.append(tarefa)

    print(f'"{tarefa}" removida da lista de tarefas.')
    print()

def refazer(tarefas, tarefas_refazer):
    # 4 - Reverter o desfazer (efeito CTRL + SHIFT + Z)
    print()

    # 4.1 - Verifica se há algo para refazer
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return
    
    # 4.2 - Recupera a última tarefa desfeita
    tarefa = tarefas_refazer.pop()

    # 4.3 - Volta para lista principal
    tarefas.append(tarefa)

    print(f'"{tarefa}" adiciona novamente na lista')
    print()

def adicionar(tarefa, tarefas, tarefas_refazer):
    # 5 - Adiciona nova tarefa
    print()

    # 5.1 - Remove espaços extras
    tarefa = tarefa.strip()

    # 5.2 - Validação
    if not tarefa:
        print('Você não digitou uma tarefa')
        return

    # 5.3 - Adiciona tarefa
    tarefas.append(tarefa)

    # 5.4 - REGRA IMPORTANTE:
    # Se adicionou algo novo, perde histórico de refazer
    tarefas_refazer. clear()

    print(f'"{tarefa}" adicionada na lista de tarefas')
    print()

# 6 - Estruturas principais
tarefas = []   
tarefas_refazer = []

# 7 - Loop principal do sistema
while True:
    print('Comandos: listar, desfazer, refazer, clear')
    entrada = input('Digite uma tarefa ou comando: ')

    # 7.1 - Comando listar
    if entrada == 'listar':
        listar(tarefas)
        continue

    # 7.2 - Comando desfazer
    elif entrada == "desfazer":
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue

    # 7.3 - Comando refazer
    elif entrada == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue

    # 7.4 - Limpar tela
    elif entrada == 'clear':
        limpar()
        continue

    # 7.5 - Caso seja uma nova tarefa
    else:
        adicionar(entrada, tarefas, tarefas_refazer)
        continue