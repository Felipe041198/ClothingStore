from src.controller.abstract_controlador import AbstractControlador
from src.model.vendedor import Vendedor
from src.utils.enum_operacoes import Operacao
from src.view.tela_vendedores import TelaVendedores


class ControladorVendedores(AbstractControlador):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__tela_vendedores = TelaVendedores()
        self.__vendedores = []

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastrar_vendedor,
            2: self.listar_vendedores,
            3: self.busca_vendedor,
            4: self.exclui_vendedor,
            5: self.editar_vendedor,
            99: self.adicionar_mock_vendedores,
            0: self.retornar
        }

        while True:
            opcao = self.__tela_vendedores.menu(list(lista_opcoes.keys()))
            lista_opcoes[opcao]()

    def cadastrar_vendedor(self):
        vendedor = self.__tela_vendedores.obter_dados_vendedor()
        vendedor_existente = self.busca_vendedor(vendedor.cpf)

        # verifica se o vendedor já está cadastrado
        if vendedor_existente:
            self.__tela_vendedores.cpf_ja_cadastrado()
            return
        self.__vendedores.append(vendedor)
        self.__tela_vendedores.sucesso_cadastro()
        self.__tela_vendedores.exibir_vendedor(vendedor)
        return vendedor

    def listar_vendedores(self):
        if not self.__vendedores:
            self.__tela_vendedores.sem_cadastro()
        else:
            self.__tela_vendedores.exibir_vendedores(self.__vendedores)
        return self.__vendedores

    def busca_vendedor(self, cpf=None):
        if cpf is None:
            cpf = self.__tela_vendedores.obter_cpf(Operacao.BUSCA)

        for vendedor in self.__vendedores:
            if vendedor.cpf == cpf:
                self.__tela_vendedores.exibir_vendedor(vendedor)
                return vendedor

        self.__tela_vendedores.cadastro_nao_encontrado()
        return None

    def editar_vendedor(self):
        cpf = self.__tela_vendedores.obter_cpf(Operacao.EDITA)
        vendedor = self.busca_vendedor(cpf)

        if vendedor:
            vendedor_atualizado = self.__tela_vendedores.editar_dados_vendedor(vendedor)
            self.__vendedores[self.__vendedores.index(vendedor)] = vendedor_atualizado
            self.__tela_vendedores.sucesso_alteracao()
            self.__tela_vendedores.exibir_vendedor(vendedor_atualizado)
        else:
            self.__tela_vendedores.cadastro_nao_encontrado()

    def exclui_vendedor(self):
        cpf = self.__tela_vendedores.obter_cpf(Operacao.EXCLUI)
        vendedor = self.busca_vendedor(cpf)

        if vendedor:
            self.__vendedores.remove(vendedor)
            self.__tela_vendedores.sucesso_exclusao(vendedor.nome)
        else:
            self.__tela_vendedores.cadastro_nao_encontrado()

    def adicionar_mock_vendedores(self):
        vendedores = {
            Vendedor(1146, "Iris Souza", "28/01/2002", 1, 1400),
            Vendedor(1111, "Vendedor teste 1", "01/01/1999", 1, 1000),
            Vendedor(1222, "Vendedor teste 2", "02/02/2002", 2, 200),
            Vendedor(1333, "Vendedor teste 3", "03/03/2003", 2, 8145),
        }
        for vendedor in vendedores:
            self.__vendedores.append(vendedor)
