# raise / throw
class CustomerNotExists(Exception):
    ...


def create_exception():
    raise CustomerNotExists('Cliente não encontrado')


#raise CustomerNotExists('Cliente não encontrato')

try:
    create_exception()

except CustomerNotExists as error:
    print('Error gerado no try except')
    print(error.__cause__)
    print(error.__class__)
    print(error.__class__.__name__)
    raise error





