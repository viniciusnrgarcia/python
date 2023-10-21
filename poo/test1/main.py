from contas import ContaPoupanca, ContaCorrente


if __name__ == '__main__':
    cp = ContaPoupanca(111, 222, 0)
    # cp.sacar(1)
    # cp.depositar(10)
    # cp.sacar(4)

    cc = ContaCorrente(333, 3333, 0, 10)
    cc.sacar(2)
    cc.sacar(2)
    cc.sacar(6)
    cc.sacar(1)
    cc.depositar(2)
    cc.sacar(25)
    cc.sacar(2)
    cc.sacar(1)
    cc.sacar(1)
