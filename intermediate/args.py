"""
Argumentos nomeados e não nomeados em funções python
"""
def sum(x, y, z):
    print(f'{x=} y={y} z={z}', '|', 'x + y + z = ', x + y + z)

sum(1, 2, 2)
sum(y=2, x=1, z=2)
sum(1, 2, z=2)



"""
valores padrão para parâmetros.
Caso não informado, o valor padrão será utilizado
"""

def calc(y, x, z=None):
    result = None
    if z is not None: # or is None do...
        print(type(z), z)
        result = x + y + z
    else:
        result = x + y
    return result

v = 2
v2 = calc(v, 1)
v3 = calc(v, 1, 5)

print(v)
print(v2)
print(v3)


