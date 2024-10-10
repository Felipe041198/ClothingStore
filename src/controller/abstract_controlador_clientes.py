from abc import ABC, abstractmethod


class AbstractControladorClientes(ABC):

    # Permite cadastrar um novo cliente
    @abstractmethod
    def cadastrar_cliente(self):
        pass

    # Retorna a lista de clientes
    @abstractmethod
    def listar_clientes(self) -> list:
        pass
