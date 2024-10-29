from src.view.abstract_tela import AbstractTela


class TelaSistema(AbstractTela):

    def __init__(self) -> None:
        pass

    def tela_opcoes(self, opcoes):
        print("\n--- Sistema de Gerenciamento de Loja de Roupas ---")
        print("1. Cadastrar Clientes")
        print("2. Cadastrar Vendedores")
        print("3. Cadastrar Produtos")
        print("4. Registrar Vendas")
        print("5. Consultar histórico")
        print("6. Sair")
        opcao = self.le_num_inteiro("Escolha a opção: ", opcoes)
        return opcao
