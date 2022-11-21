"""
Sets - Conjuntos em Python (tipo set)
Mutáveis, porém aceitam apenas tipos imutáveis como valor interno
- não tem indexes
- não garantem ordem;
são iteráveis (for, in, not, in)
"""

s1 = set()

s1.add(1)
s1.add(1)
s1.add(2)

print(s1)

s1.remove(2)

print(s1)

s1.add(2)
s1.add(3)
s1.add(2)


s2 = set()
s2.add(5)

print(s1)

s1 = s1.union(s2)

print(s1)


l1 = [1, 2, 3, 4, 4]

print(l1)
print(set(l1))


s4 = {1, 2, 2, 3}
s5 = {2, 4, 5, 6}
s6 = s4 | s5 # união
print(s6)

s6 = s4 & s5 # intersecção - item presentes em ambos os sets
print(s6)

s6 = s4 - s5  # diferença - o que não contém 
print(s6)

s6 = s4 ^ s5  # diferença simétrica - o que não contém em ambas os sets
print(s6)

