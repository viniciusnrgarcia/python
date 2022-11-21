import pprint


def p(v):
    pprint.pprint(v)


"""
List comprehension em Python
É uma forma rápida para criar listas a partir de iteráveis.
"""
# print(list(range(10)))
list = []
for num in range(10):
    list.append(num)
print(list)


list = [
    num * 2
     for num in range(10)
     ]

print(list)

# mapeamento de dados em list comprehension
products = [
    {'name': 'p1', 'price': 20, },
    {'name': 'p2', 'price': 40, },
    {'name': 'p3', 'price': 30, },
]
print(products)

new_products = [
    # product
    # {'name': product['name'], 'price': product['price']} 
    # {**product, 'price': product['price'] * 1.05} # novo dicionário, atualizando dados do dict
    {**product, 'price': product['price'] * 1.05}
    if product['price'] > 30 else {**product}
    for product in products
]

print(new_products)


l1 = [n for n in range(10) if n < 5]
p(l1)



new_products = [
    # product
    # {'name': product['name'], 'price': product['price']} 
    # {**product, 'price': product['price'] * 1.05} # novo dicionário, atualizando dados do dict
    {**product, 'price': product['price'] * 1.05}
    if product['price'] > 30 else {**product}
    for product in products
    if product['price'] > 30
]

print(new_products)