import PySimpleGUI as sg
from src.view.abstract_tela import AbstractTela


class TelaSistema(AbstractTela):
    def __init__(self) -> None:
        self.option = None

    def criar_layout(self):
        return [
            [sg.Text("MENU PRINCIPAL", font=("Courier", 24, "bold"), text_color="white", background_color="#2C2F36",
                     justification='center', expand_x=True)],
            [sg.Text("", size=(1, 2), background_color="#2C2F36")],  # Espaçamento vertical de 40 pixels
            [sg.Button("Cadastrar Clientes", key=1, size=(20, 2), font=("Arial", 12),
                       button_color=("#FFFFFF", "#3E4349"), mouseover_colors=("#FFFFFF", "#1F2225"))],
            [sg.Button("Cadastrar Vendedores", key=2, size=(20, 2), font=("Arial", 12),
                       button_color=("#FFFFFF", "#3E4349"), mouseover_colors=("#FFFFFF", "#1F2225"))],
            [sg.Button("Cadastrar Produtos", key=3, size=(20, 2), font=("Arial", 12),
                       button_color=("#FFFFFF", "#3E4349"), mouseover_colors=("#FFFFFF", "#1F2225"))],
            [sg.Button("Registrar Vendas", key=4, size=(20, 2), font=("Arial", 12),
                       button_color=("#FFFFFF", "#3E4349"), mouseover_colors=("#FFFFFF", "#1F2225"))],
            [sg.Button("Consultar Histórico", key=5, size=(20, 2), font=("Arial", 12),
                       button_color=("#FFFFFF", "#3E4349"), mouseover_colors=("#FFFFFF", "#1F2225"))],
            [sg.Button("Mock Dados", key=99, size=(20, 2), font=("Arial", 12),
                       button_color=("#FFFFFF", "#3E4349"), mouseover_colors=("#FFFFFF", "#1F2225"))],
            [sg.Button("Sair", key=0, size=(20, 2), font=("Arial", 12), button_color=("#FFFFFF", "red"),
                       mouseover_colors=("#FFFFFF", "#500000"))]
        ]

    def tela_opcoes(self, opcoes):
        layout = self.criar_layout()
        sg.theme_background_color("#2C2F36")
        window = sg.Window("Sistema de Gerenciamento de Loja de Roupas", layout, size=(800, 500),
                           element_justification='center')

        while True:
            event, values = window.read()

            if event in opcoes or event in [sg.WIN_CLOSED, 0]:  # Inclui condição para fechar janela
                self.set_option(event)
                break

        window.close()
        return self.option

    def set_option(self, opcao):
        self.option = opcao
