class ContaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    def getTitular(self):
        return self.__titular
    
    def setTitular(self, titular):
        self.__titular = titular

    def getSaldo(self):
        return self.__saldo
    
    def setTitular(self, saldo):
        self.__saldo = saldo

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
    
    def transferir(self, emissor, recepitor, valor):
        emissor.sacar(valor)

        recepitor.depositar(valor)


mario = ContaBancaria(1524, 100)
marcos = ContaBancaria(1245, 100)

try:
    mario.sacar(-10)
except Exception as e:
    print(e)

mario.transferir(mario, marcos, 10)

print(mario.mostraSaldo())
print(marcos.mostraSaldo())
   