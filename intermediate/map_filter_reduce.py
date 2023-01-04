from functools import partial, reduce


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


l1 = [
    {'n': 'Layza', 'idade': 31},
    {'n': 'Viniicus', 'idade': 34},
    {'n': 'Heitor', 'idade': 3},
    {'n': 'Layza', 'idade': 31},
    {'n': 'Layza', 'idade': 31}
]

print_iter(l1)


def add(item):
    return item + 1


l2 = [
    {**p, 'idade': add(p['idade'])} for p in l1
]

print_iter(l2)


def add_sum(item):
    return {
        **item,
        'idade': item['idade'] + 1  # realiza alguma operação e retorna item
    }


l3 = map(
    add_sum,
    l1
)

print_iter(l3)


print_iter(
    list(map(
        lambda x: x * 2,
        [1, 2, 3, 4, 5]
    ))
)


l4 = [
    p for p in l1
    if p['idade'] < 18
]
print_iter(l4)

# filter
l5 = filter(
    lambda p: p['idade'] < 18,  # or function to filter
    l1
)
print_iter(l5)


def f_reduce(total, p):
    print(total)
    return p['idade'] + total


# reduce
l6 = reduce(
    # lambda x, y: x+y, [1, 2, 3, 4, 5]
    f_reduce,
    l1,
    0
)
print(l6)
