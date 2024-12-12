from src.controller.abstract_controlador import AbstractControlador
from src.exceptions.nenhum_registro_encontrado_exception import NenhumRegistroEncontradoException
from src.mocks.produtos_mock import lista_produtos_mock
from src.model.produto import Produto
from src.utils.decorators import tratar_excecoes
from src.view.tela_gui_produtos import TelaProdutos


class ControladorProduto(AbstractControlador):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__produtos = []
        self.__tela_produto = TelaProdutos()

    @property
    def produtos(self) -> list[Produto]:
        return self.__produtos

    @property
    def produtos_dict(self) -> list[dict]:
        if self.__produtos:
            return [produto.to_dict() for produto in self.__produtos]
        raise NenhumRegistroEncontradoException

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastrar_produto,
            2: self.listar_produtos,
            3: self.buscar_produto,
            4: self.excluir_produto,
            5: self.editar_produto,
            99: self.adicionar_mock_produtos,
            0: self.retornar
        }

        while True:
            opcao = self.__tela_produto.menu(list(lista_opcoes.keys()))
            lista_opcoes[opcao]()

    @tratar_excecoes
    def cadastrar_produto(self) -> Produto | None:
        dados_produto, should_exit_to_menu = self.__tela_produto.obter_dados_produto(
            self.gerar_proximo_codigo())

        if should_exit_to_menu or not dados_produto:
            return None

        produto_existente = self.pesquisa_produto(dados_produto["codigo"])
        if produto_existente:
            self.__tela_produto.mostrar_erro("Produto já cadastrado com esse código.")
            return None

        produto = Produto(**dados_produto)
        self.__produtos.append(produto)

        self.__tela_produto.sucesso_cadastro()
        self.__tela_produto.exibir_produto(dados_produto)
        return produto

    @tratar_excecoes
    def listar_produtos(self) -> list[Produto]:
        if not self.__produtos:
            self.__tela_produto.sem_cadastro()
        else:
            self.__tela_produto.exibir_lista_produtos(self.produtos_dict)
        return self.__produtos

    @tratar_excecoes
    def buscar_produto(self) -> Produto | None:
        codigo = self.__tela_produto.busca_produto()

        if codigo is None:
            return None

        produto = self.pesquisa_produto(codigo)

        if produto:
            self.__tela_produto.exibir_produto(produto.to_dict())
            return produto

        self.__tela_produto.cadastro_nao_encontrado()

    @tratar_excecoes
    def editar_produto(self) -> Produto | None:
        codigo = self.__tela_produto.busca_produto()
        if codigo is None:
            return None
        produto = self.pesquisa_produto(codigo)

        if produto:
            dados_produto = produto.to_dict()
            dados_normalizados = {
                'nome': str(dados_produto.get('nome', '')).strip(),
                'descricao': str(dados_produto.get('descricao', '')).strip(),
                'preco': float(dados_produto.get('preco', 0.0)),
                'tamanho': str(dados_produto.get('tamanho', '')).strip(),
                'cor': str(dados_produto.get('cor', '')).strip(),
                'codigo': dados_produto.get('codigo', 0),
            }

            dados_produto_atualizado, should_exit_to_menu = self.__tela_produto.editar_dados_produto(
                dados_normalizados)

            if should_exit_to_menu or not dados_produto_atualizado:
                return None

            produto_atualizado = Produto(**dados_produto_atualizado)
            self.__produtos[self.__produtos.index(produto)] = produto_atualizado

            self.__tela_produto.sucesso_alteracao()
            self.__tela_produto.exibir_produto(dados_produto_atualizado)
            return produto_atualizado

        self.__tela_produto.cadastro_nao_encontrado()

    @tratar_excecoes
    def excluir_produto(self) -> Produto | None:
        codigo = self.__tela_produto.busca_produto()
        if codigo is None:
            return None
        produto = self.pesquisa_produto(codigo)

        if produto:
            self.__produtos.remove(produto)
            self.__tela_produto.sucesso_exclusao(produto.nome)
            return produto

        self.__tela_produto.cadastro_nao_encontrado()

    def mostrar_erro(self, mensagem: str):
        self.__tela_produto.mostrar_erro(mensagem)

    def pesquisa_produto(self, codigo: int) -> Produto | None:
        for produto in self.__produtos:
            if produto.codigo == codigo:
                return produto
        return None

    def gerar_proximo_codigo(self) -> int:
        if not self.__produtos:
            return 1
        max_codigo = max(produto.codigo for produto in self.__produtos)
        return max_codigo + 1

    def adicionar_mock_produtos(self):
        self.__produtos.extend(lista_produtos_mock)
