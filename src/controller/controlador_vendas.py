from src.controller.abstract_controlador import AbstractControlador
from src.mocks.pedidos_mock import lista_vendas_mock
from src.exceptions.nenhum_registro_encontrado_exception import NenhumRegistroEncontradoException
from src.model.venda import Venda
from src.utils.decorators import tratar_excecoes
from src.view.tela_vendas import TelaVendas
from src.mocks.venda_mock import lista_vendas_mock


class ControladorVendas(AbstractControlador):

    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__tela_venda = TelaVendas()
        self.__vendas = []

    def abre_tela(self):
        lista_opcoes = {
            1: self.realizar_venda,
            2: self.listar_vendas,
            4: self.excluir_venda,
            99: self.adiciona_mock_vendas,
            0: self.retornar
        }

        while True:
            lista_opcoes[self.__tela_venda.menu(list(lista_opcoes.keys()))]()

    @tratar_excecoes
    def realizar_venda(self) -> Venda:
        clientes = self._controlador_sistema.controlador_clientes.clientes
        vendedores = self._controlador_sistema.controlador_vendedores.vendedores
        produtos = self._controlador_sistema.controlador_produtos.produtos
        venda = self.__tela_venda.obter_dados_venda(clientes, vendedores, produtos)
        self.__vendas.append(venda)
        self.__tela_venda.sucesso_cadastro()
        return venda

    @tratar_excecoes
    def listar_vendas(self) -> list[Venda]:
        if self.__vendas:
            self.__tela_venda.exibir_vendas(self.__vendas)
            return self.__vendas
        raise NenhumRegistroEncontradoException

    def excluir_venda(self):
        venda = self.__tela_venda.seleciona_vendas(self.__vendas)

        self.__vendas.remove(venda)
        self.__tela_venda.sucesso_exclusao()

    def mostrar_erro(self, e: str):
        self.__tela_venda.mostrar_erro(e)

    def adiciona_mock_vendas(self):
        self.__vendas.extend(lista_vendas_mock)
