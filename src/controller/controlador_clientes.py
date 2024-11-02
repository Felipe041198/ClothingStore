from src.controller.abstract_controlador import AbstractControlador
from src.mocks.cliente_mock import lista_clientes_mock
from src.model.cliente import Cliente
from src.utils.enum_operacoes import Operacao
from src.view.tela_clientes import TelaClientes


class ControladorClientes(AbstractControlador):

    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__tela_clientes = TelaClientes()
        self.__clientes = []

    @property
    def clientes(self) -> list[Cliente]:
        return self.__clientes

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastrar_cliente,
            2: self.listar_clientes,
            3: self.busca_cliente,
            4: self.exclui_cliente,
            5: self.editar_cliente,
            99: self.adicionar_mock_clientes,
            0: self.retornar
        }

        while True:
            lista_opcoes[self.__tela_clientes.menu(list(lista_opcoes.keys()))]()

    def cadastrar_cliente(self) -> Cliente:
        cliente = self.__tela_clientes.obter_dados_cliente()
        self.__clientes.append(cliente)
        self.__tela_clientes.sucesso_cadastro()
        return cliente

    def listar_clientes(self) -> list[Cliente]:
        if not self.__clientes:
            self.__tela_clientes.sem_cadastro()
        else:
            self.__tela_clientes.exibir_clientes(self.__clientes)
        return self.__clientes

    def busca_cliente(self):
        cpf = self.__tela_clientes.obter_cpf(Operacao.BUSCA)
        self.lista_cliente(cpf)

    def lista_cliente(self, cpf: int) -> Cliente:
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                self.__tela_clientes.exibir_cliente(cliente)
                return cliente
        self.__tela_clientes.cadastro_nao_encontrado()

    def exclui_cliente(self) -> Cliente:
        cpf = self.__tela_clientes.obter_cpf(Operacao.EXCLUI)
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                self.__clientes.remove(cliente)
                self.__tela_clientes.sucesso_exclusao(cliente.nome)
                return cliente
        self.__tela_clientes.cadastro_nao_encontrado()

    def editar_cliente(self) -> Cliente:
        cpf = self.__tela_clientes.obter_cpf(Operacao.EDITA)

        for i, cliente in enumerate(self.__clientes):
            if cliente.cpf == cpf:
                cliente_atualizado = self.__tela_clientes.editar_dados_cliente(cliente)
                self.__clientes[i] = cliente_atualizado  # Substitui o cliente na lista
                self.__tela_clientes.sucesso_alteracao()
                return cliente

        self.__tela_clientes.cadastro_nao_encontrado()

    def adicionar_mock_clientes(self):
        self.__clientes.extend(lista_clientes_mock)
