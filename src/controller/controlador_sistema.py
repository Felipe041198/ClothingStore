from src.controller.controlador_clientes import ControladorClientes
from src.view.tela_sistema import TelaSistema


class ControladorSistema:

    def __init__(self):
        self.__controlador_clientes = ControladorClientes(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_clientes(self):
        return self.__controlador_clientes

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_clientes(self):
        self.__controlador_clientes.abre_tela()

    @staticmethod
    def encerra_sistema():
        exit(0)

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastra_clientes,
            0: self.encerra_sistema
        }

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes(list(lista_opcoes.keys()))
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
