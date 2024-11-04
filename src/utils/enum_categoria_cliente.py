from enum import Enum


class CategoriaCliente(Enum):
    NORMAL = (1, "Normal")
    PREMIUM = (2, "Premium")

    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome

    @staticmethod
    def opcoes() -> list[int]:
        lista_codigos = []
        for categorias in CategoriaCliente:
            lista_codigos.append(categorias.codigo)
        return lista_codigos

    @staticmethod
    def busca_categoria(codigo: int):
        for categoria in CategoriaCliente:
            if categoria.codigo == codigo:
                return categoria
