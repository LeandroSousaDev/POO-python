class SaldoInsuficienteError(Exception):
    def __init__(self):
        super().__init__("Voce não tem saldo sufciente")

class ValorInvalidoError(Exception):
    def __init__(self):
        super().__init__("valor invalido")

class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo = valor
        else:
            raise ValorInvalidoError()


    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError()
        elif valor <= 0:
            raise ValorInvalidoError()
        else:
            self.saldo -= valor

    def detalhes(self):
        return f"Titular: {self.titular}, Saldo: R$ {self.saldo:.2f}"

try:
    conta1 = Conta("Marcos")
    conta1.depositar(100)
    conta1.sacar(5)
    print(conta1.detalhes())

except Exception as e:
    print(e)
