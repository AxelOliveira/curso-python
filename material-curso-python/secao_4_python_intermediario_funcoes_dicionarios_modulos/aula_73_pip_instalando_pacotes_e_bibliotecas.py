"""
Aula: pip - instalando pacotes e bibliotecas

Resumo:
O pip é o gerenciador de pacotes do Python.

Ele é usado para instalar, atualizar e remover bibliotecas externas
(ou seja, coisas que não vêm junto com o Python).

Quando o ambiente virtual está ativo:
- Os pacotes são instalados dentro do ambiente virtual
- Não afetam o Python global do sistema

Quando o ambiente virtual NÃO está ativo:
- Os pacotes são instalados globalmente (não recomendado)

Dependências:
- Um pacote pode instalar outros automaticamente
- Isso acontece porque ele depende de outras bibliotecas

Arquivo requirements.txt:
- Lista todos os pacotes e versões do projeto
- Permite recriar o ambiente em outra máquina

Principais comandos:

Instalar pacote:
    pip install nome_do_pacote

Desinstalar pacote:
    pip uninstall nome_do_pacote

Listar pacotes:
    pip freeze

Atualizar pacote:
    pip install nome_do_pacote --upgrade

Instalar versão específica:
    pip install nome_do_pacote==versao

Criar requirements.txt:
    pip freeze > requirements.txt

Instalar via requirements.txt:
    pip install -r requirements.txt

Alternativa mais segura (Windows):
    python -m pip install nome_do_pacote
"""

# 1 - Garantir que o ambiente virtual está ativo
# (ex: aparece (venv) no terminal)

# 2 - Verificar versão do pip
# pip --version

# 3 - Atualizar o pip (opcional, mas recomendado)
# python -m pip install --upgrade pip

# 4 - Instalar um pacote
# pip install pymysql

# 5 - Verificar se o pacote foi instalado
# pip freeze

# 6 - Importar no código (exemplo)
# import pymysql

# 7 - Desinstalar um pacote
# pip uninstall pymysql

# 8 - Desinstalar sem confirmação
# pip uninstall pymysql -y

# 9 - Instalar uma versão específica
# pip install pymysql==1.0.2

# 10 - Atualizar um pacote
# pip install pymysql --upgrade

# 11 - Ver versões disponíveis de um pacote
# pip index versions pymysql

# 12 - Criar arquivo de dependências
# pip freeze > requirements.txt

# 13 - Instalar dependências de um projeto
# pip install -r requirements.txt

# 14 - Caso o pip dê erro no Windows
# usar:
# python -m pip install nome_do_pacote

# 15 - Atenção:
# Se o ambiente virtual não estiver ativo,
# pode ocorrer erro de import (ModuleNotFoundError)