"""
# 📘 Aula 9 - Exercício: Persistência de objetos em JSON

## 🎯 Objetivo

Praticar a conversão de objetos em dados serializáveis (JSON) e a reconstrução desses objetos a partir desses dados.

## 📌 Descrição do exercício

Você deverá:

1. Criar uma classe (por exemplo: `Pessoa`, mas pode escolher outra).
2. Criar uma ou mais instâncias dessa classe com dados.
3. Converter os dados dessas instâncias para um formato compatível com JSON.
4. Salvar esses dados em um arquivo `.json`.
5. Ler o arquivo `.json` posteriormente.
6. Utilizar os dados lidos para recriar as instâncias da classe.


## ⚙️ Regras

* Separe a solução em **dois arquivos**:

### 📂 Arquivo A (salvar dados)

* Criar a(s) instância(s)
* Converter os dados para uma estrutura (ex: dicionário)
* Salvar em um arquivo JSON

### 📂 Arquivo B (carregar dados)

* Ler o arquivo JSON
* Recuperar os dados
* Recriar as instâncias da classe com esses dados
"""
import json

class Pessoa:
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def correr(self):
        return f'{self.nome} está correndo...'


dados = {'nome': 'Wonwoo', 'idade': 27}
pessoa1 = Pessoa('Wonwoo', 27)
pessoa2 = Pessoa('Jaemin', 28)
pessoa3 = Pessoa('Bang-Chan', 29)

pessoas = [vars(pessoa1), vars(pessoa2), vars(pessoa3)]

with open('aula_9_b_exercicio_salve_sua_classe_em_json.json', 'w', encoding='utf-8') as arquivo:
    json.dump(
        pessoas,
        arquivo,
        ensure_ascii=False,
        indent=2
    )

with open('aula_9_b_exercicio_salve_sua_classe_em_json.json', 'r', encoding='utf-8') as arquivo:
    pessoas_carregadas = json.load(arquivo)

pessoas_objetos = [Pessoa(**dados) for dados in pessoas_carregadas]

for pessoa in pessoas_objetos:
    print(vars(pessoa))
    print(pessoa.correr())