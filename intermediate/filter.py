from functools import partial, reduce


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


l1 = [
    {'n': 'Layza', 'idade': 31},
    {'n': 'Vinicius', 'idade': 34},
    {'n': 'Heitor', 'idade': 3},
    {'n': 'Layza', 'idade': 31},
    {'n': 'Layza', 'idade': 31}
]

print_iter(l1)


l2 = [
    p for p in l1
    if p['idade'] < 18
]

print_iter(l2)

# filter - funcao funcional
l3 = filter(
    lambda p: p['idade'] < 18,
    l1
)

print_iter(l3)

# ou
def filter_item(p):
    return p['idade'] < 18

l3 = filter(
    filter_item,
    l1
)

print_iter(l3)
