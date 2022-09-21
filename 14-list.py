"""
Listas em Python
"""
c = [1, 2, 3, 4, 5]

for item in c:
    print(item)
else:
    print('----')

p = 'Vinicius'
m = 'Layza'
f = 'Heitor'

array = [p, m, f]

for i in array:
    array[1] = 'Layza Fernanda'
    print(i)
    if i == 'Heitor':
        array.append('Ana')
        array.append('Layza')
        array.append('Vinicius')
