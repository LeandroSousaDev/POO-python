class NotaInvalidaError(Exception):
    def __init__(self):
        super().__init__("a nota esta invalida")


class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.nota = 0

    def definir_nota(self, valor):
        if valor >= 0 and valor <= 10:
            self.nota = valor
        else:
            raise NotaInvalidaError()

try:
    aluno1 = Aluno("Mateus")
    aluno1.definir_nota(11)

    print(aluno1.nota)
except NotaInvalidaError as e:
    print(e)


