class AtributoInvalidoProdutoException(Exception):
    def __init__(self, atributo):
        self.mensagem = "Atributo {} do produto invalido.".format(atributo)
        super().__init__(self.mensagem)
