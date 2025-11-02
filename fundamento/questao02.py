class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        respota = (self.nota1 + self.nota2) / 2
        return respota

    def situacao(self):
        if self.media() >= 6:
            print(f"{self.nome}: aprovado")
        else:
            print(f"{self.nome}: reprovado")

aluno1 = Aluno("Mario", 6.0, 8.0)
aluno1.situacao()
print(f"media: {aluno1.media()}")