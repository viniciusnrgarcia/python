# PEP 557 adicionado versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html

import json
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

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


if __name__ == '__main__':
    c1 = Customer('123', 'Vinicius', 'Fartura')
    print(c1)
    print(c1.complete_data)
    print(asdict(c1))
    print(astuple(c1))

    print(c1.__dict__)

    print(c1.toJSON())
