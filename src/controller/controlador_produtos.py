from src.controller.abstract_controlador import AbstractControlador
from src.exceptions.nenhum_registro_encontrado_exception import NenhumRegistroEncontradoException
from src.mocks.produtos_mock import lista_produtos_mock
from src.model.produto import Produto
from src.utils.decorators import tratar_excecoes
from src.view.tela_produtos import TelaProduto


class ControladorProduto(AbstractControlador):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__produtos = []
        self.__tela_produto = TelaProduto()

    @property
    def produtos(self) -> list[Produto]:
        return self.__produtos

    @property
    def produtos_dict(self) -> list[dict]:
        if self.__produtos:
            lista_dados_produtos = []
            for produto in self.__produtos:
                lista_dados_produtos.append(produto.to_dict())
            return lista_dados_produtos
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
        dados_produto = self.__tela_produto.obter_dados_produto(self.gerar_proximo_codigo())
        produto_existente = self.pesquisa_produto(dados_produto['codigo'])

        if produto_existente:
            print("Produto já cadastrado")
            return

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
    def buscar_produto(self) -> Produto:
        codigo = self.__tela_produto.busca_produto()

        produto = self.pesquisa_produto(codigo)

        if produto:
            self.__tela_produto.exibir_produto(produto.to_dict())
            return produto

        self.__tela_produto.cadastro_nao_encontrado()

    @tratar_excecoes
    def editar_produto(self) -> Produto:
        codigo = self.__tela_produto.busca_produto()
        produto = self.pesquisa_produto(codigo)

        if produto:
            dados_produto_atualizado = self.__tela_produto.editar_dados_produto(produto.to_dict())
            produto_atualizado = Produto(**dados_produto_atualizado)
            self.__produtos[self.__produtos.index(produto)] = produto_atualizado
            self.__tela_produto.sucesso_alteracao()
            self.__tela_produto.exibir_produto(dados_produto_atualizado)
            return produto_atualizado

        self.__tela_produto.cadastro_nao_encontrado()

    @tratar_excecoes
    def excluir_produto(self) -> Produto:
        codigo = self.__tela_produto.busca_produto()
        produto = self.pesquisa_produto(codigo)

        if produto:
            self.__produtos.remove(produto)
            self.__tela_produto.sucesso_exclusao(produto.nome)
            return produto

        self.__tela_produto.cadastro_nao_encontrado()

    def pesquisa_produto(self, codigo: int) -> Produto:
        for produto in self.__produtos:
            if produto.codigo == codigo:
                return produto

    def gerar_proximo_codigo(self) -> int:
        if not self.__produtos:
            return 1
        max_codigo = max(produtos.codigo for produtos in self.__produtos)
        return max_codigo + 1

    def adicionar_mock_produtos(self):
        self.__produtos.extend(lista_produtos_mock)
