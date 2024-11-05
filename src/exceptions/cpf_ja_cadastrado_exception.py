class CpfJahCadastradoException(Exception):
    def __init__(self):
        super().__init__("O cpf já está cadastrado.")
