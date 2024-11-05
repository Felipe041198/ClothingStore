from src.controller.abstract_controlador import AbstractControlador
from src.model.venda import Venda
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
            2: self.lista_vendas,
            3: self.buscar_venda,
            4: self.excluir_venda,
            99: self.mock_venda,
            0: self.retornar
        }

        while True:
            lista_opcoes[self.__tela_venda.menu(list(lista_opcoes.keys()))]()

    def mock_venda(self):
        self.__vendas.extend(lista_vendas_mock)

    def realizar_venda(self) -> Venda:
        clientes = self._controlador_sistema.controlador_clientes.clientes
        vendedores = self._controlador_sistema.controlador_vendedores.vendedores
        produtos = self._controlador_sistema.controlador_produtos.produtos
        venda = self.__tela_venda.obter_dados_venda(clientes, vendedores, produtos)
        self.__vendas.append(venda)
        self.__tela_venda.sucesso_cadastro()
        return venda

    def listar_vendas(self) -> list[Venda]:
        return self.__vendas

    def lista_vendas(self):
        if not self.__vendas:
            self.__tela_venda.sem_cadastro()
        else:
            self.__tela_venda.exibir_vendas(self.__vendas)

    def buscar_venda(self):
        pass

    def excluir_venda(self):
        venda = self.__tela_venda.seleciona_vendas(self.__vendas)

        self.__vendas.remove(venda)
        self.__tela_venda.sucesso_exclusao()
