from abc import ABC, abstractmethod


class AbstractControladorClientes(ABC):

    # Permite cadastrar um novo cliente
    @abstractmethod
    def cadastrar_cliente(self):
        pass

    # Retorna a lista de clientes
    @abstractmethod
    def listar_clientes(self):
        pass

    # Retorna um cliente buscando pelo CPF
    @abstractmethod
    def busca_cliente(self):
        pass

    # Edita um cliente buscando pelo CPF
    @abstractmethod
    def editar_cliente(self):
        pass

    # Retorna a lista de clientes
    @abstractmethod
    def exclui_cliente(self):
        pass
