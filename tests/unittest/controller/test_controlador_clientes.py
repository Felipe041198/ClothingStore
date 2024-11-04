import unittest
from unittest import TestCase
from unittest.mock import patch

from src.controller.controlador_clientes import ControladorClientes
from src.controller.controlador_sistema import ControladorSistema
from src.exceptions.cpf_nao_encontrado_exception import CpfNaoEncontradoException
from src.exceptions.nenhum_registro_encontrado_exception import NenhumRegistroEncontradoException
from src.mocks.cliente_mock import cliente1, cliente2
from src.model.cliente import Cliente


class TestControladorClientes(TestCase):
    def setUp(self):
        self.controlador_sistema = ControladorSistema()
        self.controlador = ControladorClientes(self.controlador_sistema)

    # Teste para o cadastro de clientes
    @patch('src.view.tela_clientes.TelaClientes.sucesso_cadastro')
    @patch('src.view.tela_clientes.TelaClientes.obter_dados_cliente')
    def test_cadastrar_cliente(self, mock_obter_dados_cliente, mock_sucesso_cadastro):
        # Mockando a função obter_dados_cliente para retornar um cliente
        mock_obter_dados_cliente.return_value = cliente1

        resultado = self.controlador.cadastrar_cliente()
        mock_sucesso_cadastro.assert_called_once()

        # Verifica se o cliente foi adicionado
        self.assertEqual(len(self.controlador.clientes), 1)
        self.compara_clientes(resultado, cliente1)

    # Teste para a listagem de clientes
    @patch('src.view.tela_clientes.TelaClientes.exibir_clientes')
    def test_listar_clientes(self, mock_exibir_clientes):
        # Adicionando dois clientes
        self.controlador.clientes.append(cliente1)
        self.controlador.clientes.append(cliente2)

        # Chama a função de listar clientes
        result = self.controlador.listar_clientes()

        # Verifica se foi chamado e o tamanho
        mock_exibir_clientes.assert_called_once()
        self.assertEqual(len(result), 2)

    #  Teste para a listagem de clientes
    @patch('src.view.tela_clientes.TelaClientes.mostrar_erro')
    def test_listar_clientes_vazio(self, mock_mostrar_erro):

        # Chama a função de listar clientes
        result = self.controlador.listar_clientes()

        # Verifica se foi chamado e o tamanho
        mock_mostrar_erro.assert_called_once_with(str(NenhumRegistroEncontradoException()))
        self.assertIsNone(result)
        self.assertEqual(len(self.controlador.clientes), 0)

    #  Teste para a busca de clientes
    @patch('src.view.tela_clientes.TelaClientes.obter_cpf')
    @patch('src.view.tela_clientes.TelaClientes.exibir_cliente')
    def test_busca_cliente(self, mock_exibir_cliente, mock_obter_cpf):
        # Adiciona cliente
        self.controlador.clientes.append(cliente1)

        # Mockando o CPF a ser procurado
        mock_obter_cpf.return_value = cliente1.cpf
        resultado = self.controlador.busca_cliente()

        # Verifica se a função exibir_cliente foi chamada
        mock_exibir_cliente.assert_called_once_with(cliente1)
        self.compara_clientes(resultado, cliente1)

    #  Teste para a busca de cliente quando não encontrado
    @patch('src.view.tela_clientes.TelaClientes.mostrar_erro')
    @patch('src.view.tela_clientes.TelaClientes.obter_cpf')
    @patch('src.view.tela_clientes.TelaClientes.exibir_cliente')
    def test_busca_cliente_nao_encontrado(
            self,
            mock_exibir_cliente,
            mock_obter_cpf,
            mock_mostrar_erro
    ):

        # Mockando o CPF a ser procurado
        mock_obter_cpf.return_value = cliente1.cpf
        self.controlador.busca_cliente()

        # Verifica se a função exibir_cliente foi chamada
        mock_exibir_cliente.assert_not_called()
        mock_mostrar_erro.assert_called_once_with(str(CpfNaoEncontradoException()))

    #  Teste para a exclusão de clientes
    @patch('src.view.tela_clientes.TelaClientes.obter_cpf')
    @patch('src.view.tela_clientes.TelaClientes.sucesso_exclusao')
    def test_exclui_cliente(self, mock_sucesso_exclusao, mock_obter_cpf):
        # Adiciona cliente
        self.controlador.clientes.append(cliente1)

        # Mockando o CPF a ser excluído
        mock_obter_cpf.return_value = cliente1.cpf
        self.controlador.exclui_cliente()

        # Verifica se o cliente foi removido
        self.assertEqual(len(self.controlador.clientes), 0)
        mock_sucesso_exclusao.assert_called_once_with(cliente1.nome)

    #  Teste para a exclusão de clientes quando não encontrado
    @patch('src.view.tela_clientes.TelaClientes.mostrar_erro')
    @patch('src.view.tela_clientes.TelaClientes.obter_cpf')
    @patch('src.view.tela_clientes.TelaClientes.sucesso_exclusao')
    def test_exclui_cliente_cadastro_nao_encontrado(
            self,
            mock_sucesso_exclusao,
            mock_obter_cpf,
            mock_mostrar_erro
    ):

        # Mockando o CPF a ser procurado
        mock_obter_cpf.return_value = cliente1.cpf
        self.controlador.busca_cliente()

        # Verifica se a função exibir_cliente foi chamada
        mock_sucesso_exclusao.assert_not_called()
        mock_mostrar_erro.assert_called_once_with(str(CpfNaoEncontradoException()))

    #  Teste para a edição de clientes
    @patch('src.view.tela_clientes.TelaClientes.obter_cpf')
    @patch('src.view.tela_clientes.TelaClientes.editar_dados_cliente')
    @patch('src.view.tela_clientes.TelaClientes.sucesso_alteracao')
    def test_editar_cliente(self, mock_sucesso_alteracao, mock_editar_dados_cliente, mock_obter_cpf):
        # Adiciona cliente
        self.controlador.clientes.append(cliente1)

        # Mockando CPF e os novos dados
        mock_obter_cpf.return_value = cliente1.cpf
        mock_editar_dados_cliente.return_value = cliente2

        self.controlador.editar_cliente()

        # Verifica se os dados foram atualizados
        self.compara_clientes(self.controlador.clientes[0], cliente2)
        mock_sucesso_alteracao.assert_called_once()

    #  Teste para a edição de clientes quando não encontrado
    @patch('src.view.tela_clientes.TelaClientes.mostrar_erro')
    @patch('src.view.tela_clientes.TelaClientes.obter_cpf')
    @patch('src.view.tela_clientes.TelaClientes.sucesso_alteracao')
    def test_edita_cliente_cadastro_nao_encontrado(
            self,
            mock_sucesso_alteracao,
            mock_obter_cpf,
            mock_mostrar_erro
    ):
        # Mockando o CPF a ser procurado
        mock_obter_cpf.return_value = cliente1.cpf
        self.controlador.busca_cliente()

        # Verifica se a função exibir_cliente foi chamada
        mock_sucesso_alteracao.assert_not_called()
        mock_mostrar_erro.assert_called_once_with(str(CpfNaoEncontradoException()))

    def compara_clientes(self, cliente1: Cliente, cliente2: Cliente):
        self.assertEqual(cliente1.cpf, cliente2.cpf)
        self.assertEqual(cliente1.nome, cliente2.nome)
        self.assertEqual(cliente1.data_nasc, cliente2.data_nasc)
        self.assertEqual(cliente1.categoria, cliente2.categoria)
        self.assertEqual(cliente1.codigo, cliente2.codigo)


if __name__ == '__main__':
    unittest.main()
