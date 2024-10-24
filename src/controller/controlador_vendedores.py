from src.controller.abstract_controlador_vendedores import AbstractControladorVendedores
from src.view.tela_vendedores import TelaVendedores


class ControladorVendedores(AbstractControladorVendedores):
    def __init__(self):
        self.__tela_vendedores = TelaVendedores()
        self.__vendedores = []

    def menu_vendedores(self):
        while True:
            opcao = self.__tela_vendedores.menu()
            if opcao == '1':
                self.cadastrar_vendedor()
            elif opcao == '2':
                self.listar_vendedores()
            elif opcao == '3':
                self.busca_vendedor()
            elif opcao == '4':
                self.editar_vendedor()
            elif opcao == '5':
                self.exclui_vendedor()
            elif opcao == '0':
                break
            else:
                self.__tela_vendedores.opcao_invalida()

    def cadastrar_vendedor(self):
        while True:
            try:
                vendedor = self.__tela_vendedores.obter_dados_vendedor()

                # verifica se o vendedor já está cadastrado
                vendedor_existente = self.busca_vendedor(vendedor.cpf)
                if vendedor_existente:
                    self.__tela_vendedores.cpf_ja_cadastrado()
                    return 
                self.__vendedores.append(vendedor)
                self.__tela_vendedores.sucesso_cadastro()
                self.__tela_vendedores.exibir_vendedor(vendedor)
                break
            except ValueError as e:
                print(f"Erro ao cadastrar vendedor: {e}. Tente novamente.")

    def listar_vendedores(self):
        if not self.__vendedores:
            self.__tela_vendedores.sem_vendedores()
        else:
            self.__tela_vendedores.exibir_vendedores(self.__vendedores)

    def busca_vendedor(self, cpf: int = None):
        if cpf is None:
            cpf = self.__tela_vendedores.obter_cpf()
        for vendedor in self.__vendedores:
            if vendedor.cpf == cpf:
                self.__tela_vendedores.exibir_vendedor(vendedor)
                return vendedor
        self.__tela_vendedores.vendedor_nao_encontrado()
        return None

    def editar_vendedor(self):
        cpf = self.__tela_vendedores.obter_cpf()
        vendedor_encontrado = False

        for i, vendedor in enumerate(self.__vendedores):
            if vendedor.cpf == cpf:
                vendedor_atualizado = self.__tela_vendedores.editar_dados_vendedor(vendedor)
                self.__vendedores[i] = vendedor_atualizado
                self.__tela_vendedores.sucesso_alteracao()
                vendedor_encontrado = True
                break

        if not vendedor_encontrado:
            self.__tela_vendedores.vendedor_nao_encontrado()

    def exclui_vendedor(self):
        cpf = self.__tela_vendedores.obter_cpf()
        tem_vendedor = False
        for vendedor in self.__vendedores:
            if vendedor.cpf == cpf:
                self.__vendedores.remove(vendedor)
                self.__tela_vendedores.sucesso_exclusao(vendedor.nome)
                tem_vendedor = True
                break
        if not tem_vendedor:
            self.__tela_vendedores.vendedor_nao_encontrado()
