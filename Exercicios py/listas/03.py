"""Crie um dicionário representando um carrinho de compras.
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra"""

carrinho = {}
soma = 0 

carrinho['Arroz'] = 1
carrinho['Feijão'] = 2
carrinho['Óleo'] = 4
carrinho['Sal'] = 1
carrinho['Café'] = 3


for i in carrinho:
    soma += carrinho[i]

print(f'Total de {soma} produtos')