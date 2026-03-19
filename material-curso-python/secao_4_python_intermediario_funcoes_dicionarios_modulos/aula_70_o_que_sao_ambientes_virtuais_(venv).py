"""
Ambientes Virtuais

Ambientes virtuais em Python são usados para isolar projetos.

PROBLEMA QUE ELES RESOLVEM:
Quando você trabalha com vários projetos, cada um pode precisar:
- versões diferentes de bibliotecas
- versões diferentes do Python
- dependências específicas

Sem ambiente virtual:
- tudo fica instalado no sistema global
- gera conflitos de versão
- difícil manutenção

COM AMBIENTE VIRTUAL:
- cada projeto tem sua própria "cópia" do Python
- cada projeto tem suas próprias bibliotecas
- tudo fica isolado em uma pasta

COMO FUNCIONA:
- é literalmente uma pasta
- dentro dela fica:
    - executável do Python
    - bibliotecas instaladas
- ao ativar o ambiente, você usa esse Python (não o global)

VANTAGENS:
- evita conflitos entre projetos
- facilita manutenção
- deixa o projeto mais profissional
- permite recriar o ambiente com requirements.txt

NOMES COMUNS:
- venv
- env
- .venv
- .env

IMPORTANTE:
- NÃO subir a pasta venv para o GitHub
- usar .gitignore
"""

# =========================================================
# EXEMPLOS (COMENTADOS - EXECUÇÃO VIA TERMINAL)
# =========================================================

# 1) CRIAR UM AMBIENTE VIRTUAL
# python -m venv venv

# 2) ATIVAR (Windows)
# venv\Scripts\activate

# 3) ATIVAR (Linux/Mac)
# source venv/bin/activate

# 4) INSTALAR PACOTES (vai instalar dentro do venv)
# pip install requests

# 5) GERAR ARQUIVO DE DEPENDÊNCIAS
# pip freeze > requirements.txt

# 6) RECRIAR AMBIENTE EM OUTRO PC
# pip install -r requirements.txt

# 7) DESATIVAR O AMBIENTE
# deactivate


# =========================================================
# EXPLICAÇÃO EM FORMATO DE PENSAMENTO COMPUTACIONAL
# =========================================================

# 1. Criamos uma pasta chamada "venv"
# 2. Dentro dela, o Python copia:
#    - executável
#    - bibliotecas
# 3. Ao ativar:
#    - o terminal passa a usar esse Python
# 4. Qualquer instalação via pip:
#    - vai apenas para esse ambiente
# 5. Ao finalizar:
#    - podemos deletar o ambiente sem afetar o sistema
# 6. Para recriar:
#    - usamos o requirements.txt


# =========================================================
# OBSERVAÇÃO IMPORTANTE
# =========================================================

# A pasta do ambiente virtual:
# NÃO deve ir para o GitHub

# Exemplo de .gitignore:
# venv/
# .venv/
# env/