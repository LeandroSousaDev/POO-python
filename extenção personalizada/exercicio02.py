class Produto:
    def __init__(self, nome):
        self.nome = nome
        self.preco = 0

    def detalhes(self):
        return f"produto: {self.nome}, preço: R${self.preco:.2f}"

    def alterar_preco(self, valor):
        try:
            if valor > 0:
                self.preco = valor
            else:
                raise ValueError("valor não pode ser um numero negativo")
        except ValueError as e:
            print(e)


item = Produto("Arroz")
item.alterar_preco(-5)
print(item.detalhes())
