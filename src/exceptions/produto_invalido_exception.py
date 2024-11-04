class ProdutoInvalidoException(Exception):
    def __init__(self):
        super().__init__("Produto inválido.")
