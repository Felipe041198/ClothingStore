class ItemVenda:
    def __init__(
            self,
            codigo_produto: int,
            quantidade: int,
            preco_venda: float,
    ):
        self.__codigo_produto = codigo_produto
        self.__quantidade = quantidade
        self.__preco_venda = preco_venda

    @property
    def codigo_produto(self):
        return self.__codigo_produto

    @codigo_produto.setter
    def codigo_produto(self, codigo_produto):
        if not isinstance(codigo_produto, int):
            raise TypeError("O código do produto deve ser um número inteiro.")
        self.__codigo_produto = codigo_produto

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        if not isinstance(quantidade, int):
            raise TypeError("A quantidade deve ser um número inteiro.")
        self.__quantidade = quantidade

    @property
    def preco_venda(self):
        return self.__preco_venda

    @preco_venda.setter
    def preco_venda(self, preco_venda):
        if not isinstance(preco_venda, (int, float)):
            raise TypeError("Preço do produto inválido.")
        if preco_venda < 0:
            raise ValueError("O preço do produto não pode ser negativo.")
        self.__preco_venda = preco_venda
