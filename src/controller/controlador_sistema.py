import atexit

from src.controller.controlador_clientes import ControladorClientes
from src.controller.controlador_vendas import ControladorVendas
from src.controller.controlador_produtos import ControladorProduto
from src.view.tela_gui_sistema import TelaSistema
from src.controller.controlador_vendedores import ControladorVendedores
from src.controller.controlador_relatorio import ControladorRelatorio


class ControladorSistema:

    def __init__(self):
        self.__controlador_clientes = ControladorClientes(self)
        self.__controlador_vendedores = ControladorVendedores(self)
        self.__controlador_produtos = ControladorProduto(self)
        self.__controlador_vendas = ControladorVendas(self)
        self.__controlador_relatorio = ControladorRelatorio(self)
        self.__tela_sistema = TelaSistema()
        # Registra uma função para toda vez que fechar o sistema, salvar todos os dados
        atexit.register(self.salvar_todos_os_dados)

    @property
    def controlador_clientes(self) -> ControladorClientes:
        return self.__controlador_clientes

    @property
    def controlador_vendedores(self) -> ControladorVendedores:
        return self.__controlador_vendedores

    @property
    def controlador_produtos(self) -> ControladorProduto:
        return self.__controlador_produtos

    @property
    def controlador_vendas(self) -> ControladorVendas:
        return self.__controlador_vendas

    @property
    def controlador_relatorio(self) -> ControladorRelatorio:
        return self.__controlador_relatorio

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_clientes(self):
        self.__controlador_clientes.abre_tela()

    def cadastra_vendedores(self):
        self.__controlador_vendedores.abre_tela()

    def cadastra_produtos(self):
        self.__controlador_produtos.abre_tela()

    def registra_venda(self):
        self.__controlador_vendas.abre_tela()

    def exibe_relatorio(self):
        self.__controlador_relatorio.abre_tela()

    @staticmethod
    def encerra_sistema():
        exit(0)

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastra_clientes,
            2: self.cadastra_vendedores,
            3: self.cadastra_produtos,
            4: self.registra_venda,
            5: self.exibe_relatorio,
            0: self.encerra_sistema
        }

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes(list(lista_opcoes.keys()))
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def salvar_todos_os_dados(self):
        self.__controlador_clientes.salvar_clientes()
        self.__controlador_vendedores.salvar_vendedores()
        self.__controlador_produtos.salvar_produtos()
        self.__controlador_vendas.salvar_vendas()
