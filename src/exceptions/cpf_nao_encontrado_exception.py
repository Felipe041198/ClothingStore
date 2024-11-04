class CpfNaoEncontradoException(Exception):
    def __init__(self):
        super().__init__("O cpf não foi encontrado.")
