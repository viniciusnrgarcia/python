# isinstance

l1 = [
    'a', 1, 1.23, True, [0, 1, 4, 4], (1, 2), {1, 2}, {'name': 'Vinicius'},
]

print(l1)

for item in l1:
    if isinstance(item, set):
        print('SET')
        print(item, isinstance(item, set))
#    print(item, isinstance(item, set))

    elif isinstance(item, str):
        print('STR')
        print(item)

    elif isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 2)

    else:
        print('OUTRO')
        print(item)
