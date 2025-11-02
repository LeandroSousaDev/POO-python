from animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, sexo, raca):
        super().__init__(nome, sexo)
        self.raca = raca

    def emitir_som(self):
        return f"{self.nome} esta latindo"

cachorro = Cachorro("Rex", "macho", "Poodle")
print(cachorro.emitir_som())