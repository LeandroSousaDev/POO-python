class ContaBancaria:
    def __init__(self, titular, saldo, numeroDaConta):
        self.__titular = titular
        self.__numeroDaConta = numeroDaConta
        self.__saldo = saldo

    def getTitular(self):
        return self.__titular

    def setTitular(self, titular):
        if isinstance(titular, str) and len(titular.strip()) > 0:
            self.__titular = titular
        else:
            raise ValueError("nome do titular invalido")

    def getSaldo(self):
        return self.__saldo

    def setSaldo(self, saldo):
        if isinstance(saldo, int):
            self.__saldo = saldo
        else:
            raise ValueError("Saldo deve ser um numero")

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("deve depositar um valor maior que zero")
        else:
            self.__saldo += valor

    def sacar(self, valor):
        if self.__saldo < valor:
            raise ValueError("Não tem saldo sufciente")
        elif valor <= 0:
            raise ValueError("valor do saque ver ser um numero positivo")
        else:
            self.__saldo -= valor

    def mostraSaldo(self):
        return f"Conta: {self.getTitular()}, Saldo: {self.getSaldo()}"

    def transferir(self, recepitor, valor):
        self.sacar(valor)
        recepitor.depositar(valor)



conta1 = ContaBancaria("Mario" ,100, 1524)
conta2 = ContaBancaria("Marcos", 100, 1254)

try:
    conta1.setTitular("Leandro")
    print(conta1.mostraSaldo())
except Exception as e:
    print(e)

