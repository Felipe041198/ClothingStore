from datetime import date

from src.model.cliente import Cliente
from src.model.item_venda import ItemVenda
from src.model.vendedor import Vendedor


class Venda:
    def __init__(self, cliente: Cliente, vendedor: Vendedor, produtos: list[ItemVenda]):
        self.__cliente = cliente
        self.__vendedor = vendedor
        self.__produtos = produtos
        self.__data_venda = date.today()
        self.__valor_total = self.calcular_total()

    def calcular_total(self) -> float:
        return sum(produto.preco_venda * produto.quantidade for produto in self.__produtos)

    @property
    def valor_total(self) -> float:
        return self.__valor_total

    @property
    def cliente(self) -> Cliente:
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        if not isinstance(cliente, Cliente):
            raise TypeError("Cliente inválido.")
        self.__cliente = cliente

    @property
    def vendedor(self) -> Vendedor:
        return self.__vendedor

    @vendedor.setter
    def vendedor(self, vendedor):
        if not isinstance(vendedor, Vendedor):
            raise TypeError("Vendedor inválido.")
        self.__vendedor = vendedor

    @property
    def data_venda(self) -> date:
        return self.__data_venda

    @property
    def produtos(self) -> list[ItemVenda]:
        return self.__produtos

    @produtos.setter
    def produtos(self, produtos):
        for produto in produtos:
            if not isinstance(produto, ItemVenda):
                raise TypeError("Produto invalido.")
        self.__produtos = produtos
        # Recalcula se algo mudar
        self.__valor_total = self.calcular_total()
