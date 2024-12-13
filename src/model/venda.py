from datetime import date

from src.exceptions.cliente_invalido_exception import ClienteInvalidoException
from src.exceptions.produto_invalido_exception import ProdutoInvalidoException
from src.exceptions.vendedor_invalido_exception import VendedorInvalidoException
from src.model.cliente import Cliente
from src.model.item_venda import ItemVenda
from src.model.vendedor import Vendedor


class Venda:
    def __init__(self, cliente: Cliente, vendedor: Vendedor, data: date = None):
        self.__cliente = cliente
        self.__vendedor = vendedor
        # Renomear para item vendas
        self.__produtos = []
        if data is None:
            self.__data_venda = date.today().strftime("%d/%m/%Y")
        else:
            self.__data_venda = data.strftime("%d/%m/%Y") if isinstance(data, date) else data
        self.__valor_total = 0

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
            raise ClienteInvalidoException
        self.__cliente = cliente

    @property
    def vendedor(self) -> Vendedor:
        return self.__vendedor

    @vendedor.setter
    def vendedor(self, vendedor):
        if not isinstance(vendedor, Vendedor):
            raise VendedorInvalidoException
        self.__vendedor = vendedor

    @property
    def data_venda(self) -> date:
        return self.__data_venda

    @property
    def produtos(self) -> list[ItemVenda]:
        return self.__produtos

    @property
    def produtos_dict(self) -> list[dict]:
        lista_produtos = []
        for produto in self.__produtos:
            lista_produtos.append(produto.to_dict())
        return lista_produtos

    @produtos.setter
    def produtos(self, produtos):
        for produto in produtos:
            if not isinstance(produto, ItemVenda):
                raise ProdutoInvalidoException
        self.__produtos = produtos
        # Recalcula se algo mudar
        self.__valor_total = self.calcular_total()

    def adiciona_items(self, lista_items: list[dict]):
        for item in lista_items:
            self.__produtos.append(
                ItemVenda(
                    codigo_produto=item["codigo"],
                    quantidade=item["quantidade"],
                    preco_venda=item["preco"],
                )
            )
        self.__valor_total = self.calcular_total()

    def to_dict(self):
        return {
            "cliente": self.cliente.to_dict(),
            "vendedor": self.vendedor.to_dict(),
            "produtos": self.produtos_dict,
            "data_venda": self.data_venda,
            "valor_total": self.valor_total,
        }
