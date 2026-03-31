"""
TEORIA - JSON (SALVAR E CARREGAR DADOS)

1. JSON é um formato de dados usado para salvar informações

2. Muito usado porque:
    - é simples
    - funciona em várias linguagens
    - ideal para APIs e arquivos

3. Conversões importantes:

   PYTHON        → JSON
   dict          → object
   list/tuple    → array
   str           → string
   int/float     → number
   True          → true
   None          → null

4. Funções principais:

    - json.dump()  -> salva em arquivo
    - json.load()  -> lê de arquivo

5. Limitações:
    - não suporta: set, funções, classes

6. encoding:
    - sempre usar 'utf-8'
"""

import json

pessoa = {
    'nome': 'Jeon',
    'sobrenome': 'Wonwoo',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

# 1 - Salvando no JSON
with open('aula79.json', 'w', encoding='utf-8') as arquivo:
    json.dump(
        pessoa,                     # 2 - dados
        arquivo,                    # 3 - arquivo
        ensure_ascii=False,         # 4 - mantém acentos
        indent=2,                   # 5 - formatação bonita
    )

# 6 - Lendo do JSON
with open('aula79.json', 'r', encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo)

# 7 - Usando o dado normalmente
print(pessoa['nome'])