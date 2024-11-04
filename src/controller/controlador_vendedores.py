from src.controller.abstract_controlador import AbstractControlador
from src.mocks.vendedores_mock import lista_vendedores_mock
from src.model.vendedor import Vendedor
from src.utils.enum_operacoes import Operacao
from src.view.tela_vendedores import TelaVendedores


class ControladorVendedores(AbstractControlador):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__tela_vendedores = TelaVendedores()
        self.__vendedores = []

    @property
    def vendedores(self) -> list[Vendedor]:
        return self.__vendedores

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastrar_vendedor,
            2: self.listar_vendedores,
            3: self.busca_vendedor,
            4: self.exclui_vendedor,
            5: self.editar_vendedor,
            99: self.adicionar_mock_vendedores,
            0: self.retornar
        }

        while True:
            opcao = self.__tela_vendedores.menu(list(lista_opcoes.keys()))
            lista_opcoes[opcao]()

    def cadastrar_vendedor(self) -> Vendedor | None:
        vendedor = self.__tela_vendedores.obter_dados_vendedor(self.gerar_proximo_codigo())
        vendedor_existente = self.pesquisa_vendedor(vendedor.cpf)

        # verifica se o vendedor já está cadastrado
        if vendedor_existente:
            self.__tela_vendedores.cpf_ja_cadastrado()
            return

        self.__vendedores.append(vendedor)
        self.__tela_vendedores.sucesso_cadastro()
        return vendedor

    def listar_vendedores(self) -> list[Vendedor]:
        if not self.__vendedores:
            self.__tela_vendedores.sem_cadastro()
        else:
            self.__tela_vendedores.exibir_vendedores(self.__vendedores)
        return self.__vendedores

    def busca_vendedor(self) -> Vendedor | None:
        cpf = self.__tela_vendedores.obter_cpf(Operacao.BUSCA)

        vendedor = self.pesquisa_vendedor(cpf)

        if vendedor:
            self.__tela_vendedores.exibir_vendedor(vendedor)
            return vendedor

        self.__tela_vendedores.cadastro_nao_encontrado()

    def editar_vendedor(self) -> Vendedor:
        cpf = self.__tela_vendedores.obter_cpf(Operacao.EDITA)
        vendedor = self.pesquisa_vendedor(cpf)

        if vendedor:
            vendedor_atualizado = self.__tela_vendedores.editar_dados_vendedor(vendedor)
            self.__vendedores[self.__vendedores.index(vendedor)] = vendedor_atualizado
            self.__tela_vendedores.sucesso_alteracao()
            self.__tela_vendedores.exibir_vendedor(vendedor_atualizado)
            return vendedor_atualizado

        self.__tela_vendedores.cadastro_nao_encontrado()

    def exclui_vendedor(self) -> Vendedor:
        cpf = self.__tela_vendedores.obter_cpf(Operacao.EXCLUI)
        vendedor = self.pesquisa_vendedor(cpf)

        if vendedor:
            self.__vendedores.remove(vendedor)
            self.__tela_vendedores.sucesso_exclusao(vendedor.nome)
            return vendedor

        self.__tela_vendedores.cadastro_nao_encontrado()

    def pesquisa_vendedor(self, cpf: str) -> Vendedor:
        for vendedor in self.__vendedores:
            if vendedor.cpf == cpf:
                return vendedor

    def gerar_proximo_codigo(self) -> int:
        if not self.__vendedores:
            return 1
        max_codigo = max(vendedores.codigo for vendedores in self.__vendedores)
        return max_codigo + 1

    def adicionar_mock_vendedores(self):
        self.__vendedores.extend(lista_vendedores_mock)
