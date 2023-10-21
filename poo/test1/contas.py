import abc

"""Classe abstrata + uso 'abc'
"""
class Conta(abc.ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod    
    def depositar(self, valor):
        saldo += valor
        self.detalhe(f'CREDITO {valor}')


    def sacar(self, valor):
        saldo -= valor
        self.detalhe(f'DEBITO {valor}')


    def detalhe(self, msg=''):
        print(f'Saldo atual {self.saldo:.2f} {msg}')


class ContaPoupanca(Conta):
    def sacar(self, valor):
        v = self.saldo - valor
        if v >= 0:
            self.saldo -= valor
            self.detalhe(f'DEBITO POUPANCA {valor}')
            return self.saldo
        
        print('VALOR NÃO DISPONIVEL')
        self.detalhe(f'(DEBITO NEGADO {valor})')


if __name__ == '__main__':
    cp = ContaPoupanca(111, 222, 0)
    cp.sacar(1)