class Order:
    id: int
    description: str

    def __init__(self, id, description):
        self.id = id
        self.description = description

    def hash_code():
        return 123


o1 = Order(2, 'Order 2')
print(o1, o1.id)


class Product:
    id: int
    description: str

    def __init__(self) -> None:
        pass

    def to_string(self):
        print(f'Product id: {self.id} descripton: {self.description} ')


p1 = Product()
p1.id = 1
p1.description = 'Produto 1'

print(p1.id, p1.description)
print(p1.to_string())




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


c1 = Customer()
Customer.factory_method()
Customer.factory_method()

c2 = Customer.new_instance(2, 'Vinicius')
print(c2.id, c2.name)

c3 = Customer.new_instance(3, 'Layza')
print(c3.id, c3.name)
