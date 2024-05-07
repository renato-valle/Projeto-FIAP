from model.livro import Livro


class LivroDAO:
    def __init__(self) -> None:
        self.__livros: list[Livro] = list()

    def listar(self) -> list[Livro]:
        return self.__livros

    def adicionar(self, livro: Livro):
        self.__livros.append(livro)

    def remover(self, livro_id: int) -> bool:
        for liv in self.__livros:
            if liv.id == livro_id:
                index = self.__livros.index(liv)
                self.__livros.pop(index)
                return True

        return False

    def buscar_por_id(self, livro_id) -> Livro:
        for lv in self.__livros:
            if lv.id == livro_id:
                return lv

    def ultimo_id(self) -> int:
        index = len(self.__livros) - 1
        if index == -1:
            id = 0
        else:
            id = self.__livros[index].id

        return id
