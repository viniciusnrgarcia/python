"""
 Enumerate - enumerar elementos
 object iterable*
"""
from array import array

l = ['Heitor', 'Layza', 'Vinicius', ['Rosa', 'Renato'], ['Geralda', 'Carlos']]
l2 = array('i', [0, 1, 2])

for i in l:
    print(i)

items = ''
for i in list(range(1, 101)):
    items += '"' + f'{str(i)}' + '"' + ","

print(items)


l3 = [
    # 0            # 1
    ['Vinicius','Layza'],   # 0
    ['Heitor', 'Layza'],     # 1
    ['Layza', 'Heitor'],     # 2
    ['Ana']
]

e = enumerate(l3)
le = list(e)
print(l3)
print(e)
print(le)

for k, v in e:
    print(k, v)

for k, v in le:
    print(k, v)

# desempacotamento
for i in le:
    v1, v2 = i
    print(v1, v2)

