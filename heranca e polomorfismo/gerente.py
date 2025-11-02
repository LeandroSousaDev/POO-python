from heranca.funcionario import Funcionario


class Gerente(Funcionario):
    def __init__(self, nome, salarioBase):
        super().__init__(nome, salarioBase)
        self.bonus = (super().calcularPagamento() * 20) / 100

    def calcularPagamento(self):
        return super().calcularPagamento() + ((super().calcularPagamento() * self.bonus) / 100)

genrente1 = Gerente("Mario", 100)
genrente1.exibirInformacoes()