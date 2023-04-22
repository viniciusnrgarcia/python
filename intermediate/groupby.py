from itertools import groupby


l1 = [
    {'n':'Layza', 'idade':31},
    {'n':'Vinicius', 'idade':34},
    {'n':'Heitor', 'idade':3},
    {'n':'Layza', 'idade':31},
    {'n':'Layza', 'idade':31},
    {'n':'Renato', 'idade':34}
]

#print(l1)

l2 = sorted(l1, key=lambda a: a['idade'], reverse=True)

#print(l2)

def order(item):
    return item['idade']

g = groupby(l2, key=order)

for k, v in g:
    print(k, list(v))


