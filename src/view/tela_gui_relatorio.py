import PySimpleGUI as sg
from datetime import datetime
from typing import List, Optional


class TelaRelatorio:
    def __init__(self):
        self.__background_color = "#2C2F36"
        self.__text_color = "white"

    def menu(self, opcoes: List[int]) -> int:
        layout = [
            [sg.Text("MENU DE RELATÓRIOS", font=("Courier", 24, "bold"),
                     text_color=self.__text_color, background_color=self.__background_color,
                     justification='center', expand_x=True)],
            [sg.Button("Última compra por cliente", key=1, size=(30, 2),
                       font=("Arial", 12), button_color=("#FFFFFF", "#3E4349"),
                       mouseover_colors=("#FFFFFF", "#1F2225"))],
            [sg.Button("Última venda por vendedor", key=2, size=(30, 2),
                       font=("Arial", 12), button_color=("#FFFFFF", "#3E4349"),
                       mouseover_colors=("#FFFFFF", "#1F2225"))],
            [sg.Button("Relatório por tipo de cliente", key=3, size=(30, 2),
                       font=("Arial", 12), button_color=("#FFFFFF", "#3E4349"),
                       mouseover_colors=("#FFFFFF", "#1F2225"))],
            [sg.Button("Relatório por dia", key=4, size=(30, 2),
                       font=("Arial", 12), button_color=("#FFFFFF", "#3E4349"),
                       mouseover_colors=("#FFFFFF", "#1F2225"))],
            [sg.Button("Voltar ao menu principal", key=0, size=(30, 2),
                       font=("Arial", 12), button_color=("#FFFFFF", "red"),
                       mouseover_colors=("#FFFFFF", "#500000"))]
        ]

        window = sg.Window("Menu de Relatórios", layout, background_color=self.__background_color,
                           element_justification='center', finalize=True)

        escolha = None
        while True:
            event, _ = window.read()
            if event in opcoes or event in [sg.WINDOW_CLOSED, 0]:
                escolha = event
                break
        window.close()
        return escolha

    def exibir_mensagem(self, mensagem: str):
        sg.popup(mensagem,
                 title="Mensagem",
                 background_color=self.__background_color,
                 text_color=self.__text_color
                 )

    def exibir_ultima_compra(self, venda):
        produtos = [
            [produto['codigo_produto'],
             produto['nome'],
             produto['quantidade'],
             f"R${produto['preco_venda']:.2f}"]
            for produto in venda['produtos']]

        layout = [
            [sg.Text(f"Última Compra de {venda['cliente']['nome']}", font=("Courier", 18, "bold"),
                     text_color=self.__text_color, background_color=self.__background_color)],
            [sg.Text("Vendedor:",
                     font=("Arial", 12),
                     background_color=self.__background_color,
                     text_color="white"),
             sg.Text(venda['vendedor']['nome'], font=("Arial", 12), background_color=self.__background_color,
                     text_color="white")],
            [sg.Text("Data da venda:", font=("Arial", 12), background_color=self.__background_color,
                     text_color="white"),
             sg.Text(venda['data_venda'], font=("Arial", 12), background_color=self.__background_color,
                     text_color="white")],
            [sg.Table(values=produtos, headings=["Código", "Nome", "Quantidade", "Preço"],
                      auto_size_columns=False, justification='center', num_rows=10,
                      background_color="#3E4349", text_color="white")],
            [sg.Text(f"Valor Total: R${venda['valor_total']:.2f}", font=("Arial", 14),
                     background_color=self.__background_color, text_color=self.__text_color)],
            [sg.Button("OK", size=(10, 1), button_color=("#FFFFFF", "#3E4349"))]
        ]

        window = sg.Window("Detalhes da Última Compra",
                           layout,
                           background_color=self.__background_color,
                           finalize=True)
        while True:
            event, _ = window.read()
            if event in [sg.WINDOW_CLOSED, "OK"]:
                break
        window.close()

    def exibir_ultima_venda(self, venda):
        produtos = [
            [produto['codigo_produto'],
             produto['nome'],
             produto['quantidade'],
             f"R${produto['preco_venda']:.2f}"]
            for produto in venda['produtos']]

        layout = [
            [sg.Text(f"Última Venda de {venda['vendedor']['nome']}", font=("Courier", 18),
                     text_color=self.__text_color, background_color=self.__background_color)],
            [sg.Text("Cliente:",
                     font=("Arial", 12),
                     background_color=self.__background_color,
                     text_color="white"),
             sg.Text(venda['cliente']['nome'], font=("Arial", 12), background_color=self.__background_color,
                     text_color="white")],
            [sg.Text("Data da venda:", font=("Arial", 12), background_color=self.__background_color,
                     text_color="white"),
             sg.Text(venda['data_venda'], font=("Arial", 12), background_color=self.__background_color,
                     text_color="white")],
            [sg.Table(values=produtos, headings=["Código", "Nome", "Quantidade", "Preço"],
                      auto_size_columns=False, justification='center', num_rows=10,
                      background_color="#3E4349", text_color="white")],
            [sg.Text(f"Valor Total: R${venda['valor_total']:.2f}", font=("Arial", 14),
                     background_color=self.__background_color, text_color=self.__text_color)],
            [sg.Button("OK", size=(10, 1), button_color=("#FFFFFF", "#3E4349"))]
        ]

        window = sg.Window("Detalhes da Última Venda",
                           layout,
                           background_color=self.__background_color,
                           finalize=True)
        while True:
            event, _ = window.read()
            if event in [sg.WINDOW_CLOSED, "OK"]:
                break
        window.close()

    def mostrar_relatorio_por_tipo_cliente(self, relatorio_por_tipo: dict):
        data = []
        for tipo, vendas in relatorio_por_tipo.items():
            for venda in vendas:
                data.append(
                    [tipo.value,
                     venda['cliente']['nome'],
                     venda['vendedor']['nome'],
                     f"R${venda['valor_total']:.2f}",
                     venda['data_venda']])

        layout = [
            [sg.Text("Relatório por Tipo de Cliente", font=("Courier", 18),
                     text_color=self.__text_color, background_color=self.__background_color)],
            [sg.Table(values=data, headings=["Tipo", "Cliente", "Vendedor", "Valor Total", "data_venda"],
                      auto_size_columns=False, justification='center', num_rows=10,
                      background_color="#3E4349", text_color="white")],
            [sg.Button("OK", size=(10, 1), button_color=("#FFFFFF", "#3E4349"))]
        ]

        window = sg.Window("Relatório por Tipo de Cliente", layout, background_color=self.__background_color,
                           finalize=True)
        while True:
            event, _ = window.read()
            if event in [sg.WINDOW_CLOSED, "OK"]:
                break
        window.close()

    def selecionar_dia_relatorio(self, dias_disponiveis: List[str]) -> Optional[datetime]:
        layout = [
            [sg.Text("Selecione um Dia para o Relatório", font=("Courier", 18),
                     text_color=self.__text_color, background_color=self.__background_color)],
            [sg.Listbox(values=[dia for dia in dias_disponiveis], size=(30, 10), key="-DIA-")],
            [sg.Button("Selecionar", size=(10, 1), button_color=("#FFFFFF", "#3E4349")),
             sg.Button("Voltar", size=(10, 1), button_color=("#FFFFFF", "red"))]
        ]

        window = sg.Window("Relatório por Dia",
                           layout,
                           background_color=self.__background_color,
                           finalize=True)
        dia_selecionado = None
        while True:
            event, values = window.read()
            if event in [sg.WINDOW_CLOSED, "Voltar"]:
                break
            if event == "Selecionar" and values["-DIA-"]:
                dia_selecionado = values["-DIA-"][0]
                break
        window.close()
        return dia_selecionado

    def mostrar_relatorio_por_dia(self, dia: datetime, vendas_no_dia: List):
        data = [[venda['cliente']['nome'],
                 venda['vendedor']['nome'],
                 f"R${venda['valor_total']:.2f}"]
                for venda in vendas_no_dia]

        layout = [
            [sg.Text(f"Relatório do Dia {dia}", font=("Courier", 18),
                     text_color=self.__text_color, background_color=self.__background_color)],
            [sg.Table(values=data, headings=["Cliente", "Vendedor", "Valor Total"],
                      auto_size_columns=False, justification='center', num_rows=10,
                      background_color="#3E4349", text_color="white")],
            [sg.Button("OK", size=(10, 1), button_color=("#FFFFFF", "#3E4349"))]
        ]

        window = sg.Window("Relatório por Dia",
                           layout,
                           background_color=self.__background_color,
                           finalize=True)
        while True:
            event, _ = window.read()
            if event in [sg.WINDOW_CLOSED, "OK"]:
                break
        window.close()

    def mostrar_erro(self, erro: str):
        sg.popup(erro)
