class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def setLargura(self, largura):
        self.largura = largura

    def setAltura(self, altura):
        self.altura = altura

    def area(self):
        print(self.altura * self.largura)

    def perimetro(self):
        print(2 *(self.altura + self.largura))

retangulo1 = Retangulo(10, 3)
retangulo1.setLargura(15)
retangulo1.setAltura(5)
retangulo1.area()
retangulo1.perimetro()