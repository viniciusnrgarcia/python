# raise - lançando exceptions

def calc(a, b):
    try:
        return a / b
    except Exception as e:
        # print(e)
        print('error calc method')
        raise e

def check(a, b):
    if not isinstance(a, (float, int)):
        raise TypeError(
            f'{a} deve ser int ou float'
            f'{b} deve ser int ou float'
        )

    if b == 0:
        raise ZeroDivisionError(f'Divisão não permitida devido divisor zero {b}')


try:
    print(calc(1, 0))
except Exception as e:
    print('error')
    print(type(e))
    print(e)


try:
    check(0, 0)
except Exception as e:
    ...

try:
    check('a', 'b')
except Exception as e:
    print(type(e))
    print(e)


