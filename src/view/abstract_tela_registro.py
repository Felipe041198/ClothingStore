from typing import List

from src.utils.enum_tipo_cadastro import TipoCadastro
from src.view.abstract_tela import AbstractTela


class AbstractTelaRelatorio(AbstractTela):
    def __init__(self, tipo_cadastro: TipoCadastro):
        self.tipo_cadastro = tipo_cadastro

    def menu_principal(self, opcoes: List[int]) -> int:
        print("\n--- Menu de Relatórios---")
        print("1. Ultima compra de cliente")
        print("2. Ultima venda de vendedor")
        print("3. Relatório por tipo de clientes")
        print("4. Relatório por dia")
        print("0. Voltar ao menu principal")
        opcao = self.le_num_inteiro("Escolha a opção: ", opcoes)
        return opcao

    def menu_periodo(self, opcoes: List[int]) -> int:
        print("Selecione o período para o relatório:")
        print("1 - Últimas 24 horas")
        print("2 - Últimos 7 dias")
        print("3 - Últimos 15 dias")
        print("4 - Último mês")
        print("5 - Visualizar todos os registros")
        print("0 - Voltar")

        while True:
            try:
                escolha = int(input("Escolha uma opção: "))
                if escolha in opcoes:
                    return escolha
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    def sem_historico(self):
        print("Histórico não encontrado.")
