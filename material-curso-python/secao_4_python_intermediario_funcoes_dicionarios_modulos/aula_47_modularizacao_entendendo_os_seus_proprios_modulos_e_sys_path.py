"""
Modularização - Entendendo seus próprios módulos e o sys.path

CONCEITOS PRINCIPAIS:

1) Todo programa Python começa a execução por um arquivo principal, que recebe automaticamente o nome especial "__main__".

2) O python SEMPRE conhece:
    - A pasta onde o arquivo __main__ está
    - As pastas abaixo dela (subpastas)

3) O Python NÃO conhece, por padrão:
    - Pastas acima do arquivo __main__

4) Quando usamos "import nome_do_modulo":
    - O Python procura esse módulo dentro dos caminhos listados em sys.path
    - O diretório do __main__ é automaticamente incluído no sys.path

5) O atributo especial __name__ indica:
    - "__main__" -> quando o arquivo é executado diretamente
    - "nome_do_modulo" -> quando o arquivo é importado
"""
# 1) Importamos um módulo que está no mesmo diretório do arquivo principal
import aula_47_modulo

# 2) Como este arquivo foi executado diretamente, o Python define seu __name__ como "__main__"
print('Este módulo se chama', __name__)