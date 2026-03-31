# Problema dos parâmetros mutáveis em funções Python
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('Jeon')
adiciona_clientes('Wonwoo', cliente1)
adiciona_clientes('Vernon', cliente1)
cliente1.append('Mingyu')

cliente2 = adiciona_clientes('The8')
adiciona_clientes('Seungkwan', cliente2)

cliente3 = adiciona_clientes('Dino')
adiciona_clientes('Chan', cliente3) 

print(cliente1)
print(cliente2)
print(cliente3)