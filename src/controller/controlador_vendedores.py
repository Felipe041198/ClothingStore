from src.controller.abstract_controlador import AbstractControlador
from src.dao.dao_generic import DAOGeneric
from src.exceptions.cpf_ja_cadastrado_exception import CpfJahCadastradoException
from src.exceptions.cpf_nao_encontrado_exception import CpfNaoEncontradoException
from src.exceptions.nenhum_registro_encontrado_exception import NenhumRegistroEncontradoException
from src.exceptions.valor_invalido_exception import ValorInvalidoException
from src.mocks.vendedores_mock import lista_vendedores_mock
from src.model.vendedor import Vendedor
from src.utils.decorators import tratar_excecoes
from src.utils.enum_operacoes import Operacao
from src.view.tela_gui_vendedores import TelaVendedores


class ControladorVendedores(AbstractControlador):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__tela_vendedores = TelaVendedores()
        self.__vendedores_dao = DAOGeneric("vendedores")
        self.__vendedores = self.__vendedores_dao.carregar()

    @property
    def vendedores(self) -> list[Vendedor]:
        return self.__vendedores

    @property
    def vendedores_dict(self) -> list[dict]:
        if self.__vendedores:
            lista_vendedores = []
            for vendedor in self.__vendedores:
                lista_vendedores.append(vendedor.to_dict())
            return lista_vendedores
        raise NenhumRegistroEncontradoException

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

    @tratar_excecoes
    def cadastrar_vendedor(self) -> Vendedor | None:
        dados_vendedor, should_exit_to_menu = self.__tela_vendedores.obter_dados_vendedor(
            self.gerar_proximo_codigo(),
        )

        if should_exit_to_menu or not dados_vendedor:
            return None

        salario = self.validar_salario(dados_vendedor["salario"])
        dados_vendedor["salario"] = salario

        cpf_existente = self.pesquisa_vendedor(dados_vendedor["cpf"])
        if cpf_existente:
            self.__tela_vendedores.mostrar_erro("CPF já cadastrado. Insira um CPF diferente.")
            return None

        vendedor = Vendedor(**dados_vendedor)
        self.__vendedores.append(vendedor)

        self.__tela_vendedores.sucesso_cadastro()
        self.__tela_vendedores.exibir_vendedor(dados_vendedor)
        return vendedor

    @tratar_excecoes
    def listar_vendedores(self) -> list[Vendedor]:
        if not self.__vendedores:
            self.__tela_vendedores.sem_cadastro()
        else:
            self.__tela_vendedores.exibir_vendedores(self.vendedores_dict)
        return self.__vendedores

    @tratar_excecoes
    def busca_vendedor(self) -> Vendedor | None:
        cpf = self.__tela_vendedores.obter_cpf(Operacao.BUSCA)

        if not cpf:
            return None

        vendedor = self.pesquisa_vendedor(cpf)

        if vendedor:
            self.__tela_vendedores.exibir_vendedor(vendedor.to_dict())
            return vendedor

        raise CpfNaoEncontradoException

    @tratar_excecoes
    def editar_vendedor(self) -> Vendedor | None:
        cpf = self.__tela_vendedores.obter_cpf(Operacao.EDITA)
        if not cpf:
            return None

        vendedor = self.pesquisa_vendedor(cpf)

        if vendedor:
            dados_vendedor_original = vendedor.to_dict()
            dados_vendedor_atualizado, should_exit_to_menu = self.__tela_vendedores.editar_dados_vendedor(
                dados_vendedor_original)

            if should_exit_to_menu or not dados_vendedor_atualizado:
                return None

            if dados_vendedor_original == dados_vendedor_atualizado:
                return None

            salario = self.validar_salario(dados_vendedor_atualizado["salario"])
            dados_vendedor_atualizado["salario"] = salario

            vendedor_atualizado = Vendedor(**dados_vendedor_atualizado)
            self.__vendedores[self.__vendedores.index(vendedor)] = vendedor_atualizado

            self.__tela_vendedores.sucesso_alteracao()
            self.__tela_vendedores.exibir_vendedor(dados_vendedor_atualizado)
            return vendedor_atualizado

        self.__tela_vendedores.cadastro_nao_encontrado()

    @tratar_excecoes
    def exclui_vendedor(self) -> Vendedor | None:
        cpf = self.__tela_vendedores.obter_cpf(Operacao.EXCLUI)
        if not cpf:
            return None
        vendedor = self.pesquisa_vendedor(cpf)

        if vendedor:
            self.__vendedores.remove(vendedor)
            self.__tela_vendedores.sucesso_exclusao(vendedor.nome)
            return vendedor

        self.__tela_vendedores.cadastro_nao_encontrado()

    def pesquisa_vendedor(self, cpf: str) -> Vendedor | None:
        for vendedor in self.__vendedores:
            if vendedor.cpf == cpf:
                return vendedor
        return None

    @staticmethod
    def validar_salario(salario: str) -> float:
        try:
            valor = float(salario)
            if valor <= 0:
                raise ValorInvalidoException("O salário deve ser um número positivo.")
            return valor
        except ValueError:
            raise ValorInvalidoException("O salário fornecido é inválido. Insira um número.")

    def gerar_proximo_codigo(self) -> int:
        if not self.__vendedores:
            return 1
        max_codigo = max(vendedores.codigo for vendedores in self.__vendedores)
        return max_codigo + 1

    def adicionar_mock_vendedores(self):
        self.__vendedores.extend(lista_vendedores_mock)

    def mostrar_erro(self, e: str):
        self.__tela_vendedores.mostrar_erro(e)

    def salvar_vendedores(self):
        self.__vendedores_dao.salvar(self.__vendedores)
