from src.controller.abstract_controlador_cadastro import AbstractControlador
from src.utils.enum_operacoes import Operacao
from src.view.tela_clientes import TelaClientes


class ControladorClientes(AbstractControlador):

    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__tela_clientes = TelaClientes()
        self.__clientes = []

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastrar_cliente,
            2: self.listar_clientes,
            3: self.busca_cliente,
            4: self.exclui_cliente,
            5: self.editar_cliente,
            0: self.retornar
        }

        while True:
            try: 
                lista_opcoes[self.__tela_clientes.menu(list(lista_opcoes.keys()))]()
            except KeyError:
                print("Opção inválida. Tente novamente.")
            except Exception as e:
                print(f"Ocorreu um erro: {e}")

    def cadastrar_cliente(self):
        try:
            cliente = self.__tela_clientes.obter_dados_cliente()
            cliente_existente = self.busca_cliente(cliente.cpf)
            if cliente_existente:
                self.__tela_clientes.cpf_ja_cadastrado()
                return
            self.__clientes.append(cliente)
            self.__tela_clientes.sucesso_cadastro()
            self.__tela_clientes.exibir_cliente(cliente)
        except  ValueError as e:
            print(f"Erro ao cadastrar cliente: {e}. Tente novamente.")

    def listar_clientes(self):
        try:
            if not self.__clientes:
                self.__tela_clientes.sem_cadastro()
            else:
                self.__tela_clientes.exibir_clientes(self.__clientes)
        except Exception as e:
            print(f"Ocorreu um erro inesperado ao cadastrar o cliente: {e}")

    def busca_cliente(self, cpf = None):
        try:
            if cpf is None:
                cpf = self.__tela_clientes.obter_cpf(Operacao.BUSCA)
            
            for cliente in self.__clientes:
                if cliente.cpf == cpf:
                    self.__tela_clientes.exibir_cliente(cliente)
                    return cliente
            
            self.__tela_clientes.cadastro_nao_encontrado()
            return None
        except Exception as e:
            print(f"Erro ao buscar cliente: {e}")

    def exclui_cliente(self):
        try:
            cpf = self.__tela_clientes.obter_cpf(Operacao.EXCLUI)
            cliente = self.busca_cliente(cpf)

            if cliente:
                self.__clientes.remove(cliente)
                self.__tela_clientes.sucesso_exclusao(cliente.nome)
            else:
                self.__tela_clientes.cadastro_nao_encontrado()
        except Exception as e:
            print(f"Erro ao excluir perfil do cliente: {e}")

    def editar_cliente(self):
        try:
            cpf = self.__tela_clientes.obter_cpf(Operacao.EDITA)
            cliente = self.busca_cliente(cpf)

            if cliente:
                cliente_atualizado = self.__tela_clientes.editar_dados_cliente(cliente)
                self.__clientes[self.__clientes.index(cliente)] = cliente_atualizado
                self.__tela_clientes.sucesso_alteracao()
                self.__tela_clientes.exibir_cliente(cliente_atualizado)
            else:
                self.__tela_clientes.cadastro_nao_encontrado()
        except Exception as e:
            print(f"Erro ao editar perfil do cliente: {e}")
