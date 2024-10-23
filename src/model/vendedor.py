from pessoa import Pessoa


class Vendedor(Pessoa):

    def __init__(self, cpf: int, nome: str, data_nasc: str, codigo: int):
        super().__init__(cpf, nome, data_nasc)
        self.__codigo = None
        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, int):
            self.__codigo = codigo
