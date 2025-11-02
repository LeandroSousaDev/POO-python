class Funcionario:
    def __init__(self, nome, salarioBase):
        self.nome = nome
        self.__salarioBase = salarioBase

    def calcularPagamento(self):
        return self.__salarioBase

    def exibirInformacoes(self):
        print(f"Funcionário: {self.nome} - Salario: R${self.calcularPagamento()}")


funcionario1 = Funcionario("Marcos", 1000)
funcionario1.exibirInformacoes()