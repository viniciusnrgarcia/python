import time

t = 'Python'

for i in t:
    print(i)


items = ['A', 'B', 'C']

for i in items:
    print(i)

e = time.perf_counter()
e2 = time.perf_counter_ns()
e3 = time.process_time()
e4 = time.process_time_ns()

for n in range(10000000):
    if n >= 10000000 - 1:
        print(n)

f = time.perf_counter()
f2 = time.perf_counter_ns()
f3 = time.process_time()
f4 = time.process_time_ns()

print('Elapsed time: ', e, f)
print('Elapsed time during the whole program in seconds: ', f - e)

print('Elapsed time during the whole program in nanoseconds: ', f2 - e2)

print('Elapsed time during the whole program in seconds: ', f3 - e3)

print('Elapsed time during the whole program in nanoseconds: ', f4 - e4)

# print('Elapsed time (ns): ', e2, time.perf_counter_ns())
# print('Elapsed time during the whole program in seconds (ns): ', time.perf_counter_ns() - e2)

for n in range(0, 10, 2):
    print(n)
