"""
Condições
IF, ELIF e ELSE
"""

if True:
    print('Verdadeiro')

if True:
    print('NOK')

num1 = 2
num2 = 4

if num1 > 0:
    print(num1 + num2)
else:
    print('Falso')


if num1 > 3:
    print(num1)
elif num1 > 4:
    print(num1)
elif num1 >= 2:
    print('elif num1 >= 2. ', 'Valor atributo "num1" : {} '.format(num1))
else:
    print('nok')

