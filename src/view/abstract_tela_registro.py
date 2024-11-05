from typing import List

from src.utils.enum_tipo_cadastro import TipoCadastro
from src.view.abstract_tela import AbstractTela


class AbstractTelaRelatorio(AbstractTela):
    def __init__(self, tipo_cadastro: TipoCadastro):
        self.tipo_cadastro = tipo_cadastro

    def menu_principal(self, opcoes: List[int]) -> int:
        print(f"\n--- Menu de Relatórios---")
        print(f"1. Ultima compra de cliente")
        print(f"2. Ultima venda de vendedor")
        print(f"3. Relatórios sobre pedidos(s)")
        print("0. Voltar ao menu principal")
        opcao = self.le_num_inteiro("Escolha a opção: ", opcoes)
        return opcao

    def menu_periodo(self,  opcoes: List[int]) -> int:
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
        print(f"Histórico não encontrado.")
