"""
Aula: Ativando e desativando ambiente virtual (venv)

Resumo:
Quando você executa o comando "python", o sistema busca o executável nos caminhos
configurados no PATH.

Ao ativar um ambiente virtual:
- O PATH é alterado temporariamente
- O Python usado passa a ser o do ambiente virtual
- Instalações (pip) passam a ser locais (no projeto)

Ao desativar:
- Volta a usar o Python global do sistema

Principais comandos:

Windows:
    Ativar:
        .\venv\Scripts\activate
    Desativar:
        deactivate

Linux/Mac:
    Ativar:
        source venv/bin/activate
    Desativar:
        deactivate
"""

# 1 - Verificar versão do Python (antes de ativar o ambiente)
# (usa o Python global do sistema)
# python --version

# 2 - Ativar o ambiente virtual (Windows)
# .\venv\Scripts\activate

# 3 - Após ativar, o terminal mostra o nome do ambiente (ex: (venv))
# Isso indica que o ambiente virtual está ativo

# 4 - Verificar novamente o Python
# Agora será o Python dentro da pasta do ambiente virtual
# python --version

# 5 - Verificar o pip (instalador de pacotes)
# pip --version
# (mostra que está usando o pip do ambiente virtual)

# 6 - Instalar bibliotecas agora instala LOCALMENTE
# pip install nome_da_biblioteca

# 7 - Desativar o ambiente virtual
# deactivate

# 8 - Após desativar, o Python volta a ser o global
# python --version