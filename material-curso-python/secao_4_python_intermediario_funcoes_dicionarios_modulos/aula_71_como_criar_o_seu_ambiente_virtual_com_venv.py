"""
AULA 71 - COMO CRIAR UM AMBIENTE VIRTUAL (venv)

Nesta aula aprendemos como CRIAR um ambiente virtual na prática.

CONTEXTO:
- Um ambiente virtual é uma pasta com uma cópia do Python
- Tudo que for instalado nele fica isolado do sistema global

IMPORTANTE:
- Funciona em Windows, Linux e Mac
- O comando de criação é o mesmo em todos os sistemas

COMANDO PRINCIPAL:
python -m venv nome_do_ambiente

EXPLICAÇÃO:
- python → executa o Python
- -m → executa um módulo como script
- venv → módulo responsável por criar o ambiente virtual
- nome_do_ambiente → nome da pasta que será criada

ESTRUTURA CRIADA:

Windows:
- venv/
    - Scripts/  → executáveis (python, pip, activate)
    - Lib/      → bibliotecas instaladas
    - Include/  → arquivos internos

Linux/Mac:
- venv/
    - bin/      → executáveis
    - lib/      → bibliotecas
    - include/  → arquivos internos

OBSERVAÇÃO IMPORTANTE:
- A versão do Python usada para criar o venv será a mesma dentro dele
"""

# =========================================================
# CRIANDO UM AMBIENTE VIRTUAL
# =========================================================

# 1. Executar no terminal dentro do projeto
# python -m venv venv

# 2. Isso cria uma pasta chamada "venv"
# 3. Dentro dela fica uma cópia do Python
# 4. Ainda NÃO está ativo


# =========================================================
# EXPLICAÇÃO EM PENSAMENTO COMPUTACIONAL
# =========================================================

# 1. O Python recebe o comando "-m venv"
# 2. Ele executa o módulo venv
# 3. O módulo cria uma nova pasta (ambiente virtual)
# 4. Dentro dessa pasta ele copia:
#    - executável do Python
#    - pip
#    - estrutura de bibliotecas
# 5. Esse ambiente fica isolado do sistema global


# =========================================================
# ESTRUTURA DO AMBIENTE (WINDOWS)
# =========================================================

# venv/
# ├── Scripts/
# │   ├── python.exe
# │   ├── pip.exe
# │   ├── activate
# │
# ├── Lib/
# │   └── site-packages/
# │       → onde ficam as bibliotecas instaladas
# │
# └── Include/


# =========================================================
# ESTRUTURA DO AMBIENTE (LINUX / MAC)
# =========================================================

# venv/
# ├── bin/
# │   ├── python
# │   ├── pip
# │   ├── activate
# │
# ├── lib/
# │   └── pythonX.X/
# │       → bibliotecas instaladas
# │
# └── include/


# =========================================================
# OBSERVAÇÃO IMPORTANTE SOBRE O PYTHON
# =========================================================

# Antes de ativar o venv:
# → você está usando o Python GLOBAL do sistema

# Depois de ativar (próxima aula):
# → você passa a usar o Python do ambiente virtual

# Ou seja:
# o ambiente virtual "troca" temporariamente o Python ativo


# =========================================================
# RESUMO
# =========================================================

# - Criar venv = criar uma pasta isolada com Python
# - Cada projeto pode ter seu próprio ambiente
# - Ainda não ativamos (isso vem na próxima aula)