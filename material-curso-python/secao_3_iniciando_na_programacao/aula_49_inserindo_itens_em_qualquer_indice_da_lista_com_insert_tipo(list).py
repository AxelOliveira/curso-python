"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
        append - Adiciona um item ao final
        insert - Adiciona um item no índice escolhido
        pop - Remove do final ou do índice escolhido
        del - Apaga um índice
        clear - limpa a lista
        extend - estende a lista
        + - concatena a lista
Create Read Update     Delete
Criar, ler, alterar, apagar = lista[i]   (CRUD)
Quando não souber qual o ultimo indice da sua lista é só utilizar -1, pois começa de trás para frente
.insert(0, 5) adiciona o número 5 no indice 0 (primeiro sempre será o número do indice e depois o que você quer adicionar)
insert não substitui — ele empurra
"""

lista = [10, 20, 30, 40]
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear()
lista.insert(100, 5)
print(lista[4])