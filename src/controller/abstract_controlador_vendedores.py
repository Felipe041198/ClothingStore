from abc import ABC, abstractmethod


class AbstractControladorVendedores(ABC):
    @abstractmethod
    def cadastrar_vendedor(self):
        pass

    @abstractmethod
    def listar_vendedores(self):
        pass

    @abstractmethod
    def busca_vendedor(self):
        pass

    @abstractmethod
    def editar_vendedor(self):
        pass

    @abstractmethod
    def exclui_vendedor(self):
        pass
