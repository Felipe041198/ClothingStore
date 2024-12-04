import unittest
from unittest import TestCase
from unittest.mock import patch

from src.controller.controlador_produtos import ControladorProduto
from src.controller.controlador_sistema import ControladorSistema
from src.mocks.produtos_mock import produto1, produto2
from src.model.produto import Produto


class TestControladorProduto(TestCase):
    def setUp(self):
        self.controlador_sistema = ControladorSistema()
        self.controlador = ControladorProduto(self.controlador_sistema)

    @patch('src.view.tela_produtos.TelaProduto.sucesso_cadastro')
    @patch('src.view.tela_produtos.TelaProduto.obter_dados_produto')
    def test_cadastrar_produto(self, mock_obter_dados_produto, mock_sucesso_cadastro):
        # Mockando a função obter_dados_produto para retornar um produto
        mock_obter_dados_produto.return_value = produto1.to_dict()

        resultado = self.controlador.cadastrar_produto()

        mock_sucesso_cadastro.assert_called_once()
        self.assertIn(resultado, self.controlador.produtos)
        self.assertEqual(len(self.controlador.produtos), 1)
        self.compara_produtos(resultado, produto1)

    @patch('src.view.tela_produtos.TelaProduto.exibir_lista_produtos')
    def test_listar_produtos(self, mock_exibir_lista_produtos):
        self.controlador.produtos.append(produto1)
        self.controlador.produtos.append(produto2)

        resultado = self.controlador.listar_produtos()

        mock_exibir_lista_produtos.assert_called_once()
        self.assertEqual(len(resultado), 2)

    @patch('src.view.tela_produtos.TelaProduto.sem_cadastro')
    def test_listar_produtos_vazio(self, mock_sem_cadastro):
        resultado = self.controlador.listar_produtos()

        mock_sem_cadastro.assert_called_once()
        self.assertEqual(len(resultado), 0)

    @patch('src.view.tela_produtos.TelaProduto.busca_produto')
    @patch('src.view.tela_produtos.TelaProduto.exibir_produto')
    def test_buscar_produto(self, mock_exibir_produto, mock_busca_produto):
        self.controlador.produtos.append(produto1)
        mock_busca_produto.return_value = produto1.codigo

        resultado = self.controlador.buscar_produto()

        mock_exibir_produto.assert_called_once_with(produto1.to_dict())
        self.assertEqual(resultado, produto1)

    @patch('src.view.tela_produtos.TelaProduto.busca_produto')
    @patch('src.view.tela_produtos.TelaProduto.cadastro_nao_encontrado')
    def test_buscar_produto_nao_encontrado(self, mock_cadastro_nao_encontrado, mock_busca_produto):
        mock_busca_produto.return_value = produto1.codigo

        resultado = self.controlador.buscar_produto()

        mock_cadastro_nao_encontrado.assert_called_once()
        self.assertIsNone(resultado)

    @patch('src.view.tela_produtos.TelaProduto.busca_produto')
    @patch('src.view.tela_produtos.TelaProduto.sucesso_exclusao')
    def test_exclui_produto(self, mock_sucesso_exclusao, mock_busca_produto):
        self.controlador.produtos.append(produto1)
        mock_busca_produto.return_value = produto1.codigo

        resultado = self.controlador.excluir_produto()

        self.assertEqual(len(self.controlador.produtos), 0)
        mock_sucesso_exclusao.assert_called_once_with(produto1.nome)
        self.compara_produtos(resultado, produto1)

    @patch('src.view.tela_produtos.TelaProduto.busca_produto')
    @patch('src.view.tela_produtos.TelaProduto.cadastro_nao_encontrado')
    def test_excluir_produto_nao_encontrado(self, mock_busca_produto, mock_cadastro_nao_encontrado):
        mock_busca_produto.return_value = produto1.codigo

        resultado = self.controlador.excluir_produto()

        mock_cadastro_nao_encontrado.assert_called_once()
        self.assertIsNone(resultado)

    # Função auxiliar para comparar produtos
    def compara_produtos(self, produto1: Produto, produto2: Produto):
        self.assertEqual(produto1.codigo, produto2.codigo)
        self.assertEqual(produto1.nome, produto2.nome)
        self.assertEqual(produto1.descricao, produto2.descricao)
        self.assertEqual(produto1.tamanho, produto2.tamanho)
        self.assertEqual(produto1.cor, produto2.cor)
        self.assertEqual(produto1.preco, produto2.preco)


if __name__ == '__main__':
    unittest.main()
