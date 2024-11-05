from cliente import Cliente
from vendedor import Vendedor


class Relatorio:

    def __init__(self, vendas=None):
        self.__vendas = vendas if vendas is not None else []
        self.__cliente = None
        self.__vendedor = None

    @property
    def vendas(self):
        return self.__vendas

    @vendas.setter
    def vendas(self, vendas):
        if not isinstance(vendas, list):
            raise TypeError("Vendas inválidas.")
        self.__vendas = vendas

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        if cliente and not isinstance(cliente, Cliente):
            raise TypeError("O cliente inválido.")
        self.__cliente = cliente

    @property
    def vendedor(self):
        return self.__vendedor

    @vendedor.setter
    def vendedor(self, vendedor):
        if vendedor and not isinstance(vendedor, Vendedor):
            raise TypeError("O vendedor inválido")
        self.__vendedor = vendedor
