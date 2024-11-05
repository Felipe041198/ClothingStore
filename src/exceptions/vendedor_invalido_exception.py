class VendedorInvalidoException(Exception):
    def __init__(self):
        super().__init__("Vendedor inválido.")
