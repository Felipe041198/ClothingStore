from src.controller.controlador_clientes import ControladorClientes
from src.controller.controlador_vendas import ControladorVendas
from src.view.tela_sistema import TelaSistema
from src.controller.controlador_vendedores import ControladorVendedores


class ControladorSistema:

    def __init__(self):
        self.__controlador_clientes = ControladorClientes(self)
        self.__controlador_vendedores = ControladorVendedores(self)
        self.__controlador_produtos = None
        self.__controlador_vendas = ControladorVendas(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_clientes(self):
        return self.__controlador_clientes

    @property
    def controlador_vendedores(self):
        return self.__controlador_vendedores

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_clientes(self):
        self.__controlador_clientes.abre_tela()

    def cadastra_vendedores(self):
        self.__controlador_vendedores.abre_tela()

    def registra_venda(self):
        self.__controlador_vendas.abre_tela()

    @staticmethod
    def encerra_sistema():
        exit(0)

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastra_clientes,
            2: self.cadastra_vendedores,
            4: self.registra_venda,
            0: self.encerra_sistema
        }

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes(list(lista_opcoes.keys()))
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
