from pessoas import Pessoa
import contas


class Cliente(Pessoa):

    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: contas.Conta | None = None


if __name__ == '__main__':
    c1 = Cliente('Vinicius', 35)
    c1.conta = contas.ContaCorrente(1001, 5515121, 1000, 5000)
    print(c1)
    print(c1.conta)
