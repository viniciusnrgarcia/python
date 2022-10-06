"""
Split, Join, Enumerate
* Split - dividir uma string
* Join - Juntar
* Enumerate - enumerar elementos
"""

string = "156451 154541 2 2121321. 23232"
l1 = string.split(' ')
l2 = string.split('.')

p = ''
count = 0
for v in l1:
    print(v)
    count = l1.count(v)

print(count)

for index, value in enumerate(l1):
    print(f'Indice da lista : {index}, seu valor é {value}')

for i, v in enumerate(range(5)):
    print(f'Indice da lista : {i}, seu valor é {v}')


l3 = [
    [0, 'Heitor'],
    [1, 'Layza'],
    [2, 'Vinicius']
]

for i, v in l3:
    print(f'Indice da lista : {i}, seu valor é {v}')

l4 = ['A', 'B', 'C', 'D']

n1, n2, n3, n4 = l4

print(n2)