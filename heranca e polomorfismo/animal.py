class Animal:
    def __init__(self, nome, sexo):
        self.nome = nome
        self.sexo = sexo

    def emitir_som(self):
        return "Som genérico"


class Cachorro(Animal):
    def emitir_som(self):
        return "Au au"


class Gato(Animal):
    def emitir_som(self):
        return "Miau"

class Passaro(Animal):
    def emitir_som(self):
        return "piu piu"

class Leao(Animal):
    def emitir_som(self):
        return super().emitir_som()

animais = [Cachorro("Caramelo", "Macho"), Gato("Tom", "Macho"), Passaro("Piu-piu", "Macho"), Leao("Simba", "Macho")]


for animal in animais:
    print(f"{animal.nome}: {animal.emitir_som()}")
