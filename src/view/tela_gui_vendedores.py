import PySimpleGUI as sg
from typing import List
from src.utils.enum_tipo_cadastro import TipoCadastro
from src.utils.validador import Validador
from src.view.abstract_gui_tela_cadastro import AbstractTelaCadastro


class TelaVendedores(AbstractTelaCadastro):
    def __init__(self):
        super().__init__(tipo_cadastro=TipoCadastro.VENDEDOR)

    def obter_dados_vendedor(self, codigo: int) -> tuple[dict | None, bool]:
        layout = [
            [sg.Text('CADASTRO DE VENDEDOR', font=("Courier", 24, "bold"), text_color="white",
                     background_color="#2C2F36", justification='center', expand_x=True)],
            [sg.Text('Nome:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.InputText(key='nome')],
            [sg.Text('CPF:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.InputText(key='cpf')],
            [sg.Text('Data de Nascimento (dd/mm/yyyy):',
                     size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.InputText(key='data_nasc')],
            [sg.Text('Código gerado:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.Text(f'{codigo}', size=(15, 1), background_color="#2C2F36", text_color="white")],
            [sg.Text('Salário:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.InputText(key='salario')],
            [sg.Button('Cadastrar', size=(10, 1), button_color=("#FFFFFF", "#3E4349")),
             sg.Button('Voltar', size=(10, 1), button_color=("#FFFFFF", "#3E4349"))]
        ]

        window = sg.Window('Cadastro de Vendedor', layout, background_color="#2C2F36", finalize=True)
        dados_vendedor = None
        should_exit_to_menu = False

        while True:
            event, values = window.read()

            if event in (sg.WINDOW_CLOSED, 'Voltar'):
                if any(values.values()) and not self.confirmar_acoes("Há informações preenchidas."
                                                                     "Deseja descartar?"):
                    continue
                should_exit_to_menu = True
                break

            if event == 'Cadastrar':
                validadores = {
                    "nome": Validador.validar_nome,
                    "cpf": Validador.validar_cpf,
                    "data_nasc": Validador.validar_data_nascimento,
                    "salario": lambda salario: "inválido"
                    if not salario.replace('.', '', 1).isdigit() or float(
                        salario) <= 0 else "válido"
                }

                campos_invalidos = self.validar_campos(values, list(validadores.keys()), validadores)

                if campos_invalidos:
                    sg.popup(
                        f"Preencha os seguintes campos obrigatórios ou corrija valores inválidos:"
                        f"{', '.join(campos_invalidos)}",
                        title="Erro",
                        background_color="#2C2F36",
                        text_color="white"
                    )
                    continue

                dados_vendedor = {
                    "nome": values["nome"].strip(),
                    "cpf": values["cpf"].strip(),
                    "data_nasc": values["data_nasc"].strip(),
                    "codigo": codigo,
                    "salario": float(values["salario"])
                }
                break

        window.close()
        return dados_vendedor, should_exit_to_menu

    def exibir_vendedor(self, vendedor: dict):
        salario_formatado = f"R${vendedor['salario']:.2f}"
        layout = [
            [sg.Text("Detalhes do Vendedor", font=("Courier", 18, "bold"), text_color="white",
                     background_color="#2C2F36", justification='center', expand_x=True, pad=(0, 10))],
            [sg.Text("Nome:", font=("Arial", 12, "bold"), background_color="#2C2F36", text_color="white"),
             sg.Text(vendedor['nome'], font=("Arial", 12), background_color="#2C2F36", text_color="white")],
            [sg.Text("CPF:", font=("Arial", 12, "bold"), background_color="#2C2F36", text_color="white"),
             sg.Text(vendedor['cpf'], font=("Arial", 12), background_color="#2C2F36", text_color="white")],
            [sg.Text("Data de Nascimento:", font=("Arial", 12, "bold"),
                     background_color="#2C2F36", text_color="white"),
             sg.Text(vendedor['data_nasc'], font=("Arial", 12),
                     background_color="#2C2F36", text_color="white")],
            [sg.Text("Código:", font=("Arial", 12, "bold"), background_color="#2C2F36", text_color="white"),
             sg.Text(vendedor['codigo'], font=("Arial", 12), background_color="#2C2F36", text_color="white")],
            [sg.Text("Salário:", font=("Arial", 12, "bold"), background_color="#2C2F36", text_color="white"),
             sg.Text(salario_formatado, font=("Arial", 12), background_color="#2C2F36", text_color="white")],
            [sg.Button('OK', button_color=("#FFFFFF", "#3E4349"), size=(10, 1))]
        ]

        sg.Window("Detalhes do Vendedor", layout, background_color="#2C2F36").read(close=True)

    def exibir_vendedores(self, vendedores: List[dict]):
        header = ['CÓDIGO', 'NOME', 'CPF', 'DATA DE NASCIMENTO', 'SALÁRIO']
        data = [
            [vendedor['codigo'],
             vendedor['nome'],
             vendedor['cpf'],
             vendedor['data_nasc'],
             f"R${vendedor['salario']:.2f}".replace('.', ',')]
            for vendedor in vendedores
        ]

        layout = [
            [sg.Text("Lista de Vendedores", font=("Courier", 18, "bold"), text_color="white",
                     background_color="#2C2F36", justification='center', expand_x=True)],
            [
                sg.Column(
                    [[sg.Table(
                        data,
                        headings=header,
                        num_rows=min(len(data), 20),
                        key='-TABLE-',
                        background_color="#2C2F36",
                        text_color="white",
                        header_background_color="#007ACC",
                        header_text_color="white",
                        alternating_row_color="#3E4349",
                        auto_size_columns=False,
                        col_widths=[8, 20, 18, 20, 15],
                        justification='center',
                        row_height=35,
                        enable_events=True
                    )]],
                    element_justification='center',
                    expand_x=True
                )
            ],
            [sg.Button("Voltar", button_color=("#FFFFFF", "#3E4349"), size=(10, 1))]
        ]

        sg.Window(
            "Vendedores",
            layout,
            background_color="#2C2F36",
            size=(900, 500),
            resizable=True
        ).read(close=True)

    def editar_dados_vendedor(self, vendedor: dict) -> tuple[dict | None, bool]:
        layout = [
            [sg.Text('EDITAR VENDEDOR', font=("Courier", 18, "bold"),
                     text_color="white", background_color="#2C2F36", justification='center', expand_x=True)],
            [sg.Text('Código:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.Text(f"{vendedor['codigo']}", size=(15, 1), background_color="#2C2F36", text_color="white")],
            [sg.Text('Nome:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.InputText(default_text=vendedor['nome'], key='nome')],
            [sg.Text('CPF:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.InputText(default_text=vendedor['cpf'], key='cpf')],
            [sg.Text('Data de Nascimento:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.InputText(default_text=vendedor['data_nasc'], key='data_nasc')],
            [sg.Text('Salário:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.InputText(default_text=f"{vendedor['salario']:.2f}", key='salario')],
            [sg.Button('Salvar', button_color=("#FFFFFF", "#3E4349"), size=(10, 1)),
             sg.Button('Cancelar', button_color=("#FFFFFF", "#FF0000"), size=(10, 1))]
        ]

        window = sg.Window('Editar Vendedor', layout, background_color="#2C2F36", finalize=True)
        should_exit_to_menu = False
        dados_vendedor = None

        while True:
            event, values = window.read()

            if event in (sg.WINDOW_CLOSED, 'Cancelar'):
                should_exit_to_menu = True
                break

            if event == 'Salvar':
                validadores = {
                    "nome": Validador.validar_nome,
                    "cpf": Validador.validar_cpf,
                    "data_nasc": Validador.validar_data_nascimento,
                    "salario": lambda salario: "inválido"
                    if not salario.replace('.', '', 1).isdigit() or float(
                        salario) <= 0 else "válido"
                }

                campos_invalidos = self.validar_campos(values, list(validadores.keys()), validadores)

                if campos_invalidos:
                    sg.popup(
                        f"Preencha os seguintes campos obrigatórios ou corrija valores inválidos:"
                        f"{', '.join(campos_invalidos)}",
                        title="Erro",
                        background_color="#2C2F36",
                        text_color="white"
                    )
                    continue

                try:
                    salario = float(values['salario'])
                    if salario <= 0:
                        raise ValueError("O salário deve ser maior que zero.")
                except ValueError:
                    sg.popup("Erro no Salário: Insira um valor válido maior que zero.",
                             background_color="#2C2F36", text_color="white")
                    continue

                dados_vendedor = {
                    "nome": values["nome"].strip(),
                    "cpf": values["cpf"].strip(),
                    "data_nasc": values["data_nasc"].strip(),
                    "codigo": vendedor["codigo"],
                    "salario": float(values["salario"])
                }
                break

        window.close()
        return dados_vendedor, should_exit_to_menu
