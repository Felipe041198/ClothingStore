import unittest
from unittest import TestCase
from unittest.mock import patch, NonCallableMock

from src.controller.controlador_clientes import ControladorClientes
from src.controller.controlador_sistema import ControladorSistema
from src.mocks.cliente_mock import cliente1, cliente2


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

        self.controlador.cadastrar_cliente()
        mock_sucesso_cadastro.assert_called_once()

        # Verifica se o cliente foi adicionado
        self.assertEqual(len(self.controlador.clientes), 1)
        self.assertEqual(self.controlador.clientes[0].nome, cliente1.nome)
        self.assertEqual(self.controlador.clientes[0].cpf, cliente1.cpf)
        self.assertEqual(self.controlador.clientes[0].categoria, cliente1.categoria)
        self.assertEqual(self.controlador.clientes[0].data_nasc, cliente1.data_nasc)
        self.assertEqual(self.controlador.clientes[0].codigo, cliente1.codigo)

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
    @patch('src.view.tela_clientes.TelaClientes.sem_cadastro')
    def test_listar_clientes_vazio(self, mock_sem_cadastro):

        # Chama a função de listar clientes
        result = self.controlador.listar_clientes()

        # Verifica se foi chamado e o tamanho
        mock_sem_cadastro.assert_called_once()
        self.assertEqual(len(result), 0)
        self.assertEqual(len(self.controlador.clientes), 0)

    @patch('src.view.tela_clientes.TelaClientes.obter_cpf')
    @patch('src.view.tela_clientes.TelaClientes.exibir_cliente')
    def test_busca_cliente(self, mock_exibir_cliente, mock_obter_cpf):
        # Adiciona cliente
        self.controlador.clientes.append(cliente1)

        # Mockando o CPF a ser procurado
        mock_obter_cpf.return_value = cliente1.cpf
        self.controlador.busca_cliente()

        # Verifica se a função exibir_cliente foi chamada
        mock_exibir_cliente.assert_called_once_with(cliente1)

    @patch('src.view.tela_clientes.TelaClientes.cadastro_nao_encontrado')
    @patch('src.view.tela_clientes.TelaClientes.obter_cpf')
    @patch('src.view.tela_clientes.TelaClientes.exibir_cliente')
    def test_busca_cliente_nao_encontrado(
            self,
            mock_exibir_cliente,
            mock_obter_cpf,
            mock_cadastro_nao_encontrado : NonCallableMock
    ):

        # Mockando o CPF a ser procurado
        mock_obter_cpf.return_value = cliente1.cpf
        self.controlador.busca_cliente()

        # Verifica se a função exibir_cliente foi chamada
        mock_exibir_cliente.assert_not_called()
        mock_cadastro_nao_encontrado.assert_called_once()

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

    @patch('src.view.tela_clientes.TelaClientes.cadastro_nao_encontrado')
    @patch('src.view.tela_clientes.TelaClientes.obter_cpf')
    @patch('src.view.tela_clientes.TelaClientes.sucesso_exclusao')
    def test_exclui_cliente_cadastro_nao_encontrado(
            self,
            mock_sucesso_exclusao,
            mock_obter_cpf,
            mock_cadastro_nao_encontrado : NonCallableMock
    ):

        # Mockando o CPF a ser procurado
        mock_obter_cpf.return_value = cliente1.cpf
        self.controlador.busca_cliente()

        # Verifica se a função exibir_cliente foi chamada
        mock_sucesso_exclusao.assert_not_called()
        mock_cadastro_nao_encontrado.assert_called_once()

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
        self.assertEqual(self.controlador.clientes[0].cpf, cliente2.cpf)
        self.assertEqual(self.controlador.clientes[0].nome, cliente2.nome)
        self.assertEqual(self.controlador.clientes[0].data_nasc, cliente2.data_nasc)
        self.assertEqual(self.controlador.clientes[0].categoria, cliente2.categoria)
        self.assertEqual(self.controlador.clientes[0].codigo, cliente2.codigo)
        mock_sucesso_alteracao.assert_called_once()

    @patch('src.view.tela_clientes.TelaClientes.cadastro_nao_encontrado')
    @patch('src.view.tela_clientes.TelaClientes.obter_cpf')
    @patch('src.view.tela_clientes.TelaClientes.sucesso_alteracao')
    def test_edita_cliente_cadastro_nao_encontrado(
            self,
            mock_sucesso_alteracao,
            mock_obter_cpf,
            mock_cadastro_nao_encontrado: NonCallableMock
    ):
        # Mockando o CPF a ser procurado
        mock_obter_cpf.return_value = cliente1.cpf
        self.controlador.busca_cliente()

        # Verifica se a função exibir_cliente foi chamada
        mock_sucesso_alteracao.assert_not_called()
        mock_cadastro_nao_encontrado.assert_called_once()


if __name__ == '__main__':
    unittest.main()
