from src.controller.abstract_controlador import AbstractControlador
from src.dao.dao_generic import DAOGeneric
from src.exceptions.cpf_nao_encontrado_exception import CpfNaoEncontradoException
from src.exceptions.nenhum_registro_encontrado_exception import NenhumRegistroEncontradoException
from src.mocks.cliente_mock import lista_clientes_mock
from src.model.cliente import Cliente
from src.utils.decorators import tratar_excecoes
from src.utils.enum_operacoes import Operacao
from src.view.tela_gui_clientes import TelaClientes


class ControladorClientes(AbstractControlador):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__tela_clientes = TelaClientes()
        self.__clientes_dao = DAOGeneric("clientes")
        self.__clientes = self.__clientes_dao.carregar()

    @property
    def clientes(self) -> list[Cliente]:
        return self.__clientes

    @property
    def clientes_dict(self) -> list[dict]:
        if self.__clientes:
            lista_clientes = []
            for cliente in self.__clientes:
                lista_clientes.append(cliente.to_dict())
            return lista_clientes
        raise NenhumRegistroEncontradoException

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastrar_cliente,
            2: self.listar_clientes,
            3: self.busca_cliente_cpf,
            4: self.exclui_cliente,
            5: self.editar_cliente,
            99: self.adicionar_mock_clientes,
            0: self.retornar
        }

        while True:
            opcao = self.__tela_clientes.menu(list(lista_opcoes.keys()))
            lista_opcoes[opcao]()

    @tratar_excecoes
    def cadastrar_cliente(self) -> Cliente | None:
        dados_cliente, should_exit_to_menu = self.__tela_clientes.obter_dados_cliente(
            self.gerar_proximo_codigo(),
        )

        if should_exit_to_menu or not dados_cliente:
            return None

        cpf_existente = self.pesquisa_cliente(dados_cliente["cpf"])
        if cpf_existente:
            self.__tela_clientes.mostrar_erro("CPF já cadastrado. Insira um CPF diferente.")
            return None

        cliente = Cliente(**dados_cliente)
        self.__clientes.append(cliente)

        self.__tela_clientes.sucesso_cadastro()
        self.__tela_clientes.exibir_cliente(dados_cliente)
        return cliente

    @tratar_excecoes
    def listar_clientes(self) -> list[Cliente]:
        if not self.__clientes:
            self.__tela_clientes.sem_cadastro()
        else:
            self.__tela_clientes.exibir_clientes(self.clientes_dict)
        return self.__clientes

    @tratar_excecoes
    def busca_cliente(self) -> Cliente | None:
        cpf = self.__tela_clientes.obter_cpf(Operacao.BUSCA)

        if not cpf:
            return None

        cliente = self.pesquisa_cliente(cpf)

        if cliente:
            return cliente

        raise CpfNaoEncontradoException

    @tratar_excecoes
    def busca_cliente_cpf(self) -> Cliente | None:
        cpf = self.__tela_clientes.obter_cpf(Operacao.BUSCA)

        if not cpf:
            return None

        cliente = self.pesquisa_cliente(cpf)

        if cliente:
            self.__tela_clientes.exibir_cliente(cliente.to_dict())
            return cliente

        raise CpfNaoEncontradoException

    @tratar_excecoes
    def editar_cliente(self) -> Cliente | None:
        cpf = self.__tela_clientes.obter_cpf(Operacao.EDITA)
        if not cpf:
            return None

        cliente = self.pesquisa_cliente(cpf)

        if cliente:
            dados_cliente_original = cliente.to_dict()
            dados_cliente_atualizado, should_exit_to_menu = self.__tela_clientes.editar_dados_cliente(
                dados_cliente_original)

            if should_exit_to_menu or not dados_cliente_atualizado:
                return None

            if dados_cliente_original == dados_cliente_atualizado:
                return None

            cliente_atualizado = Cliente(**dados_cliente_atualizado)
            self.__clientes[self.__clientes.index(cliente)] = cliente_atualizado

            self.__tela_clientes.sucesso_alteracao()
            self.__tela_clientes.exibir_cliente(dados_cliente_atualizado)
            return cliente_atualizado

        self.__tela_clientes.cadastro_nao_encontrado()

    @tratar_excecoes
    def exclui_cliente(self) -> Cliente | None:
        cpf = self.__tela_clientes.obter_cpf(Operacao.EXCLUI)
        if not cpf:
            return None
        cliente = self.pesquisa_cliente(cpf)

        if cliente:
            self.__clientes.remove(cliente)
            self.__tela_clientes.sucesso_exclusao(cliente.nome)
            return cliente

        self.__tela_clientes.cadastro_nao_encontrado()

    def pesquisa_cliente(self, cpf: str) -> Cliente | None:
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def gerar_proximo_codigo(self) -> int:
        if not self.__clientes:
            return 1
        max_codigo = max(cliente.codigo for cliente in self.__clientes)
        return max_codigo + 1

    def adicionar_mock_clientes(self):
        self.__clientes.extend(lista_clientes_mock)

    def mostrar_erro(self, e: str):
        self.__tela_clientes.mostrar_erro(e)

    def salvar_clientes(self):
        self.__clientes_dao.salvar(self.__clientes)
