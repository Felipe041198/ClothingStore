import PySimpleGUI as sg
from typing import List
from src.utils.enum_tipo_cadastro import TipoCadastro
from src.utils.enum_categoria_cliente import CategoriaCliente
from src.view.abstract_gui_tela_cadastro import AbstractTelaCadastro


class TelaClientes(AbstractTelaCadastro):
    def __init__(self):
        super().__init__(tipo_cadastro=TipoCadastro.CLIENTE)

    def obter_dados_cliente(self, codigo: int) -> tuple[dict | None, bool]:
        layout = [
            [sg.Text('CADASTRO DE CLIENTE', font=("Courier", 24, "bold"), text_color="white",
                     background_color="#2C2F36", justification='center', expand_x=True)],
            [sg.Text('Nome:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.InputText(key='nome')],
            [sg.Text('CPF:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.InputText(key='cpf')],
            [sg.Text('Data de Nascimento (dd/mm/yyyy):', size=(25, 1),
                     background_color="#2C2F36", text_color="white"),
             sg.InputText(key='data_nasc')],
            [sg.Text('Código gerado:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.Text(f'{codigo}', size=(15, 1), background_color="#2C2F36", text_color="white")],
            [sg.Text('Categoria:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.Combo(
                 [categoria.nome for categoria in CategoriaCliente],
                 key='categoria',
                 readonly=True
             )],
            [sg.Button('Cadastrar', size=(10, 1), button_color=("#FFFFFF", "#3E4349")),
             sg.Button('Voltar', size=(10, 1), button_color=("#FFFFFF", "#3E4349"))]
        ]

        window = sg.Window('Cadastro de Cliente', layout, background_color="#2C2F36", finalize=True)
        dados_cliente = None
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
                campos_invalidos = self.obter_campos_invalidos(values, contexto='cliente')

                if campos_invalidos:
                    sg.popup(
                        f"Preencha os seguintes campos obrigatórios ou corrija valores inválidos:"
                        f"{', '.join(campos_invalidos)}",
                        title="Erro",
                        background_color="#2C2F36",
                        text_color="white"
                    )
                    continue

                categoria = next(
                    (categoria for categoria in CategoriaCliente if categoria.nome == values['categoria']), None
                )

                if not categoria:
                    sg.popup(
                        "Selecione uma categoria válida.",
                        title="Erro",
                        background_color="#2C2F36",
                        text_color="white"
                    )
                    continue

                dados_cliente = {
                    "nome": values["nome"].strip(),
                    "cpf": values["cpf"].strip(),
                    "data_nasc": values["data_nasc"],
                    "codigo": codigo,
                    "categoria": categoria
                }
                break

        window.close()
        return dados_cliente, should_exit_to_menu

    def exibir_cliente(self, cliente: dict):
        layout = [
            [sg.Text("Detalhes do Cliente", font=("Courier", 18, "bold"), text_color="white",
                     background_color="#2C2F36", justification='center', expand_x=True, pad=(0, 10))],
            [sg.Text("Nome:", font=("Arial", 12, "bold"), background_color="#2C2F36", text_color="white"),
             sg.Text(cliente['nome'], font=("Arial", 12), background_color="#2C2F36", text_color="white")],
            [sg.Text("CPF:", font=("Arial", 12, "bold"), background_color="#2C2F36", text_color="white"),
             sg.Text(cliente['cpf'], font=("Arial", 12), background_color="#2C2F36", text_color="white")],
            [sg.Text("Data de Nascimento:", font=("Arial", 12, "bold"),
                     background_color="#2C2F36", text_color="white"),
             sg.Text(cliente['data_nasc'], font=("Arial", 12), background_color="#2C2F36", text_color="white")],
            [sg.Text("Código:", font=("Arial", 12, "bold"), background_color="#2C2F36", text_color="white"),
             sg.Text(cliente['codigo'], font=("Arial", 12), background_color="#2C2F36", text_color="white")],
            [sg.Text("Categoria:", font=("Arial", 12, "bold"), background_color="#2C2F36", text_color="white"),
             sg.Text(cliente['categoria'].nome, font=("Arial", 12), background_color="#2C2F36", text_color="white")],
            [sg.Button('OK', button_color=("#FFFFFF", "#3E4349"), size=(10, 1))]
        ]

        sg.Window("Detalhes do Cliente", layout, background_color="#2C2F36").read(close=True)

    def exibir_clientes(self, clientes: List[dict]):
        header = ['CÓDIGO', 'NOME', 'CPF', 'DATA DE NASCIMENTO', 'CATEGORIA']
        data = [
            [cliente['codigo'],
             cliente['nome'],
             cliente['cpf'],
             cliente['data_nasc'],
             cliente['categoria'].nome]
            for cliente in clientes
        ]

        layout = [
            [sg.Text("Lista de Clientes", font=("Courier", 18, "bold"), text_color="white",
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
            "Clientes",
            layout,
            background_color="#2C2F36",
            size=(900, 500),
            resizable=True
        ).read(close=True)

    def editar_dados_cliente(self, cliente: dict) -> tuple[dict | None, bool]:
        layout = [
            [sg.Text('EDITAR CLIENTE', font=("Courier", 18, "bold"),
                     text_color="white", background_color="#2C2F36", justification='center', expand_x=True)],
            [sg.Text('Código:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.Text(f"{cliente['codigo']}", size=(15, 1), background_color="#2C2F36", text_color="white")],
            [sg.Text('Nome:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.InputText(default_text=cliente['nome'], key='nome')],
            [sg.Text('CPF:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.InputText(default_text=cliente['cpf'], key='cpf')],
            [sg.Text('Data de Nascimento:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.InputText(default_text=cliente['data_nasc'], key='data_nasc')],
            [sg.Text('Categoria:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.Combo(
                 [categoria.nome for categoria in CategoriaCliente],
                 default_value=cliente['categoria'].nome,
                 key='categoria',
                 readonly=True
             )],
            [sg.Button('Salvar', button_color=("#FFFFFF", "#3E4349"), size=(10, 1)),
             sg.Button('Cancelar', button_color=("#FFFFFF", "#FF0000"), size=(10, 1))]
        ]

        window = sg.Window('Editar Cliente', layout, background_color="#2C2F36", finalize=True)
        should_exit_to_menu = False
        dados_cliente = None

        while True:
            event, values = window.read()

            if event in (sg.WINDOW_CLOSED, 'Cancelar'):
                should_exit_to_menu = True
                break

            if event == 'Salvar':
                campos_invalidos = self.obter_campos_invalidos(values, contexto='cliente')

                if campos_invalidos:
                    sg.popup(
                        f"Preencha os seguintes campos obrigatórios ou corrija valores inválidos:"
                        f"{', '.join(campos_invalidos)}",
                        title="Erro",
                        background_color="#2C2F36",
                        text_color="white"
                    )
                    continue

                categoria = next(
                    (categoria for categoria in CategoriaCliente if categoria.nome == values['categoria']), None
                )

                if not categoria:
                    sg.popup(
                        "Selecione uma categoria válida.",
                        title="Erro",
                        background_color="#2C2F36",
                        text_color="white"
                    )
                    continue

                dados_cliente = {
                    "nome": values["nome"].strip(),
                    "cpf": values["cpf"].strip(),
                    "data_nasc": values["data_nasc"].strip(),
                    "codigo": cliente["codigo"],
                    "categoria": categoria
                }
                break

        window.close()
        return dados_cliente, should_exit_to_menu
