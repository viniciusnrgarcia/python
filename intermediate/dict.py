import copy

produto = {
    'id': 12341,
    'descricao' : 'p1',
    'quantidade' : 34,
    'preco' : 200244212.00,
    'disponibilidade' : [
        {
            'filial' : 1
        },
        {
            'filial': 2
        }
    ]

}

print(produto['id'])
print(produto['quantidade'])

for k, v in enumerate(produto):
    print(f'{v} : {produto[v]}')
    if isinstance(produto[v], list):
        for k, v in enumerate(produto[v]):
            print(v)
            print(f'ID filial: {v["filial"]} ')


produto2 = {}

produto2['id'] = 1235224

print(produto2)



"""
# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com as chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - apaga um item com a chave especificada (del)
# popitem - apaga o último item adicionado
# update - atualiza um dicionário com outro
"""

print(len(produto))
print(list(produto.keys()))
print(list(produto.values()))
print(list(produto.items()))


d1 = {
    'c1': 1,
    'l1': [1, 2, 3]
}

d2 = d1.copy() # shallow copy 

d2['c1'] = 2

print(d2)
print(d1)

d3 = copy.deepcopy(d1)

d1['l1'][1] = 9999

print(d3)
print(d1)
print(d2)



print(d1.get('c3'))

d1['c3'] = 'Test'
d1['c4'] = 'Test'
print(d1)
n = d1.pop('c3')

print(d1)


d1['c4'] = 'Test'

print(d1)

d1.popitem()

print(d1)


d1.update({
    'c1': '21312421321',
    'item': 232123
})

print(d1)


d1.update(c1='999999', item=99999)

print(d1)


"""
Empacotamento e desempacotamento de dicionários
"""
a, b = 1, 2
a, b = b, a
print(a, b)

p1 = {
    'n': 'V',
    's': 'G'
}

a, b = p1
print(a, b)

a, b = p1.values()
print(a, b)

a, b = p1.items()
print(a, b)

(a1, a2), b = p1.items()
print(a1, a2, b)

for k, v in p1.items():
    print(k, v)


p2 = {
    'i': 34,
    'a': 1.88
}

# Join dicionários
p3 = {**p1, **p2}

print(p3)


# args e kwargs
def mv(*args, **kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

mv(n='Vinicius', qlq=34)

# desempacotamento de argumentos
mv(**p3)

