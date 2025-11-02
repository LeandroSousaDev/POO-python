class Livro:
    def __init__(self, tutulo, autor, anoPublicacao):
        self.titulo = tutulo
        self.autor = autor
        self.anoPublicacao = anoPublicacao

    def detalhes(self):
        return {
            "titulo": self.titulo,
            "autor:": self.autor,
            "ano publicação": self.anoPublicacao
        }

livro1 = Livro("Harry Potter e a Pedra Filosofal",
               "J.K. Rowling",
               2007)

livro2 = Livro("Harry Potter e a Camara Secreta",
               "J.K. Rowling",
               2008)

livro3 = Livro("Harry Potter e a Prisioneiro e azkaban",
               "J.K. Rowling",
               2009)

listaLivros = [
    {"livro 1": livro1.detalhes()},
    {"livro 2": livro2.detalhes()},
    {"livro 3": livro3.detalhes()}
]

print(listaLivros)