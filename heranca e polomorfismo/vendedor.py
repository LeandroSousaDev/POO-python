from heranca.funcionario import Funcionario


class Vendedor(Funcionario):
    def __init__(self, nome, salarioBase):
        super().__init__(nome, salarioBase)
        self.bonus = (super().calcularPagamento() * 20) / 100

    def calcularPagamento(self):
        return super().calcularPagamento() + self.bonus

vendedor1 = Vendedor("Matheus", 700)
vendedor1.exibirInformacoes()