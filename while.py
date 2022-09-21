"""
while
utilizado para realizar ações enquanto uma condição for verdade, assim como Java.
"""
import time

t = time.time()

e = 1000000000
i = 0

while i <= e:
    # print('C: {}'.format(i))
    i = i + 1

print('total time (s) {} '.format(time.time() - t))

