"""
while
utilizado para realizar ações enquanto uma condição for verdade, assim como Java.
"""
import time

t = time.time()

e = 1000000
i = 0

while i <= e:
    # print('C: {}'.format(i))
    i = i + 1

print('total time (s) {} '.format(time.time() - t))

x = 0
while x < 10:
    x = x + 1
    if x == 3 or x == 5 or x == 7:
        continue
    print(x)

x = 0
while x < 10:
    x = x + 1
    if x == 3 or x == 5 or x == 7:
        break
    print(x)

y = 0

while y < 100:
    y += 1
    if y > 99:
        print(y)
else:
    print('Fim processamento while')

while True:
    break
else:
    print('Fim processamento')

