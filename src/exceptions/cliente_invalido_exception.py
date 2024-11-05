class ClienteInvalidoException(Exception):
    def __init__(self):
        super().__init__("Cliente inválido.")
