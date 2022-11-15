
text = iter('Vinicius')

print(text)
print(text.__next__())
print(next(text))
print(next(text))

iterator = iter('Garcia')

while True:
    try:
        l = next(iterator)
        print(l)
    except StopIteration:
        break

for item in text:
    print(item)
