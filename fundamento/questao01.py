class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibirInformacoes(self):
        print(f"Marca: self.marca")
        print(self.modelo)
        print(self.ano)


carro1 = Carro(modelo="Civic", marca="Honda", ano=2025)
carro1.exibirInformacoes()
