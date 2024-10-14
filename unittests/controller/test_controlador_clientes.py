import unittest
from unittest import TestCase
from unittest.mock import patch, MagicMock
from src.controller.controlador_clientes import ControladorClientes
from src.model.cliente import Cliente
from src.utils.enum_operacoes_cliente import OperacoesCliente


class TestControladorClientes(TestCase):
    def setUp(self):
        self.controlador = ControladorClientes()

    @patch('src.view.tela_clientes.TelaClientes.obter_dados_cliente')
    def test_cadastrar_cliente(self, mock_obter_dados_cliente):
        # Mockando a função obter_dados_cliente para retornar um cliente
        mock_obter_dados_cliente.return_value = Cliente(123456789, 'Cliente Teste', '01/01/1990', 1)

        self.controlador.cadastrar_cliente()

        # Verifica se o cliente foi adicionado
        self.assertEqual(len(self.controlador.listar_clientes()), 1)
        self.assertEqual(self.controlador.listar_clientes()[0].nome, 'Cliente Teste')

    def test_listar_clientes(self):
        # Adiciona cliente manualmente
        self.controlador._ControladorClientes__clientes.append(Cliente(123456789, 'Cliente Teste', '01/01/1990', 1))

        with patch('src.view.tela_clientes.TelaClientes.exibir_clientes') as mock_exibir_clientes:
            self.controlador.listar_clientes()
            mock_exibir_clientes.assert_called_once()

    @patch('src.view.tela_clientes.TelaClientes.obter_cpf')
    @patch('src.view.tela_clientes.TelaClientes.exibir_cliente')
    def test_busca_cliente(self, mock_exibir_cliente, mock_obter_cpf):
        # Adiciona cliente
        cliente = Cliente(123456789, 'Cliente Teste', '01/01/1990', 1)
        self.controlador._ControladorClientes__clientes.append(cliente)

        # Mockando o CPF a ser procurado
        mock_obter_cpf.return_value = 123456789
        self.controlador.busca_cliente()

        # Verifica se a função exibir_cliente foi chamada
        mock_exibir_cliente.assert_called_once_with(cliente)

    @patch('src.view.tela_clientes.TelaClientes.obter_cpf')
    @patch('src.view.tela_clientes.TelaClientes.sucesso_exclusao')
    def test_exclui_cliente(self, mock_sucesso_exclusao, mock_obter_cpf):
        # Adiciona cliente
        cliente = Cliente(123456789, 'Cliente Teste', '01/01/1990', 1)
        self.controlador._ControladorClientes__clientes.append(cliente)

        # Mockando o CPF a ser excluído
        mock_obter_cpf.return_value = 123456789
        self.controlador.exclui_cliente()

        # Verifica se o cliente foi removido
        self.assertEqual(len(self.controlador._ControladorClientes__clientes), 0)
        mock_sucesso_exclusao.assert_called_once_with(cliente.nome)

    @patch('src.view.tela_clientes.TelaClientes.obter_cpf')
    @patch('src.view.tela_clientes.TelaClientes.obter_dados_cliente')
    @patch('src.view.tela_clientes.TelaClientes.sucesso_alteracao')
    def test_editar_cliente(self, mock_sucesso_alteracao, mock_obter_dados_cliente, mock_obter_cpf):
        # Adiciona cliente
        cliente = Cliente(123456789, 'Cliente Teste', '01/01/1990', 1)
        self.controlador._ControladorClientes__clientes.append(cliente)

        # Mockando CPF e os novos dados
        mock_obter_cpf.return_value = 123456789
        mock_obter_dados_cliente.return_value = Cliente(123456789, 'Cliente Editado', '01/01/1991', 2)

        self.controlador.editar_cliente()

        # Verifica se os dados foram atualizados
        self.assertEqual(self.controlador._ControladorClientes__clientes[0].nome, 'Cliente Editado')
        self.assertEqual(self.controlador._ControladorClientes__clientes[0].data_nasc, '01/01/1991')
        self.assertEqual(self.controlador._ControladorClientes__clientes[0].categoria, 2)
        mock_sucesso_alteracao.assert_called_once()


if __name__ == '__main__':
    unittest.main()
