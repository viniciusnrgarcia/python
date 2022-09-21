"""
Formatando valores com modificadores

:s - Texto (str)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:. (NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro

"""

num1 = 19
num2 = 3
div = num1 / num2
print('{:.2f}'.format(div))
print(f'{div:.4f}')

nome = 'Vinicius Garcia'
print(f'{nome:s}')

v = '2000'
print(f'{v:0>10}')

print(f'{v:0<10}')
print(f'{v:1<10}')

nome_formatado = '{:@>50} '.format(nome)
print(nome_formatado)

print(nome.rjust(30, '#'))
print(nome.lower())
print(nome.upper())
print(nome.capitalize())
print(nome.casefold())
print(nome.swapcase())

