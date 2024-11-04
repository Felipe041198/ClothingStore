from src.controller.abstract_controlador import AbstractControlador
from src.exceptions.cpf_ja_cadastrado_exception import CpfJahCadastradoException
from src.exceptions.cpf_nao_encontrado_exception import CpfNaoEncontradoException
from src.exceptions.nenhum_registro_encontrado_exception import NenhumRegistroEncontradoException
from src.mocks.cliente_mock import lista_clientes_mock
from src.model.cliente import Cliente
from src.utils.decorators import tratar_excecoes
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

    @tratar_excecoes
    def cadastrar_cliente(self) -> Cliente | None:
        cliente = self.__tela_clientes.obter_dados_cliente(self.gerar_proximo_codigo())

        if self.pesquisa_cliente(cliente.cpf):
            raise CpfJahCadastradoException
        self.__clientes.append(cliente)
        self.__tela_clientes.sucesso_cadastro()
        return cliente

    @tratar_excecoes
    def listar_clientes(self) -> list[Cliente]:
        if self.__clientes:
            self.__tela_clientes.exibir_clientes(self.__clientes)
            return self.__clientes
        raise NenhumRegistroEncontradoException

    @tratar_excecoes
    def busca_cliente(self) -> Cliente:
        cpf = self.__tela_clientes.obter_cpf(Operacao.BUSCA)

        cliente = self.pesquisa_cliente(cpf)
        if cliente:
            self.__tela_clientes.exibir_cliente(cliente)
            return cliente
        raise CpfNaoEncontradoException

    @tratar_excecoes
    def exclui_cliente(self) -> Cliente:
        cpf = self.__tela_clientes.obter_cpf(Operacao.EXCLUI)
        cliente = self.pesquisa_cliente(cpf)

        if cliente:
            self.__clientes.remove(cliente)
            self.__tela_clientes.sucesso_exclusao(cliente.nome)
            return cliente
        raise CpfNaoEncontradoException

    @tratar_excecoes
    def editar_cliente(self) -> Cliente:
        cpf = self.__tela_clientes.obter_cpf(Operacao.EDITA)
        cliente = self.pesquisa_cliente(cpf)

        if cliente:
            cliente_atualizado = self.__tela_clientes.editar_dados_cliente(cliente)
            self.__clientes[self.__clientes.index(cliente)] = cliente_atualizado
            self.__tela_clientes.sucesso_alteracao()
            self.__tela_clientes.exibir_cliente(cliente_atualizado)
            return cliente_atualizado
        raise CpfNaoEncontradoException

    def pesquisa_cliente(self, cpf: str) -> Cliente:
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                return cliente

    def gerar_proximo_codigo(self) -> int:
        if not self.__clientes:
            return 1
        max_codigo = max(cliente.codigo for cliente in self.__clientes)
        return max_codigo + 1

    def adicionar_mock_clientes(self):
        self.__clientes.extend(lista_clientes_mock)

    def mostrar_erro(self, e: str):
        self.__tela_clientes.mostrar_erro(e)
