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

    def cadastrar_cliente(self) -> Cliente | None:
        cliente = self.__tela_clientes.obter_dados_cliente(self.gerar_proximo_codigo())
        cliente_existente = self.busca_cliente(cliente.cpf)
        if cliente_existente:
            self.__tela_clientes.cpf_ja_cadastrado()
            return
        self.__clientes.append(cliente)
        self.__tela_clientes.sucesso_cadastro()
        return cliente

    def listar_clientes(self) -> list[Cliente]:
        if not self.__clientes:
            self.__tela_clientes.sem_cadastro()
        else:
            self.__tela_clientes.exibir_clientes(self.__clientes)
        return self.__clientes

    def busca_cliente(self, cpf=None):
        if cpf is None:
            cpf = self.__tela_clientes.obter_cpf(Operacao.BUSCA)

        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                self.__tela_clientes.exibir_cliente(cliente)
                return cliente
        self.__tela_clientes.cadastro_nao_encontrado()

    def exclui_cliente(self) -> Cliente:
        cpf = self.__tela_clientes.obter_cpf(Operacao.EXCLUI)
        cliente = self.busca_cliente(cpf)

        if cliente:
            self.__clientes.remove(cliente)
            self.__tela_clientes.sucesso_exclusao(cliente.nome)
            return cliente
        else:
            self.__tela_clientes.cadastro_nao_encontrado()

    def editar_cliente(self):
        cpf = self.__tela_clientes.obter_cpf(Operacao.EDITA)
        cliente = self.busca_cliente(cpf)

        if cliente:
            cliente_atualizado = self.__tela_clientes.editar_dados_cliente(cliente)
            self.__clientes[self.__clientes.index(cliente)] = cliente_atualizado
            self.__tela_clientes.sucesso_alteracao()
            self.__tela_clientes.exibir_cliente(cliente_atualizado)
            return cliente_atualizado
        else:
            self.__tela_clientes.cadastro_nao_encontrado()

    def adicionar_mock_clientes(self):
        self.__clientes.extend(lista_clientes_mock)

    def gerar_proximo_codigo(self) -> int:
        if not self.__clientes:
            return 1
        max_codigo = max(cliente.codigo for cliente in self.__clientes)
        return max_codigo + 1
