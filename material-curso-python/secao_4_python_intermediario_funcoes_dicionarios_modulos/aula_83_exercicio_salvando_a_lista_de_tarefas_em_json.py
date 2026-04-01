"""
CONCEITO PRINCIPAL:
- Memória do programa é temporária (RAM)
- JSON permite salvar dados em disco (arquivo)

FLUXO DO PROGRAMA:
1. Ao iniciar -> tenta ler o arquivo JSON
2. Se não existir -> cria lista vazia
3. Durante execução -> altera lista em memória
4. Após cada ação -> salva no arquivo

PONTO CRÍTICO:
A função ler() PRECISA sempre retornar uma lista válida
-> se retornar None -> quebra o programa (erro de append)

CONCEITO IMPORTANTE:
- json.load -> lê arquivo -> Python (dict/list)
- json.dump -> salva Python -> arquivo JSON

ESTRATÉGIA USADA:
- Lista de tarefas = fonte principal
- JSON = armazenamento persistente
"""
import json
import os

def listar(tarefas):
    print()

    # 1 - Guard clause: evita execução desnecessária
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return
    
    # 2 - Exibe tarefas
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()

def desfazer(tarefas, tarefas_refazer):
    print()

    # 3 - Verifica se há o que desfazer
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return
    
    # 4 - Remove última tarefa (estrutura de pilha)
    tarefa = tarefas.pop()

    # 5 - Guarda para possível refazer
    tarefas_refazer.append(tarefa)

    print(f'{tarefa=} removida da lista de tarefas.')
    print()

    listar(tarefas)

def refazer(tarefas, tarefas_refazer):
    print()

    # 6 - Verifica se há o que refazer
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return
    
    # 7 - Recupera tarefa
    tarefa = tarefas_refazer.pop()

    # 8 - Reinsere na lista principal
    tarefas.append(tarefa)

    print(f'{tarefa=} adicionada na lista de tarefas.')
    print()

    listar(tarefas)

def adicionar(tarefa, tarefas):
    print()

    # 9 - Limpa entrada
    tarefa = tarefa.strip()

    # 10 - Valida entrada
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    
    # 11 - Adiciona tarefa
    tarefas.append(tarefa)

    print(f'{tarefa=} adicionada na lista de tarefas.')
    print()

    listar(tarefas)

def ler(caminho_arquivo):
    # 12 - Tenta carregar dados do arquivo
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            return json.load(arquivo)
        
    # 13 - Se arquivo não existir -> retorna lista vazia
    except FileNotFoundError:
        print('Arquivo não existe')
        return []
    
def salvar(tarefas, caminho_arquivo):
    # 14 - Salva lista no arquivo JSON
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)

CAMINHO_ARQUIVO = 'aula83.json'

# 15 - Inicializa lista a partir do arquivo
tarefas = ler(CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    # 16 - Mapeamento de comandos -> funções
    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('clear'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }

    # 17 - Busca comando ou usa adicionar como padrão
    comando = comandos.get(tarefa, comandos['adicionar'])

    # 18 - Executa comando
    comando ()

    # 19 - Persiste dados após cada ação
    salvar(tarefas, CAMINHO_ARQUIVO)