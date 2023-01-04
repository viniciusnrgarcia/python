from itertools import zip_longest


def join(l1, l2):
    interval = min(len(l1), len(l2))
    print(interval)
    return [
        (l1[i], l2[i]) for i in range(interval)
    ]

l1 = ['Salvador', 'Belo Horizonte', 'Fartura', 'Barueri']
l2 = ['BA', 'MG', 'SP']
l3 = ['Pequena', 'Média', 'Grande']

print(join(l1, l2))

print(list(zip(l1, l2)))

print(list(zip_longest(l1, l2, l3)))



lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(list(zip_longest(lista_a, lista_b, fillvalue=0))) # replace None
print(lista_soma)  # [22, 4, 6, 10, 55, 60, 70]
