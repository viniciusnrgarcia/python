from itertools import groupby


l1 = [
    {'n':'Layza', 'idade':31},
    {'n':'Viniicus', 'idade':34},
    {'n':'Heitor', 'idade':3},
    {'n':'Layza', 'idade':31},
    {'n':'Layza', 'idade':31}
]

# print(l1)

l2 = sorted(l1, key=lambda a: a['idade'], reverse=True)

g = groupby(l2)

for k, v in g:
    print(k, list(v))


