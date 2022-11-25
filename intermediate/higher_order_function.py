"""
Funções de primeira classe
Os termos Higher Order Functions e First-Class Functions têm significados diferentes.
Higher Order Functions - Funções que podem receber e/ou retornar outras funções
First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)
"""


def f1(msg, name):
    return f'{msg}, {name}!'


def exec(f2, *args):
    return f2(*args)

v = exec(f1, 'Hello', 'Vinicius')
print(v)

