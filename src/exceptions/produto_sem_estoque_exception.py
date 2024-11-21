class ProdutoSemEstoqueException(Exception):
    def __init__(self):
        super().__init__("O produto está sem o estoque disponível.")
