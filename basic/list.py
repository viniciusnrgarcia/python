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

print(array)
print(array[::-1])

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2

print(l1)
print(l2)
print(l3)
l1.append(4)
print(l1)

print(len(l3))

l3.reverse()

print(l3)

l3.reverse()

for i in l3:
    if i > 4:
        l3.remove(6)
    print(i, l3)

print(max(l3), min(l3))

l4 = list(range(1, 100))
print(l4)

for i in l4:
    print(i)

l5 = list(range(1, 10))

print(l5)
l6 = l5.pop() # remove o último elemento da lista
print(l5)
print(l6)

secret = 'python'
secret_temp = 'pn'

for l in secret:
    print(l)
    if l in secret_temp:
        print(l, secret_temp)


l4.clear() # limpa a lista


### Join lists

list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_c = list_a + list_b
print(list_c)

print(list_a)
list_d = list_a.extend(list_b) # Realiza junção da lista A, adicionando conteúdo (extendendo) da segunda coleção.
print(list_d)
print(list_a)
print(list_b)

list_e = [1, 2, '3']
list_f = list_e.copy() # copiando listas

print(list_f)
