from src.model.pessoa import Pessoa
from src.utils.enum_categoria_cliente import CategoriaCliente


class Cliente(Pessoa):
    def __init__(self, cpf: str, nome: str, data_nasc: str, categoria: CategoriaCliente, codigo: int):
        super().__init__(cpf, nome, data_nasc, codigo)
        self.__categoria = None
        if isinstance(categoria, CategoriaCliente):
            self.__categoria = categoria

    @property
    def categoria(self) -> CategoriaCliente:
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria):
        if isinstance(categoria, CategoriaCliente):
            self.__categoria = categoria
