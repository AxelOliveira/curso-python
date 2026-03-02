# 1 - Importamos o módulo copy para usar deep copy
import copy

# 2 - Importamos a lista de produtos do package
from dados import produtos

# ============================================================
# EXERCÍCIO 1
# Aumentar os preços dos produtos em 10%
# Gerar nova lista usando deep copy
# ============================================================

# 3 - Criamos nova lista aplicando transformação no preço
novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]

# ============================================================
# EXERCÍCIO 2
# Ordenar produtos por nome (decrescente)
# ============================================================

# 4 - Geramos nova lista ordenada pelo nome do maior para o menor
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)

# ============================================================
# EXERCÍCIO 3
# Ordenar produtos por preço (crescente)
# ============================================================

# 5 - Germaos nova lista ordenada pelo menor preço
produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco']
)

# ============================================================
# RESULTADO FINAL
# ============================================================

# 6 - Exibimos lista original
print(*produtos, sep='\n')
print()

# 7 - Exibimos produtos com preço aumentado
print(*novos_produtos, sep='\n')
print()

# 8 - Exibimos produtos ordenados por nome
print(*produtos_ordenados_por_nome, sep='\n')
print()

# 9 - Exibimos produtos ordenados por preço
print(*produtos_ordenados_por_preco, sep='\n')