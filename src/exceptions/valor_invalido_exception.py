class ValorInvalidoException(Exception):
    def __init__(self, mensagem="Valor inválido fornecido."):
        self.mensagem = mensagem
        super().__init__(self.mensagem)
