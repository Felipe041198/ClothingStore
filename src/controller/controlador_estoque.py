from src.controller.abstract_controlador import AbstractControlador
from src.model.movimentacao import TipoMovimentacao
from src.view.tela_estoque import TelaEstoque


class ControladorEstoque(AbstractControlador):
    def __init__(self, controlador_sistema) -> None:
        super().__init__(controlador_sistema)
        self.__tela_estoque = TelaEstoque()
        self.__movimentacoes = []

    @property
    def movimentacoes(self) -> list[TipoMovimentacao]:
        return self.__movimentacoes

    def abre_tela(self):
        lista_opcoes = {
            1: self.adicionar_estoque_por_codigo,
            2: self.adicionar_estoque_por_lista,
            3: self.remover_estoque,
            4: self.exclui_cliente,
            5: self.editar_cliente,
            99: self.adicionar_mock_clientes,
            0: self.retornar
        }

        while True:
            lista_opcoes[self.__tela_estoque.menu(list(lista_opcoes.keys()))]()
