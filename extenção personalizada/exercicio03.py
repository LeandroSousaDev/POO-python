class QuantidadeInvalidaError(Exception):
    def __init__(self):
        super().__init__("Valor da quantidade invalida")

class TipoInvalidoError(Exception):
    def __init__(self):
        super().__init__("Quantide de ser um numero")


class Pedido:
    def __init__(self, item):
        self.item = item
        self.quantidade = 0

    def definir_quantidade(self, quantidade):
        try:
            if not isinstance(quantidade,int):
                raise TipoInvalidoError()

            elif quantidade > 0:
                self.quantidade = quantidade

            else:
                raise QuantidadeInvalidaError()

        # except QuantidadeInvalidaError as e:
        #     print(e)
        #
        # except TipoInvalidoError as e:
        #     print(e)

        except Exception as e:
            print(e)

    def resumo(self):
        return f"item: {self.item}, quantidade: {self.quantidade}"

item = Pedido("Suco")
item.definir_quantidade(10)
print(item.resumo())
