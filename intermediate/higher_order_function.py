"""
Funções de primeira classe

Academicamente, os termos Higher Order Functions e First-Class Functions têm significados diferentes.

Higher Order Functions - Funções que podem receber e/ou retornar outras funções

First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

Não faria muita diferença no seu código, mas penso que deveria lhe informar isso.

Observação: esses termos podem ser diferentes e ainda refletir o mesmo significado.
"""


def f1(msg, name):
    return f'{msg}, {name}!'


def exec(f2, *args):
    return f2(*args)

v = exec(f1, 'Hello', 'Vinicius')
print(v)

