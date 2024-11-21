from src.model.produto import Produto
from src.utils.enum_tipo_movimentacao import TipoMovimentacao


class Movimentacao:

    def __init__(
            self,
            produto: Produto,
            quantidade: int,
            tipo: TipoMovimentacao
    ):
        self.__produto = produto
        self.__quantidade = quantidade
        self.__tipo = tipo

    @property
    def produto(self) -> Produto:
        return self.__produto

    @produto.setter
    def produto(self, produto: Produto):
        self.__produto = produto

    @property
    def quantidade(self) -> int:
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade: int):
        self.__quantidade = quantidade

    @property
    def tipo(self) -> TipoMovimentacao:
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: TipoMovimentacao):
        self.__tipo = tipo
