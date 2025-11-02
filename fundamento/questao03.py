class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def exibirSaldo(self):
        print(self.saldo)

pessoa1 = ContaBancaria("Mario", 0)
pessoa1.depositar(100)
pessoa1.sacar(10)
pessoa1.exibirSaldo()
