# PEP 557 adicionado versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html


from dataclasses import dataclass, asdict, astuple


@dataclass(init=True)
# @dataclass(init=False)
class Customer:
    id: str
    name: str
    address: str
    locale: str = 'BR'

    # getter
    @property
    def complete_data(self):
        return f'{self.id}, {self.name}, {self.address}'

    # def __post_init__(self):
    #    print('post init')


if __name__ == '__main__':
    c1 = Customer('123', 'Vinicius', 'Fartura')
    print(c1)
    print(c1.complete_data)
    print(asdict(c1))
    print(astuple(c1))
