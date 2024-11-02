from src.controller.abstract_controlador import AbstractControlador
from src.view.tela_vendas import TelaVendas


class ControladorVendas(AbstractControlador):

    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__tela_venda = TelaVendas()
        self.__vendas = []

    def abre_tela(self):
        lista_opcoes = {
            1: self.realizar_venda,
            2: self.listar_vendas,
            3: self.buscar_venda,
            4: self.excluir_venda,
            0: self.retornar
        }

        while True:
            lista_opcoes[self.__tela_venda.menu(list(lista_opcoes.keys()))]()

    def realizar_venda(self):
        clientes = self._controlador_sistema.controlador_clientes.clientes
        vendedores = self._controlador_sistema.controlador_vendedores.vendedores
        produtos = self._controlador_sistema.controlador_produtos.produtos
        venda = self.__tela_venda.obter_dados_venda(clientes, vendedores, produtos)
        self.__vendas.append(venda)
        self.__tela_venda.sucesso_venda()

    def listar_vendas(self):
        pass

    def buscar_venda(self):
        pass

    def excluir_venda(self):
        pass
