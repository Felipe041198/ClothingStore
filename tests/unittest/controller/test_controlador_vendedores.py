import unittest
from unittest import TestCase
from unittest.mock import patch, MagicMock

from src.controller.controlador_sistema import ControladorSistema
from src.controller.controlador_vendedores import ControladorVendedores
from src.exceptions.cpf_nao_encontrado_exception import CpfNaoEncontradoException
from src.exceptions.nenhum_registro_encontrado_exception import NenhumRegistroEncontradoException
from src.mocks.vendedores_mock import vendedor1, vendedor2
from src.model.vendedor import Vendedor


class TestControladorVendedores(TestCase):
    def setUp(self):
        self.controlador_sistema = ControladorSistema()
        self.controlador_sistema._ControladorSistema__tela_sistema = MagicMock()

        self.controlador = ControladorVendedores(self.controlador_sistema)
        self.__mock_tela_vendedores = MagicMock()
        self.controlador._ControladorVendedores__tela_vendedores = self.__mock_tela_vendedores

    # Teste para o cadastro de vendedores
    def test_cadastrar_vendedor(self):
        self.controlador._ControladorVendedores__tela_vendedores.obter_dados_vendedor.return_value \
            = vendedor1.to_dict(), False

        resultado = self.controlador.cadastrar_vendedor()

        self.controlador._ControladorVendedores__tela_vendedores.sucesso_cadastro.assert_called_once()
        self.assertEqual(len(self.controlador.vendedores), 1)
        self.compara_vendedores(resultado, vendedor1)

    # Teste para a listagem de vendedores
    def test_listar_vendedores(self):
        self.controlador.vendedores.append(vendedor1)
        self.controlador.vendedores.append(vendedor2)

        resultado = self.controlador.listar_vendedores()

        self.controlador._ControladorVendedores__tela_vendedores.exibir_vendedores.assert_called_once()
        self.assertEqual(len(resultado), 2)

    # Teste para listagem de vendedores vazia
    @patch('src.view.tela_gui_vendedores.TelaVendedores.mostrar_erro')
    def test_listar_vendedores_vazio(self, mock_mostrar_erro):
        result = self.controlador.listar_vendedores()

        self.controlador._ControladorVendedores__tela_vendedores.mostrar_erro.assert_called_once_with(
            str(NenhumRegistroEncontradoException())
        )
        self.assertEqual(len(self.controlador.vendedores), 0)
        self.assertIsNone(result)

    # Teste para a busca de vendedores
    @patch('src.view.tela_gui_vendedores.TelaVendedores.obter_cpf')
    @patch('src.view.tela_gui_vendedores.TelaVendedores.exibir_vendedor')
    def test_busca_vendedor(self, mock_exibir_vendedor, mock_obter_cpf):
        self.controlador.vendedores.append(vendedor1)
        self.controlador._ControladorVendedores__tela_vendedores.obter_cpf.return_value = vendedor1.cpf

        resultado = self.controlador.busca_vendedor()

        self.controlador._ControladorVendedores__tela_vendedores.exibir_vendedor.assert_called_once_with(
            vendedor1.to_dict()
        )
        self.compara_vendedores(resultado, vendedor1)

    # Teste para a busca de vendedor não encontrado
    def test_busca_vendedor_nao_encontrado(self):
        self.controlador._ControladorVendedores__tela_vendedores.obter_cpf.return_value = vendedor1.cpf

        resultado = self.controlador.busca_vendedor()

        self.controlador._ControladorVendedores__tela_vendedores.mostrar_erro.assert_called_once_with(
            str(CpfNaoEncontradoException())
        )
        self.assertIsNone(resultado)

    # Teste para exclusão de vendedores
    def test_exclui_vendedor(self):
        self.controlador.vendedores.append(vendedor1)
        self.controlador._ControladorVendedores__tela_vendedores.obter_cpf.return_value = vendedor1.cpf

        self.controlador.exclui_vendedor()

        self.assertEqual(len(self.controlador.vendedores), 0)
        self.controlador._ControladorVendedores__tela_vendedores.sucesso_exclusao.assert_called_once_with(
            vendedor1.nome
        )

    # Teste para exclusão de vendedor não encontrado
    def test_exclui_vendedor_nao_encontrado(self):
        self.controlador._ControladorVendedores__tela_vendedores.obter_cpf.return_value = vendedor1.cpf

        resultado = self.controlador.exclui_vendedor()

        self.controlador._ControladorVendedores__tela_vendedores.mostrar_erro.assert_called_once_with(
            str(CpfNaoEncontradoException()))
        self.assertIsNone(resultado)

    # Função auxiliar para comparar vendedores
    def compara_vendedores(self, vendedor1: Vendedor, vendedor2: Vendedor):
        self.assertEqual(vendedor1.cpf, vendedor2.cpf)
        self.assertEqual(vendedor1.nome, vendedor2.nome)
        self.assertEqual(vendedor1.data_nasc, vendedor2.data_nasc)
        self.assertEqual(vendedor1.codigo, vendedor2.codigo)
        self.assertEqual(vendedor1.salario, vendedor2.salario)


if __name__ == '__main__':
    unittest.main()
