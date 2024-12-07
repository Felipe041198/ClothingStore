import PySimpleGUI as sg
from typing import List
from src.utils.enum_tipo_cadastro import TipoCadastro


class TelaRelatorio:
    def __init__(self):
        self.tipo_cadastro = TipoCadastro.PEDIDO

    def menu_principal(self, opcoes: List[int]) -> int:
        layout = [
            [sg.Text('--- Menu de Relatórios ---')],
            [sg.Button('1. Última compra de cliente')],
            [sg.Button('2. Última venda de vendedor')],
            [sg.Button('3. Relatório por tipo de clientes')],
            [sg.Button('4. Relatório por dia')],
            [sg.Button('0. Voltar ao menu principal')],
        ]

        window = sg.Window('Menu de Relatórios', layout)
        event, _ = window.read()
        window.close()

        try:
            opcao = int(event.split('.')[0])
            if opcao in opcoes:
                return opcao
        except (ValueError, AttributeError):
            sg.popup('Opção inválida, tente novamente.')

    def menu_periodo(self, opcoes: List[int]) -> int:
        layout = [
            [sg.Text('Selecione o período para o relatório:')],
            [sg.Button('1 - Últimas 24 horas')],
            [sg.Button('2 - Últimos 7 dias')],
            [sg.Button('3 - Últimos 15 dias')],
            [sg.Button('4 - Último mês')],
            [sg.Button('5 - Visualizar todos os registros')],
            [sg.Button('0 - Voltar')],
        ]

        window = sg.Window('Seleção de Período', layout)
        event, _ = window.read()
        window.close()

        try:
            escolha = int(event.split(' ')[0])
            if escolha in opcoes:
                return escolha
        except (ValueError, AttributeError):
            sg.popup('Opção inválida, tente novamente.')

    def sem_historico(self):
        sg.popup("Histórico não encontrado.")

    def exibir_mensagem(self, mensagem: str):
        sg.popup(mensagem)

    def exibir_ultima_compra(self, venda):
        """Exibe os detalhes da última compra."""
        cliente_info = f"Cliente: {venda.cliente.nome}\nCPF: {venda.cliente.cpf}"
        data_info = f"Data da Venda: {venda.data_venda.strftime('%d/%m/%Y %H:%M:%S')}"
        produtos_info = "\n".join(
            [f"- Código: {produto.codigo_produto} Quantidade: {produto.quantidade}, "
             f"Valor: R$ {produto.quantidade * produto.preco_venda:.2f}"
             for produto in venda.produtos]
        )
        valor_total = f"Valor Total: R$ {venda.valor_total:.2f}"

        sg.popup(
            f"--- Última Compra ---\n{cliente_info}\n{data_info}\nProdutos Comprados:\n{produtos_info}\n{valor_total}")

    # Continue com os outros métodos para exibir informações de maneira semelhante usando sg.popup() ou outras funções adequadas do PySimpleGUI.


# Exemplo de uso da classe para abrir um menu
if __name__ == "__main__":
    tela = TelaRelatorio()
    tela.menu_principal(opcoes=[0, 1, 2, 3, 4])
