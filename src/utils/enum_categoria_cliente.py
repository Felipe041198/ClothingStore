from enum import Enum


class CategoriaCliente(Enum):
    NORMAL = "Normal"
    PREMIUM = "Premium"


def busca_categoria(codigo: int) -> CategoriaCliente:
    categorias = {
        1: CategoriaCliente.NORMAL,
        2: CategoriaCliente.PREMIUM,
    }

    return categorias.get(codigo)
