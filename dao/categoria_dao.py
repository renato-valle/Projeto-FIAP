from model.categoria import Categoria


class CategoriaDAO:
    def __init__(self) -> None:
        self.__categorias: list[Categoria] = list()

    def listar(self) -> list[Categoria]:
        return self.__categorias

    def adicionar(self, categoria: Categoria) -> None:
        self.__categorias.append(categoria)

    def remover(self, categoria_id: int) -> bool:
        for c in self.__categorias:
            if c.id == categoria_id:
                index = self.__categorias.index(c)
                self.__categorias.pop(index)
                return True  # encontrado

        return False  # não encontrado

    def buscar_por_id(self, categora_id) -> Categoria:
        cat = None
        for c in self.__categorias:
            if c.id == categora_id:
                cat = c
                break

        return cat

    def ultimo_id(self) -> int:
        index = len(self.__categorias) - 1
        if index == -1:
            id = 0
        else:
            id = self.__categorias[index].id

        return id
