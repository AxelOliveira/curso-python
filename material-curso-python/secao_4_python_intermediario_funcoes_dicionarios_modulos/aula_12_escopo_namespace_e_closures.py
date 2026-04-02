################################################################################
#
# Escopo e Namespace no Python
#
# O que você vai aprender neste vídeo:
# * PARTE 1
# ** O que é escopo
# ** O que é namespace
# ** Uso de `globals()` e `locals()` para introspecção do namespace
# ** Uso de `vars()` e `dir()` para instrospecção do namespace
# ** Relação entre escopo e namespace
#
# * PARTE 2
# ** A regra LEGB e como o Python a usa para resolver nomes
# ** Modificar o comportamento do Python com `global` e `nonlocal`
# ** PARA NERDS - varnames, freevars e cellvars
#
# Nota: quando eu usar a palavra "nome" sempre estarei me referindo
# identificadores de algo como: variável, função, classe, imports, etc...
#
# Conhecimento Python requerido: variáveis, funções e estruturas de dados.
#
################################################################################

# EXEMPLO 2

"""Um módulo de exemplo"""

################################################################################
#
# O que é escopo
#
# Escopo é a região do código onde um nome está diretamente acessível.
# Ele determina os limites e o tempo de vida dos nomes definidos internamente.
#
# Escopo é usado para encapsular o código e evitar colisões de nomes e efeitos
# colaterais indesejados.
#
# O Python tem quatro tipos de escopos: Built-In, Global, Enclosing e Local.
# Esses escopos são dinâmicos. O interpretador pode criar e apagar em tempo de
# execução.
#
# Cada escopo tem seu "espaço de nomes" (namespace), que é um local onde os
# nomes e seus respectivos objetos são armazenados.
#
################################################################################

# nome definido no escopo global (módulo)
um_nome = "um_nome (GLOBAL)"


# nome definido no escopo global (módulo)
def func_global(sou_local: str) -> None:
    # Escopo local (função e seus parâmetros)

    # `um_nome` no escopo local é OUTRA VARIÁVEL (sem relação outro escopo)
    um_nome = "um_nome (LOCAL)"  # nome definido no escopo local
    outro_nome = "outro_nome (LOCAL)"  # nome definido no escopo local

    # Parâmetros de funções também são do escopo local da função
    print(f"Dentro da função: {um_nome}, {outro_nome}, {sou_local}")


# ISSO NÃO FUNCIONA
# print(outro_nome, sou_local)

# Isso é injetado automaticamente pelo Python no escopo global
print("Nome do módulo:", __name__)
print("Arquivo do módulo:", __file__)
print("Documentação do módulo:", __doc__)
print()  # apenas uma quebra de linha

func_global("arg (local)")
# Saída - Dentro da função: um_nome (LOCAL), outro_nome (LOCAL), arg (local)

print(f"Fora da função: {um_nome}")  # Acessa a variável GLOBAL
# Saída - Fora da função: um_nome (GLOBAL)


#
#
#
#
#

# EXEMPLO 3
################################################################################
#
# O que é namespace?
#
# Namespace é uma estrutura de dados real que mapeia nomes para objetos. Cada
# chave é o nome que você define e o valor é o objeto correspondente no seu
# código. Sempre que você cria um nome, essa associação é guardada dentro de um
# namespace.
#
# Vamos usar `globals()` e `locals()` no mesmo código anterior e confirmar isso.
#
# globals(): Retorna um dicionário que representa o namespace global do módulo
#            atual. Isso inclui todos os nomes definidos na raiz do arquivo.
# locals():  Retorna um dicionário com os nomes definidos no escopo local onde
#            a função está sendo executada. Importante: ela só inclui nomes que
#            já foram definidos antes da sua chamada.
#
################################################################################

namespace_global = globals()
um_nome = "um_nome (GLOBAL)"

# # print(id(um_nome), id(namespace_global["um_nome"]))
# print(dir(__builtins__))


def func_global(sou_local: str) -> None:
    um_nome = "um_nome (LOCAL)"
    outro_nome = "outro_nome (LOCAL)"
    print("LOCALS (namespace da função)")
    print(locals())
    print()


# func_global("arg (local)")
# print()

# print("GLOBALS (namespace do módulo)")
# print(globals())

#
#
#
#
#

# EXEMPLO 4
################################################################################
#
# o que é namespace?
#
# namespace é uma estrutura de dados real que mapeia nomes para objetos. cada
# chave é o nome que você define e o valor é o objeto correspondente no seu
# código. sempre que você cria um nome, essa associação é guardada dentro de um
# namespace.
#
# vamos usar `vars()` e `dir()` no mesmo código anterior e confirmar isso.
#
# `vars()`: retorna o atributo `__dict__` de um objeto, que é onde seus
#           atributos são armazenados. se chamada sem argumentos, `vars()` se
#           comporta exatamente como `locals()`, retornando o namespace local.
# `dir()`:  sem argumentos, `dir()` lista todos os nomes disponíveis no escopo
#           atual. com um objeto como argumento, tenta listar todos os nomes
#           acessíveis nele (como métodos e atributos). note que `dir()`
#           retorna apenas os nomes, não os objetos ou seus valores.
#
################################################################################

um_nome = "um_nome (global)"


def func_global(sou_local: str) -> None:
    um_nome = "um_nome (local)"
    outro_nome = "outro_nome (local)"
    print("locals (namespace da função)")
    print("dir", dir())
    print("vars", vars())
    print()


# func_global("arg (local)")
# print()

print("globals (namespace do módulo)")
print("dir", dir())
print("vars", vars())

#
#
#
#
#

# EXEMPLO 5
################################################################################
#
# Relação entre escopo e namespace
#
# Escopo e namespace são assuntos interligados e muitas vezes confundidos.
# Mas a diferença entre eles é simples:
#
# - Escopo define os limites e o tempo de vida de um trecho de código que tem
#   um namespace.
# - Namespace é um objeto real que guarda os nomes e seus respectivos valores.
#
# É por isso que, ao fazer `import x`, dizemos que `x` é um namespace, ele
# guarda nomes como `x.func_global()`, `x.valor`, etc.
#
################################################################################
# import x


def func_global() -> None:
    print(f"Estou em: {__name__} - {__file__.split('/')[-1]}")


# x.func_global()
func_global()
print()
print(globals())