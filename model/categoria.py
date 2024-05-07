class Categoria:
    def __init__(self, id: int, nome: str) -> None:
        self.__id: int = id
        self.__nome: str = nome

    def __str__(self) -> str:
        return f'{self.id} | {self.nome}'

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
