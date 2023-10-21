import abc

"""Classe abstrata + uso 'abc'
"""


class Conta(abc.ABC):
    def __init__(self, agencia, conta, saldo=0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor: float) -> float:
        saldo -= valor
        print('abstract method')
        self.detalhe(f'DEBITO {valor}')

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhe(f'CREDITO {valor}')
        return self.saldo

    def detalhe(self, msg: str = ''):
        print(f'Saldo atual {self.saldo:.2f} {msg}')

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r},{self.saldo!r})'
        return f'{class_name}{attrs}'


class ContaPoupanca(Conta):
    def sacar(self, valor):
        v = self.saldo - valor
        if v >= 0:
            self.saldo -= valor
            self.detalhe(f'DEBITO POUPANCA {valor}')
            return self.saldo

        print('VALOR NÃO DISPONIVEL')
        self.detalhe(f'(DEBITO NEGADO {valor})')


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, limite=0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        v = self.saldo - valor
        l = -self.limite
        if v >= 0 or v >= l:
            self.saldo -= valor
            self.detalhe(f'DEBITO POUPANCA {valor}')
            return self.saldo

        # print(f'VALOR NÃO DISPONIVEL. LIMITE DISPONIVEL {self.limite}')
        self.detalhe(
            f'(DEBITO NEGADO {valor}). LIMITE DISPONIVEL {-self.limite - l:.2f}')

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r},{self.saldo!r}, '\
            f'{self.limite!r})'  # quebra de linha
        return f'{class_name}{attrs}'
