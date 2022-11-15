"""
Desempacotamento
"""
l = ['Vinicius', 'Layza', 'Heitor', 'Ana', 1, 2, 3]

n1, n2, n3, *l2, last = l

print(l)
print(n1, n2, n3)
print(l2)
print(last)

# 3 últimos elementos
*l3, last1, last2, last3 = l
print(last1, last2, last3)

n11, *_ = l
print(n11)
