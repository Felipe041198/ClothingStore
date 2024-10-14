from abc import ABC, abstractmethod
from typing import List

from src.model.cliente import Cliente


class AbstractControladorClientes(ABC):

    # Permite cadastrar um novo cliente
    @abstractmethod
    def cadastrar_cliente(self):
        pass

    # Retorna a lista de clientes
    @abstractmethod
    def listar_clientes(self) -> List[Cliente]:
        pass

    # Retorna um cpf da UI
    @abstractmethod
    def busca_cliente(self) -> int:
        pass

    # Retorna um cliente buscando pelo CPF
    @abstractmethod
    def lista_cliente(self, cpf: int) -> Cliente | None:
        pass

    # Edita um cliente buscando pelo CPF
    @abstractmethod
    def editar_cliente(self):
        pass

    # Retorna a lista de clientes
    @abstractmethod
    def exclui_cliente(self):
        pass
