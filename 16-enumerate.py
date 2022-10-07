"""
 Enumerate - enumerar elementos
"""
from array import array

l = ['Heitor', 'Layza', 'Vinicius', ['Rosa', 'Renato'], ['Geralda', 'Carlos']]
l2 = array('i', [0, 1, 2])

for i in l:
    print(i)

itens = ''
for i in list(range(1, 101)):
    itens += '"' + f'{str(i)}' + '"' + ","

print(itens)


