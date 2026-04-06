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

#
#
#
#
#

################################################################################
#
# A regra LEGB e como o Python a usa para resolver nomes
#
# O Python segue uma ordem específica e unidirecional para busca por nomes.
# A ordem sempre vai do escopo mais interno para o mais externo:
#
# Certo ✅: Local -> Enclosing -> Global -> Built-In -> ❌ NameError
# Errado ❌: Built-In -> ❌Global -> ❌Enclosing -> ❌Local
#
# De nenhum escopo externo é possível usar algo de escopo interno.
#
################################################################################
import inspect

nome_global = "nome_global"


def func_global() -> None:
    nome_enclosing = "nome_enclosing"  # Enclosing (Local)

    def func_interna() -> None:
        print("IMPRIMINDO", nome_enclosing)

        # nome_enclosing = "CRIAR UMA NOVA VARIÁVEL NESSE ESCOPO"

        def func_mais_interna() -> None:
            nome_local = "nome_local"  # Local

            get_legb("nome_enclosing", inspect.currentframe())
            print(
                "LOCAL:",
                nome_local,
                nome_enclosing,
                "funcao_interna",
                nome_global,
                "+builtins",
            )

        func_mais_interna()

    func_interna()
    # print(
    #     "ENCLOSING:",
    #     nome_enclosing,
    #     "funcao_interna",
    #     "funcao_global",
    #     nome_global,
    #     "+builtins",
    # )


func_global()
# print("GLOBAL:", nome_global, "func_global", "+builtins")

#
#
#
#
#

################################################################################
#
# Uso de `global` e `nonlocal` para mudar o comportamento
#
# Quando você define um nome em determinado escopo, o Python assume que aquele
# nome é único naquele escopo. Por isso, é impossível modificar o valor de um
# nome do escopo externo sem informar isso ao interpretador.
#
# ** `global` - Para modificar nomes do escopo global dentro de qualquer escopo
#               local, precisamos usar a palavra chave `global`.
# ** `nonlocal` -  Para modificar os nomes do escopo `enclosing` dentro de qualquer
#               escopo local, precisamos usar a palavra chave `nonlocal`.
#
################################################################################


nome_global = "nome_global"


def func_global() -> None:
    global nome_global

    nome_enclosing = "nome_enclosing"
    nome_global = 123456

    def func_interna() -> None:
        def func3() -> None:
            def func4() -> None:
                nonlocal nome_enclosing

                nome_local = "nome_local"
                nome_enclosing = 654321

                print("func_interna", nome_enclosing)

            func4()

        func3()

    func_interna()
    print("func_global", nome_enclosing)


func_global()
# print("NO GLOBAL", nome_global)

#
#
#
#
#

################################################################################
#
# PARA NERDS: varnames, freevars, cellvars
#
# Em alguns momentos você pode ver um comportamento estranho ao solicitar o
# namespace local de uma função. Ao LER uma variável do enclosing, ela pode
# aparecer como parte do namespace local (da a impressão que ela foi definida
# internamente na função). O que é isso?
#
# Detalhe: isso pode mudar dependendo do interpretador que você usar.
#
# ** Freevars são as variáveis da função externa que estão sendo usadas dentro
#    da função interna. A gente detecta isso pela função interna, porque ela é
#    quem depende desses nomes. Eles entram em co_freevars.
# ** Cellvars são as variáveis declaradas na função atual (externa) que
#    precisam ser capturadas porque são usadas por funções internas. A gente
#    detecta isso pela função externa, porque ela é quem fornece essas
#    variáveis pro closure. Eles aparecem em co_cellvars.
# ** Varnames são as variáveis locais de verdade, exclusivas da função. Elas
#    estão em co_varnames e não fazem parte de nenhum closure, só existem ali
#    dentro mesmo.
#
#
################################################################################


nome_global = "nome_global"


def func_global() -> None:
    nome_enclosing = nome_global

    def func_interna() -> None:
        nome_local = nome_enclosing

        print("dir/locals func_interna: ", f"[color(45)]{', '.join(dir())}")
        get_all_names(func_interna.__code__)

    func_interna()
    print("dir/locals de func_global: ", f"[color(45)]{', '.join(dir())}")
    get_all_names(func_global.__code__)


func_global()