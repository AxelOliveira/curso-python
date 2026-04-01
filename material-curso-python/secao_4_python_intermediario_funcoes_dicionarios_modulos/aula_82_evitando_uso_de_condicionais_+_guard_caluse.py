"""
PROBLEMA PRINCIPAL:
O erro 'NoneType has no attribute append' acontece quando a variável esperada como lista na verdade é None.

Isso ocorre quando uma função NÃO retorna um valor consistente.

No nosso caso:
- A função ler() precisava SEMPRE retornar uma lista
- Se o arquivo não existesse, ela retornava None (ou comportamento inconsistente)
- Depois, ao usar tarefas.append(), quebrava o código

SOLUÇÃO:
Garantir que a função ler() SEMPRE retorne uma lista:
- Se der erro -> retorna []
- Se funcionar -> retorna json.load()

OUTRO CONCEITO IMPORTANTE:
Uso de dicionário de comandos:
- Evita vários if/elif
- Permite mapear strings -> funções

CUIDADO:
- Funções dentro do dicionário NÃO podem ser executadas direto
- Por isso usamos lambda (adiar execução)

MELHORIA:
Usar comandos.get(chave, padrão) ao invés de if/else
"""

import json
import os

def listar(tarefas):
    print()

    # 1 - Se não houver tarefas, encerrar função (guard clause)
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return
    
    # 2 - Exibir tarefas
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()

def desfazer(tarefas, tarefas_refazer):
    print()

    # 3 - Verifica se há tarefas para desfazer
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return
    
    # 4 - Remove última tarefa (pilha - LIFO)
    tarefa = tarefas.pop()

    # 5 - Move para a lista de refazer
    tarefas_refazer.append(tarefa)

    print(f'{tarefa=} removida da lista de tarefas.')
    print()

    # 6 - Atualiza visualização
    listar(tarefas)

def refazer(tarefas, tarefas_refazer):
    print()

    # 7 - Verifica se há tarefas para refazer
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return
    
    # 8 - Recupera última tarefa desfeita
    tarefa = tarefas_refazer.pop()

    # 9 - Retorna para lista principal
    tarefas.append(tarefa)

    print(f'{tarefa=} adicionada na lista de tarefas')
    print()

    # 10 - Atualiza visualização
    listar(tarefas)

def adicionar(tarefa, tarefas):
    print()

    # 11 - Remove espaços extras
    tarefa = tarefa.strip()

    # 12 - Valida entrada
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    
    # 13 - Adiciona tarefa
    tarefas.append(tarefa)

    print(f'{tarefa=} adicionada na lista de tarefas')
    print()

    # 14 - Atualiza visualização
    listar(tarefas)

def ler(caminho_arquivo):
    # 15 - Tenta ler o arquivo
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            return json.load(arquivo)
        
    # 16 - Se arquivo não existir -> retorna lista vazia
    except FileNotFoundError:
        print('Arquivo não existe')
        return []
    
def salvar(tarefas, caminho_arquivo):
    # 17 - Salva lista no JSON
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)

CAMINHO_ARQUIVO = 'aula83.json'

# 18 - Carrega dados (sempre será lista)
tarefas = ler(CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer, refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    # 19 - Dicionário de comandos (evita if)
    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('clear'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }

    # 20 - Busca comando ou usa adicionar como padrão
    comando = comandos.get(tarefa, comandos['adicionar'])

    # 21 - Executa função
    comando()

    # 22 - Salva automaticamente após qualquer ação
    salvar(tarefas, CAMINHO_ARQUIVO)