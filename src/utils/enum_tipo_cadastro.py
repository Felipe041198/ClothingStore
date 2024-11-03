from enum import Enum


class TipoCadastro(Enum):
    CLIENTE = ("cliente", "clientes", "CPF")
    VENDEDOR = ("vendedor", "vendedores", "CPF")
    PRODUTO = ("produto", "produtos", "código")
    PEDIDO = ("pedidos", "pedido", "código")

    def __init__(self, singular, plural, identificador):
        self.singular = singular
        self.plural = plural
        self.identificador = identificador
