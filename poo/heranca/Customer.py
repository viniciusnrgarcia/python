"""
Herança
"""


class Customer:
    id: int
    name: str

    def __init__(self) -> None:
        pass

    @classmethod
    def factory_method(cls):
        print('factory_method')

    @staticmethod
    def new_instance(id, name):
        c = Customer()
        c.id = id
        c.name = name
        return c

    def to_string(self):
        print(f'Customer id: {self.id}, name: {self.name}')



class CorporateCustomer(Customer):

    corporate_id: str



c1 = Customer()
c1.id = 123
c1.name = 'Vinicius'
c1.corporate_id = 124

print(c1.id, c1.name, c1.corporate_id)



c2 = CorporateCustomer()
c2.id = 123
c2.corporate_id = 4552

print(c2.id, c2.corporate_id)

