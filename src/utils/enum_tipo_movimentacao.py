from enum import Enum


class TipoMovimentacao(Enum):
    SAIDA = (1, "Saída", "Saídas")
    ENTRADA = (2, "Entrada", "Entradas")

    def __init__(self, codigo, nome, plural):
        self.codigo = codigo
        self.nome = nome
        self.plural = plural

    @staticmethod
    def opcoes() -> list[int]:
        lista_codigos = []
        for movimentacao in TipoMovimentacao:
            lista_codigos.append(movimentacao.codigo)
        return lista_codigos

    @staticmethod
    def busca_movimentacao(codigo: int):
        for movimentacao in TipoMovimentacao:
            if movimentacao.codigo == codigo:
                return movimentacao
