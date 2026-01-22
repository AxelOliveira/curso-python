"""
Dicionários em Python (tipo dict)

Dicionários são estruturas de dados do tipo par de "chave" e "valor".

- A chave funciona de forma parecida com o índice das listas, mas em vez de usar número (0, 1, 2...), usamos identificadores.
- As chaves devem ser de tipos IMUTÁVEIS.
- Os valores podem ser de QUALQUER tipo, inclusive outro dicionário ou lista.

Tipos imutáveis comuns:
- str, int, float, bool, tuple

Tipo mutáveis:
- list, dict

Usamos:
- Chaves {}
- ou a classe dict()
para criar dicionários
"""

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'enderecos': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'outra rua', 'numero': 321},
    ],
}

# Acessando valores através da chave
print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

# Percorrendo o dicionário
# O for percorre as CHAVES do dicionário
for chave in pessoa:
    print(chave, pessoa[chave])