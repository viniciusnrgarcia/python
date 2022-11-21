"""
Closure e funções que retornam outras funções
"""


def f1(message):
    def f2(name):
        return f'{message}, {name}'
    return f2 # apontamento para memória, se retornar f2(), chamando a function, a mesma é executada. Se não invocar a function com '()', a mesma fica em memória, permitindo uso do closure


s1 = f1('Bom dia')
s2 = f1('Bom dia')
s3 = f1('Bom dia')

print(s1('L'))
print(s2('V')) # invocação da função, finalizando execução.
print(s3('H'))
