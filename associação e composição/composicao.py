class Componente:
    def __init__(self,nome,modelo):
        self.nome = nome
        self.modelo = modelo

class Computador:
    def __init__(self,nome):
        self.nome = nome
        self.componentes = []

    def adicionar_componente(self,nome,modelo):
        self.componentes.append(Componente(nome, modelo))
        
    def listarComponentes(self):
        for componente in self.componentes:
            print(f"{componente.nome}, {componente.modelo}")


computador = Computador("PC")
computador.adicionar_componente("processador", "intel")
computador.adicionar_componente("memoria", "Sandisck")
computador.listarComponentes()