from src.controller.abstract_controlador_clientes import AbstractControladorClientes
from src.utils.enum_operacoes import Operacao
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
                self.busca_cliente()
            elif opcao == '4':
                self.exclui_cliente()
            elif opcao == '5':
                self.editar_cliente()
            elif opcao == '0':
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

    def busca_cliente(self):
        cpf = self.__tela_clientes.obter_cpf(Operacao.BUSCA)
        self.lista_cliente(cpf)

    def lista_cliente(self, cpf: int):
        tem_cliente = False
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                self.__tela_clientes.exibir_cliente(cliente)
                tem_cliente = True
                break
        if not tem_cliente:
            self.__tela_clientes.cliente_nao_encontrado()

    def exclui_cliente(self):
        cpf = self.__tela_clientes.obter_cpf(Operacao.EXCLUI)
        tem_cliente = False
        for cliente in self.__clientes:
            if cliente.cpf == cpf:
                self.__clientes.remove(cliente)
                self.__tela_clientes.sucesso_exclusao(cliente.nome)
                tem_cliente = True
                break
        if not tem_cliente:
            self.__tela_clientes.cliente_nao_encontrado()

    def editar_cliente(self):
        cpf = self.__tela_clientes.obter_cpf(Operacao.EDITA)
        cliente_encontrado = False

        for i, cliente in enumerate(self.__clientes):
            if cliente.cpf == cpf:
                cliente_atualizado = self.__tela_clientes.editar_dados_cliente(cliente)
                self.__clientes[i] = cliente_atualizado  # Substitui o cliente na lista
                self.__tela_clientes.sucesso_alteracao()
                cliente_encontrado = True
                break

        if not cliente_encontrado:
            self.__tela_clientes.cliente_nao_encontrado()
