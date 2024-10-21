from src.model.pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, cpf: int, nome: str, data_nasc: str, categoria: int):
        super().__init__(cpf, nome, data_nasc)
        self.__categoria = None
        if isinstance(categoria, int):
            self.__categoria = categoria

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria):
        if isinstance(categoria, int):
            self.__categoria = categoria
