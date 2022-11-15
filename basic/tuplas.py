"""
Tuplas
"""

t1 = (1, 2, 'Vinicius', 3, 'Garcia')

print(type(t1))
print(t1)
print(t1[2])


l = [()]
print(type(l))
print(type(l[0]))


t2 = (1, 2, 3)
t2 = list(t2)
t2[1] = 3000
t2 = tuple(t2)

print(t2)

