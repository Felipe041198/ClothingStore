from src.controller.abstract_controlador_clientes import AbstractControladorClientes
from src.view.tela_clientes import TelaClientes


class ControladorClientes(AbstractControladorClientes):
    def __init__(self):
        self.__tela_clientes = TelaClientes()
        self.__clientes = []

    def menu_clientes(self):
        while True:
            opcao = self.__tela_clientes.menu()
            if opcao == '1':
                self.cadastrar_cliente()
            elif opcao == '2':
                self.listar_clientes()
            elif opcao == '3':
                break
            else:
                self.__tela_clientes.opcao_invalida()

    def cadastrar_cliente(self):
        cliente = self.__tela_clientes.obter_dados_cliente()
        self.__clientes.append(cliente)
        self.__tela_clientes.sucesso_cadastro()

    def listar_clientes(self):
        if not self.__clientes:
            self.__tela_clientes.sem_clientes()
        else:
            self.__tela_clientes.exibir_clientes(self.__clientes)
