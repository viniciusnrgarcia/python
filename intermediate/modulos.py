import sys

import modulos_m as m

# importação de modulos
import modulo_test.modulo
from modulo_test.modulo import calc
from modulo_test import modulo


print('Modulo: ', __name__)
print(m.f1())
# print(*sys.path, sep='\n')
print(m.item)

print(calc(2, 3))
print(modulo_test.modulo.calc(2, 5))
print(modulo.calc(2, 1))
