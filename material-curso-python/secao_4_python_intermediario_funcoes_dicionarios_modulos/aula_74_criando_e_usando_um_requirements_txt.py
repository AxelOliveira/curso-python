"""
Aula: Criando e usando requirements.txt

Resumo:
O arquivo requirements.txt é usado para salvar todas as dependências
(bibliotecas) de um projeto Python.

Ele permite:
- Recriar o ambiente virtual em outra máquina
- Evitar subir a pasta do ambiente virtual (venv) no GitHub
- Garantir que o projeto use as mesmas versões das bibliotecas

Fluxo básico:
1. Instalar bibliotecas com pip
2. Gerar o requirements.txt com pip freeze
3. Compartilhar apenas o código + requirements.txt
4. Reinstalar tudo com pip install -r requirements.txt
"""

# 1 - Listar bibliotecas instaladas no ambiente virtual
# pip freeze

# 2 - Criar o arquivo requirements.txt com todas as dependências
# pip freeze > requirements.txt

# 3 - O arquivo requirements.txt contém:
# nome_da_biblioteca==versao

# 4 - NÃO subir a pasta do ambiente virtual (venv) para o GitHub
# (ela deve estar no .gitignore)

# 5 - Apagar o ambiente virtual (simulando outro computador)
# (deletar a pasta venv)

# 6 - Criar um novo ambiente virtual
# python -m venv venv

# 7 - Ativar o ambiente virtual

# Windows:
# .\venv\Scripts\activate

# Linux/Mac:
# source venv/bin/activate

# 8 - Reinstalar todas as dependências do projeto
# pip install -r requirements.txt

# 9 - Verificar se tudo foi instalado corretamente
# pip freeze

# 10 - Sempre que instalar uma nova biblioteca:
# atualizar o requirements.txt novamente
# pip freeze > requirements.txt