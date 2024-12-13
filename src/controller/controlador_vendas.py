from src.controller.abstract_controlador import AbstractControlador
from src.dao.dao_generic import DAOGeneric
from src.mocks.pedidos_mock import lista_vendas_mock
from src.exceptions.nenhum_registro_encontrado_exception import NenhumRegistroEncontradoException
from src.model.cliente import Cliente
from src.model.venda import Venda
from src.model.vendedor import Vendedor
from src.utils.decorators import tratar_excecoes
from src.view.tela_gui_vendas import TelaVendas


class ControladorVendas(AbstractControlador):

    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__tela_venda = TelaVendas()
        self.__vendas_dao = DAOGeneric("vendas")
        self.__vendas = self.__vendas_dao.carregar()

    @property
    def vendas(self) -> list[Venda]:
        return self.__vendas

    @property
    def vendas_dict(self) -> list[dict]:
        lista_vendas = []
        for venda in self.__vendas:
            lista_vendas.append(venda.to_dict())
        return lista_vendas

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
        clientes = self._controlador_sistema.controlador_clientes.clientes_dict
        vendedores = self._controlador_sistema.controlador_vendedores.vendedores_dict
        produtos = self._controlador_sistema.controlador_produtos.produtos_dict
        dados_venda = self.__tela_venda.obter_dados_venda(clientes, vendedores, produtos)
        venda = Venda(
            cliente=Cliente(**dados_venda['cliente']),
            vendedor=Vendedor(**dados_venda['vendedor']),
        )
        venda.adiciona_items(dados_venda["produtos"])
        self.__vendas.append(venda)
        self.__tela_venda.sucesso_cadastro()
        return venda

    @tratar_excecoes
    def listar_vendas(self) -> list[Venda]:
        if self.__vendas:
            self.__tela_venda.exibir_vendas(self.vendas_dict)
            return self.__vendas
        raise NenhumRegistroEncontradoException

    def excluir_venda(self):
        if not self.__vendas:
            self.__tela_venda.sem_cadastro()
            return
        indice_venda = self.__tela_venda.seleciona_vendas(self.vendas_dict)
        if indice_venda is None:
            return

        self.__vendas.pop(indice_venda)
        self.__tela_venda.sucesso_exclusao()

    def mostrar_erro(self, e: str):
        self.__tela_venda.mostrar_erro(e)

    def adiciona_mock_vendas(self):
        self.__vendas.extend(lista_vendas_mock)

    def salvar_vendas(self):
        self.__vendas_dao.salvar(self.__vendas)
