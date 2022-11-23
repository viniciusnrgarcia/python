import sys


# Generator expression, Iterables i Iterators em Python
iterable = ['1', '2', 3]
iterator = iter(iterable) # iterable.__iter__() # item

print(iterator)
print(next(iterator))
print(next(iterator))
print(next(iterator))


list = [n for n in range(100000)]
generator = (n for n in range(6))

print(sys.getsizeof(list))
print(sys.getsizeof(generator))

# for i in generator:
#     print(i)


# Generator functions em Python


def generator(n=0):
    yield 1 # pause
    print('end')
    yield 2 # pause


gen = generator(n=0)

print(next(gen))
print(next(gen)) # continue


# pausa a cada execução, indicado por 'yield'
def gen(n=0, maximum=5):
    while True:
        yield n
        n += 1

        if n > maximum:
            return

g = gen(maximum=10000)
for n in g:
    print(n)

