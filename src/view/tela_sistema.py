import PySimpleGUI as sg
from src.view.abstract_tela import AbstractTela


class TelaSistema(AbstractTela):
    def __init__(self) -> None:
        self.option = None
        self.layout = [
            [sg.Text("MENU PRINCIPAL", font=("Arial", 20), text_color="white", background_color="#2C2F36")],
            [sg.Button("Cadastrar Clientes", key=1, size=(20, 2), font=("Arial", 12),
                       button_color=("#FFFFFF", "#3E4349"))],
            [sg.Button("Cadastrar Vendedores", key=2, size=(20, 2), font=("Arial", 12),
                       button_color=("#FFFFFF", "#3E4349"))],
            [sg.Button("Cadastrar Produtos", key=3, size=(20, 2), font=("Arial", 12),
                       button_color=("#FFFFFF", "#3E4349"))],
            [sg.Button("Registrar Vendas", key=4, size=(20, 2), font=("Arial", 12),
                       button_color=("#FFFFFF", "#3E4349"))],
            [sg.Button("Consultar Histórico", key=5, size=(20, 2), font=("Arial", 12),
                       button_color=("#FFFFFF", "#3E4349"))],
            [sg.Button("Mock Dados", key=99, size=(20, 2), font=("Arial", 12), button_color=("#FFFFFF", "#3E4349"))],
            [sg.Button("Sair", key=0, size=(20, 2), font=("Arial", 12), button_color=("#FFFFFF", "red"))]
        ]

    def tela_opcoes(self, opcoes):
        sg.theme_background_color("#2C2F36")
        window = sg.Window("Sistema de Gerenciamento de Loja de Roupas", self.layout)

        while True:
            event, values = window.read()

            if event in opcoes:
                self.set_option(event)
                break

        window.close()
        return self.option

    def set_option(self, opcao):
        self.option = opcao
