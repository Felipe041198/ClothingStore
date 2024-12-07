import PySimpleGUI as sg
from typing import List
from src.utils.enum_operacoes import Operacao
from src.utils.enum_tipo_cadastro import TipoCadastro


class AbstractTelaCadastro:
    def __init__(self, tipo_cadastro: TipoCadastro) -> None:
        self.option = None
        self.tipo_cadastro = tipo_cadastro
        sg.theme_background_color("#2C2F36")

    def criar_layout(self):
        layout = [
            [sg.Text(f"MENU DE {self.tipo_cadastro.plural.upper()}",
                     font=("Courier", 24, "bold"),
                     text_color="white",
                     background_color="#2C2F36",
                     justification='center',
                     expand_x=True)],
            [sg.Text("", size=(1, 2), background_color="#2C2F36")],  # Espaçamento vertical
            [sg.Button(f"Cadastrar novo {self.tipo_cadastro.singular}", key=1, size=(25, 2),
                       font=("Arial", 12), button_color=("#FFFFFF", "#3E4349"),
                       mouseover_colors=("#FFFFFF", "#1F2225"))],
            [sg.Button(f"Listar {self.tipo_cadastro.plural}", key=2, size=(25, 2),
                       font=("Arial", 12), button_color=("#FFFFFF", "#3E4349"),
                       mouseover_colors=("#FFFFFF", "#1F2225"))],
            [sg.Button(f"Procurar {self.tipo_cadastro.singular} por {self.tipo_cadastro.identificador}", key=3,
                       size=(25, 2),
                       font=("Arial", 12), button_color=("#FFFFFF", "#3E4349"),
                       mouseover_colors=("#FFFFFF", "#1F2225"))]
            if not self.tipo_cadastro == TipoCadastro.PEDIDO else None,
            [sg.Button(f"Excluir {self.tipo_cadastro.singular} por {self.tipo_cadastro.identificador}", key=4,
                       size=(25, 2),
                       font=("Arial", 12), button_color=("#FFFFFF", "#3E4349"),
                       mouseover_colors=("#FFFFFF", "#1F2225"))],
            [sg.Button(f"Editar {self.tipo_cadastro.singular} por {self.tipo_cadastro.identificador}", key=5,
                       size=(25, 2),
                       font=("Arial", 12), button_color=("#FFFFFF", "#3E4349"),
                       mouseover_colors=("#FFFFFF", "#1F2225"))]
            if not self.tipo_cadastro == TipoCadastro.PEDIDO else None,
            [sg.Button("Voltar ao menu principal", key=0, size=(25, 2),
                       font=("Arial", 12), button_color=("#FFFFFF", "red"),
                       mouseover_colors=("#FFFFFF", "#500000"))]
        ]

        # Remove Nones do layout
        return [element for element in layout if element is not None]

    def menu(self, opcoes: List[int]) -> int:
        layout = self.criar_layout()
        window = sg.Window(f"Menu de {self.tipo_cadastro.plural.capitalize()}", layout, size=(800, 500),
                           element_justification='center')

        while True:
            event, _ = window.read()

            if event in opcoes or event in [sg.WIN_CLOSED, 0]:
                self.option = event
                break

        window.close()
        return self.option

    def obter_cpf(self, tipo_busca: Operacao) -> str:
        layout = [
            [sg.Text(f'--- Qual CPF do {self.tipo_cadastro.singular} que deseja {tipo_busca.value}? ---',
                     background_color="#2C2F36", text_color="#FFFFFF")],
            [sg.InputText(key='cpf')],
            [sg.Button('OK')]
        ]

        window = sg.Window('Obter CPF', layout)
        event, values = window.read()
        window.close()

        if event == 'OK':
            return values['cpf']
        return ''

    def sucesso_cadastro(self):
        sg.popup(f"{self.tipo_cadastro.singular.capitalize()} cadastrado com sucesso!")

    def sucesso_alteracao(self):
        sg.popup(f"{self.tipo_cadastro.singular.capitalize()} alterado com sucesso!")

    def sucesso_exclusao(self, nome: str = ""):
        sg.popup(f"{self.tipo_cadastro.singular.capitalize()} {nome} excluído com sucesso!")

    def sem_cadastro(self):
        sg.popup(f"Não há {self.tipo_cadastro.plural} cadastrados.")

    def cadastro_nao_encontrado(self):
        sg.popup("Cadastro não encontrado.")

    def mostrar_erro(self, erro: str):
        sg.popup(erro)
