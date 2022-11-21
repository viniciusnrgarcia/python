""""
Funções (def) em Python
"""


def f(v):
    return v


var = f('Print')

print(var)

"""
Exemplo 2
"""


def div(n1, n2):
    if n2 == 0:
        return
    return n1 / n2


d = div(2, 1)

if d:
    print(d)
else:
    print('Valor inválido')

"""
"""


def h1():
    return 'function 1'


def h2(f):
    print('function 2')
    return f()


print(h1())
print(h2(h1))


def f1(fn, *args, **kwargs):
    print(f'Executando function 1 {f}, {args}, {kwargs}')
    return fn(*args, **kwargs)


def f2(n):
    print(f'Executando function 2 {n}')
    return f'Value (f2): {n}'


def f3(n, s):
    print(f'Executando function 3 {n} {s}')
    return f'Value (f3): {n} {s}'


exec1 = f1(f2, 'Vinicius')
print(exec1)

exec2 = f1(f3, 'Vinicius', s='Garcia')
print(exec2)


"""
Escopo de funções em Python
* Escopo global é todo código alcançavel.
* Escopo local é apenas no mesmo local.
"""

# global scope
x = 1

def f1():
    # inner scope
    x = 10
    print(x)

def f2():
    global x # não recomando
    x = x + 2
    print(f'global X: {x}')

print(x) 
f1()
print(x) 

f2()
print(x)
