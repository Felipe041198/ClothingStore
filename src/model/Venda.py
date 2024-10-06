from Validador import Validador
from Cliente import Cliente
from Vendedor import Vendedor
from Produto import Produto

class Venda:
    def __init__(self, cliente:Cliente, vendedor: Vendedor, produtos:list[Produto], data_venda: str):
        self.__cliente = cliente
        self.__vendedor = vendedor
        self.__produtos = produtos
        self.__data_venda = Validador.validar_data_nascimento(data_venda)
        self.__valor_total = self.calcular_total()

    def calcular_total(self):
        return sum(produto.preco for produto in self.produtos)

    @property
    def valor_total(self):
        return self.__valor_total

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        if not isinstance(cliente,  Cliente):
            raise TypeError("Cliente inválido.")
        self.__cliente = cliente

    @property
    def vendedor(self):
        return self.__vendedor

    @vendedor.setter
    def vendedor(self, vendedor):
        if not isinstance(vendedor,  Vendedor):
            raise TypeError("Vendedor inválido.")
        self.__vendedor = vendedor

    @property
    def data_venda(self):
        return self.__data_venda

    @data_venda.setter
    def data_venda(self, data_venda):
        self.__data_venda = Validador.validar_data_nascimento(data_venda)

    @property
    def produtos(self):
        return self.__produtos

    @produtos.setter
    def produtos(self, produtos):
        if not isinstance(produtos, list):
            raise TypeError("Produtos deve ser uma lista.")
        for produto in produtos:
            if not isinstance(produto, Produto):
                raise TypeError("Produto não cadastrado.")
        self.__produtos = produtos
        self.__valor_total = self.calcular_total() #recalcula se algo mudar
