import pprint

def p(m):
    pprint.pprint(m)


"""
Dictionary Comprehension e Set Comprehension
"""
product = {
    'name': 'A',
    'price': 1.54,
    'category': 'office'
}

for k, v in product.items():
    print(k, v)

dc = {
    k: v
    if isinstance(v, (int, float)) else v.upper()
    for k, v in product.items()
    if k != 'category' # filter
}

p(dc)


s1 = {i for i in range(10)}
p(s1)
p(set(range(10)))

