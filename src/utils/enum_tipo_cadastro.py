from enum import Enum


class TipoCadastro(Enum):
    CLIENTE = ("cliente", "clientes")
    VENDEDOR = ("vendedor", "vendedores")

    def __init__(self, singular, plural):
        self.singular = singular
        self.plural = plural
