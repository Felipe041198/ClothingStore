class NenhumRegistroEncontradoException(Exception):
    def __init__(self):
        super().__init__("Nenhum registro encontrado.")
