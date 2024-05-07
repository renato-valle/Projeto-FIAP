from model.autor import Autor
from model.editora import Editora
from model.categoria import Categoria


class Livro:
    def __init__(self,
                 id: int,
                 titulo: str,
                 resumo: str,
                 ano: int,
                 paginas: int,
                 isbn: str,
                 categoria: Categoria,
                 editora: Editora,
                 autor: Autor) -> None:
        self.__id = id
        self.__titulo = titulo
        self.__resumo = resumo
        self.__ano = ano
        self.__paginas = paginas
        self.__isbn = isbn
        self.__categoria = categoria
        self.__editora = editora
        self.__autor = autor

    def __str__(self) -> str:
        return f'Id: {self.__id} | Título: {self.__titulo} | Resumo: {self.__resumo} | Ano: {self.__ano} | Páginas: {self.__paginas} | Isbn: {self.__isbn} | Categoria: {self.categoria.nome} | Editora: {self.editora.nome} | Autor: {self.autor.nome}'

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    @property
    def resumo(self) -> str:
        return self.__resumo

    @resumo.setter
    def resumo(self, resumo: str):
        self.__resumo = resumo

    @property
    def ano(self) -> int:
        return self.__ano

    @ano.setter
    def ano(self, ano: int):
        self.__ano = ano

    @property
    def paginas(self) -> int:
        return self.__paginas

    @paginas.setter
    def paginas(self, paginas: int):
        self.__paginas = paginas

    @property
    def isbn(self) -> str:
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn: str):
        self.__isbn = isbn

    @property
    def categoria(self) -> Categoria:
        return self.__categoria

    @categoria.setter
    def categoria(self, cat: Categoria):
        self.__categoria = cat

    @property
    def editora(self) -> Editora:
        return self.__editora

    @editora.setter
    def editora(self, ed: Editora):
        self.__editora = ed

    @property
    def autor(self) -> Autor:
        return self.__autor

    @autor.setter
    def autor(self, autor: Autor):
        self.__autor = autor
