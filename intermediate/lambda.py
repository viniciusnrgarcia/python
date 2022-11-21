"""
Função lambda em Python
A função lambda é uma função como qualquer outra em Python.
São funções anônimas que contém apenas uma linha, ou seja, tudo deve ser 
contido dentro de uma única expressão.
"""

l1 = [4, 5, 2, 1, 5, 8, 0, 2]
l1.sort(reverse=True)

l2 = [
    {'n': 'V', 's': 'G'},
    {'n': 'L', 's': 'O'},
    {'n': 'H', 's': 'G'}
]


def order(item):
    return item['n']  # ordena pelo item 'n'


l2.sort(reverse=False, key=order)
print(l2)

for item in l2:
    print(item['n'])


"""
lambda expression
"""
l2.sort(reverse=True, key=lambda item: item['n'])

l4 = sorted(l2, key=lambda item: item['n'], reverse=True)

for item in l4:
    print(item['n'])


"""
"""


def exec(f1, *args):
    return f1(*args)


def sum_value(x, y):
    return x + y


print(
    exec(
        lambda x, y: x + y,  # function lambda sendo enviada como parâmetro
        2, 3
    ),
    exec(sum_value, 1, 2)  # function normal sendo invocada
)


def create_mult(multi):
    def multi(num):
        return num * multi
    return multi


# mesma function acima em lambda
duplicate = exec(
    lambda m: lambda n: m*n,
    2
)

print(duplicate(2))


print(
    exec(
        lambda *args: sum(args), 
        1, 2, 3, 5
    )
)