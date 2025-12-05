class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.diciplinas = []
    
    def adicionarDiciplina(self, diciplina):
        if diciplina not in self.diciplinas:
            self.diciplinas.append(diciplina)
            diciplina.adicionarProfessor(self)


class Diciplina:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []

    def adicionarProfessor(self, professor):
        if professor not in self.professores:
            self.professores.append(professor)
            professor.adicionarDiciplina(self)


professor1 = Professor("Marcos")
diciplina1 = Diciplina("Java")
diciplina2 = Diciplina("Js")
professor1.adicionarDiciplina(diciplina1)
professor1.adicionarDiciplina(diciplina2)

for professor in diciplina2.professores:
    print(professor.nome)

