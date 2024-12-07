import PySimpleGUI as sg
from typing import List, Dict, Any
from src.utils.enum_tipo_cadastro import TipoCadastro
from src.view.abstract_gui_tela_cadastro import AbstractTelaCadastro


class TelaVendedores(AbstractTelaCadastro):
    def __init__(self):
        super().__init__(tipo_cadastro=TipoCadastro.VENDEDOR)

    def obter_dados_vendedor(self, codigo: int) -> (dict[str, int | float | Any], bool):
        layout = [
            [sg.Text('--- Cadastro de Vendedor ---', font=("Courier", 24, "bold"), text_color="white",
                     background_color="#2C2F36")],
            [sg.Text('CPF:', size=(15, 1), background_color="#2C2F36", text_color="white"), sg.InputText(key='cpf')],
            [sg.Text('Nome:', size=(15, 1), background_color="#2C2F36", text_color="white"), sg.InputText(key='nome')],
            [sg.Text('Data de Nascimento:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.InputText(key='data_nasc')],
            [sg.Text(f'Código gerado: {codigo}', size=(15, 1), background_color="#2C2F36", text_color="white")],
            [sg.Text('Salário:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.InputText(key='salario')],
            [sg.Button('Cadastrar', size=(10, 1), button_color=("#FFFFFF", "#3E4349")),
             sg.Button('Voltar', size=(10, 1), button_color=("#FFFFFF", "#3E4349"))]
        ]

        window = sg.Window('Cadastro de Vendedor', layout, background_color="#2C2F36")

        dados_vendedor = {}
        should_exit_to_menu = False

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == 'Voltar':
                if not any(values.values()):  # Se todos os campos estão vazios, pode fechar
                    should_exit_to_menu = True
                    break
                else:
                    user_response = sg.popup_yes_no(
                        "Há informações preenchidas. Tem certeza que deseja voltar? As informações serão perdidas.",
                        title="Confirmação",
                        background_color="#2C2F36",
                        text_color="white",
                        button_color=("#FFFFFF", "#3E4349")
                    )
                    if user_response == "Yes":
                        should_exit_to_menu = True
                        break
            elif event == 'Cadastrar':
                if any(values.values()):  # Apenas tente capturar se houver algo preenchido
                    dados_vendedor = {
                        "cpf": values['cpf'],
                        "nome": values['nome'],
                        "data_nasc": values['data_nasc'],
                        "codigo": codigo,
                        "salario": float(values['salario']) if values['salario'] else 0.0
                    }
                    break

        window.close()

        return dados_vendedor, should_exit_to_menu

    def exibir_vendedor(self, vendedor: dict):
        salario_formatado = f"R${vendedor['salario']}".replace('.', ',')
        sg.popup(f"Código: {vendedor['codigo']}\n"
                 f"Nome: {vendedor['nome']}\n"
                 f"CPF: {vendedor['cpf']}\n"
                 f"Data de nascimento: {vendedor['data_nasc']}\n"
                 f"Salário: {salario_formatado}",
                 background_color="#2C2F36", text_color="white")

    def exibir_vendedores(self, vendedores: List[dict]):
        layout = [[sg.Text("--- Lista de Vendedores ---", font=("Courier", 18, "bold"), text_color="white",
                           background_color="#2C2F36")]]
        for vendedor in vendedores:
            salario_formatado = f"R${vendedor['salario']}".replace('.', ',')
            layout.append([sg.Text(f"Código: {vendedor['codigo']}, "
                                   f"Nome: {vendedor['nome']}, "
                                   f"CPF: {vendedor['cpf']}, "
                                   f"Data de nascimento: {vendedor['data_nasc']}, "
                                   f"Salário: {salario_formatado}",
                                   background_color="#2C2F36", text_color="white")])

        layout.append([sg.Button("Voltar", button_color=("#FFFFFF", "#3E4349"))])
        window = sg.Window("Vendedores", layout, background_color="#2C2F36")
        window.read()
        window.close()

    def editar_dados_vendedor(self, vendedor: dict) -> (dict, bool):
        layout = [
            [sg.Text('--- Editar Vendedor ---', font=("Courier", 24, "bold"), text_color="white",
                     background_color="#2C2F36")],
            [sg.Text(f"Nome atual ({vendedor['nome']})", size=(30, 1), background_color="#2C2F36", text_color="white"),
             sg.InputText(key='nome', default_text=vendedor['nome'])],
            [sg.Text(f"CPF atual ({vendedor['cpf']})", size=(30, 1), background_color="#2C2F36", text_color="white"),
             sg.InputText(key='cpf', default_text=vendedor['cpf'])],
            [sg.Text(f"Data de nascimento atual ({vendedor['data_nasc']})", size=(30, 1), background_color="#2C2F36",
                     text_color="white"),
             sg.InputText(key='data_nasc', default_text=vendedor['data_nasc'])],
            [sg.Text(f"Salário atual ({vendedor['salario']:.2f})", size=(30, 1), background_color="#2C2F36",
                     text_color="white"),
             sg.InputText(key='salario', default_text=f"{vendedor['salario']}")],
            [sg.Button('OK', size=(10, 1), button_color=("#FFFFFF", "#3E4349")),
             sg.Button('Cancelar', size=(10, 1), button_color=("#FFFFFF", "#3E4349"))]
        ]

        window = sg.Window('Editar Vendedor', layout, background_color="#2C2F36")

        dados_vendedor = vendedor
        should_exit_to_menu = False

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == 'Cancelar':
                if any(values.values()):  # Se há informações preenchidas
                    if sg.popup_yes_no(
                            "Há informações preenchidas. Tem certeza que deseja voltar? As informações serão perdidas.",
                            title="Confirmação",
                            background_color="#2C2F36",
                            text_color="white",
                            button_color=("#FFFFFF", "#3E4349")
                    ) == "Sim":
                        should_exit_to_menu = True
                        dados_vendedor = {}
                        break
                else:
                    should_exit_to_menu = True
                    dados_vendedor = {}
                    break
            elif event == 'OK':
                dados_vendedor.update({
                    "cpf": values['cpf'],
                    "nome": values['nome'],
                    "data_nasc": values['data_nasc'],
                    "salario": float(values['salario'])
                })
                break

        window.close()
        return dados_vendedor if dados_vendedor else None, should_exit_to_menu
