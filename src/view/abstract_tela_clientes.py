from abc import ABC, abstractmethod
from src.model.cliente import Cliente
from src.utils.enum_operacoes import Operacao


class AbstractTelaClientes(ABC):
    @abstractmethod
    def menu(self, opcoes):
        pass

    @abstractmethod
    def obter_dados_cliente(self):
        pass

    @abstractmethod
    def obter_cpf(self, tipo_busca: Operacao) -> int:
        pass

    @abstractmethod
    def sucesso_cadastro(self):
        pass

    @abstractmethod
    def sucesso_alteracao(self):
        pass

    @abstractmethod
    def sucesso_exclusao(self, nome_cliente: str):
        pass

    @abstractmethod
    def sem_clientes(self):
        pass

    @abstractmethod
    def cliente_nao_encontrado(self):
        pass

    @abstractmethod
    def exibir_cliente(self, cliente: Cliente):
        pass

    @abstractmethod
    def exibir_clientes(self, clientes):
        pass

    @abstractmethod
    def editar_dados_cliente(self, cliente: Cliente):
        pass
