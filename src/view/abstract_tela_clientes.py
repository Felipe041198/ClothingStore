from abc import ABC, abstractmethod


class AbstractTelaClientes(ABC):
    @abstractmethod
    def menu(self):
        pass

    @abstractmethod
    def obter_dados_cliente(self):
        pass

    @abstractmethod
    def sucesso_cadastro(self):
        pass

    @abstractmethod
    def sem_clientes(self):
        pass

    @abstractmethod
    def exibir_clientes(self, clientes):
        pass

    @abstractmethod
    def opcao_invalida(self):
        pass