import PySimpleGUI as sg
from typing import List, Any
from src.utils.enum_tipo_cadastro import TipoCadastro
from src.view.abstract_gui_tela_cadastro import AbstractTelaCadastro


class TelaVendedores(AbstractTelaCadastro):
    def __init__(self):
        super().__init__(tipo_cadastro=TipoCadastro.VENDEDOR)

    def obter_dados_vendedor(self, codigo: int, pesquisa_vendedor_callback) -> (dict[str, int | float | Any], bool):
        layout = [
            [sg.Text('CADASTRO DE VENDEDOR',
                     font=("Courier", 24, "bold"),
                     text_color="white",
                     background_color="#2C2F36",
                     justification='center',
                     expand_x=True)],
            [sg.Text('CPF:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.InputText(key='cpf')],
            [sg.Text('Nome:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.InputText(key='nome')],
            [sg.Text('Data de Nascimento:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.InputText(key='data_nasc')],
            [sg.Text('Código gerado:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.Text(f'{codigo}', size=(15, 1), background_color="#2C2F36", text_color="white")],
            [sg.Text('Salário:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.InputText(key='salario')],
            [sg.Text('', size=(1, 1), background_color="#2C2F36")],
            [sg.Button('Cadastrar', size=(10, 1), button_color=("#FFFFFF", "#3E4349"), disabled=True),
             sg.Button('Voltar', size=(10, 1), button_color=("#FFFFFF", "#3E4349"))]
        ]

        window = sg.Window('Cadastro de Vendedor', layout, background_color="#2C2F36", finalize=True)

        window['cpf'].bind('<KeyRelease>', 'focused')
        window['nome'].bind('<KeyRelease>', 'focused')
        window['data_nasc'].bind('<KeyRelease>', 'focused')

        dados_vendedor = {}
        should_exit_to_menu = False

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == 'Voltar':
                if not any(values.values()):
                    should_exit_to_menu = True
                    break
                else:
                    if self.confirmar_acoes(
                            "Há informações preenchidas. Tem certeza que deseja voltar? As informações serão perdidas."):
                        should_exit_to_menu = True
                        break

            if event.endswith('focused'):
                _, _, _ = self.validar_campos(values, window)
                all_filled = all(values[key] for key in ['cpf', 'nome', 'data_nasc', 'salario'])
                window['Cadastrar'].update(disabled=not all_filled)

            elif event == 'Cadastrar':
                validacao_cpf, validacao_nome, validacao_data_nasc = self.validar_campos(values, window)

                # Verificar se o vendedor já está cadastrado
                vendedor_existente = pesquisa_vendedor_callback(validacao_cpf)
                if vendedor_existente:
                    if self.confirmar_acoes(
                            "CPF já cadastrado. Deseja visualizar o cadastro existente ou alterar o CPF para continuar?"
                    ):
                        self.exibir_vendedor(vendedor_existente.to_dict())
                        continue
                    else:
                        continue

                dados_vendedor = {
                    "cpf": validacao_cpf,
                    "nome": validacao_nome,
                    "data_nasc": validacao_data_nasc,
                    "codigo": codigo,
                    "salario": float(values['salario']) if values['salario'] else 0.0
                }
                break

        window.close()

        return dados_vendedor, should_exit_to_menu

    def exibir_vendedor(self, vendedor: dict):
        salario_formatado = f"R${vendedor['salario']:.2f}".replace('.', ',')
        sg.theme_background_color("#2C2F36")

        layout = [
            [sg.Text("Detalhes do vendedor", font=("Courier", 18, "bold"), text_color="white",
                     background_color="#2C2F36", justification='center', expand_x=True, pad=(0, 10))],
            [sg.Text(f"Nome:", font=("Arial", 12, "bold"), background_color="#2C2F36", text_color="white"),
             sg.Text(f"{vendedor['nome']}", font=("Arial", 12), background_color="#2C2F36", text_color="white")],
            [sg.Text(f"Código:", font=("Arial", 12, "bold"), background_color="#2C2F36", text_color="white"),
             sg.Text(f"{vendedor['codigo']}", font=("Arial", 12), background_color="#2C2F36", text_color="white")],
            [sg.Text(f"CPF:", font=("Arial", 12, "bold"), background_color="#2C2F36", text_color="white"),
             sg.Text(f"{vendedor['cpf']}", font=("Arial", 12), background_color="#2C2F36", text_color="white")],
            [sg.Text(f"Data de nascimento:", font=("Arial", 12, "bold"), background_color="#2C2F36",
                     text_color="white"),
             sg.Text(f"{vendedor['data_nasc']}", font=("Arial", 12), background_color="#2C2F36", text_color="white")],
            [sg.Text(f"Salário:", font=("Arial", 12, "bold"), background_color="#2C2F36", text_color="white"),
             sg.Text(f"{salario_formatado}", font=("Arial", 12), background_color="#2C2F36", text_color="white")],
            [sg.Text('', size=(1, 1), background_color="#2C2F36")],  # Espaçamento extra
            [sg.Button('Voltar', button_color=("#FFFFFF", "#3E4349"), mouseover_colors=("#FFFFFF", "#FF0000"),
                       size=(10, 1))]
        ]

        window = sg.Window("Detalhes do Vendedor", layout, background_color="#2C2F36")
        window.read()
        window.close()

    def exibir_vendedores(self, vendedores: List[dict]):
        header = ['CÓDIGO', 'NOME', 'CPF', 'DATA DE NASCIMENTO', 'SALÁRIO']
        data = [[vendedor['codigo'],
                 vendedor['nome'],
                 vendedor['cpf'],
                 vendedor['data_nasc'],
                 f"R${vendedor['salario']:.2f}".replace('.', ',')] for vendedor in vendedores]

        layout = [
            [sg.Text("Lista de Vendedores", font=("Courier", 18, "bold"), text_color="white",
                     background_color="#2C2F36", justification='center', expand_x=True)],
            [sg.HorizontalSeparator()],
            [sg.HorizontalSeparator(pad=(40, 0))],  # Espaçamento à esquerda da tabela
            [sg.Table(values=data,
                      headings=header,
                      auto_size_columns=False,
                      col_widths=[10, 20, 20, 25, 15],
                      justification='center',
                      num_rows=min(len(data), 20),
                      key='-TABLE-',
                      background_color="#2C2F36",
                      text_color="white",
                      header_background_color="#007ACC",
                      header_font=("Courier", 12, "bold"),
                      header_text_color="white",
                      row_height=25,
                      alternating_row_color='#313640',
                      display_row_numbers=False,
                      vertical_scroll_only=False,
                      enable_click_events=True,
                      expand_x=True,
                      expand_y=True)],
            [sg.HorizontalSeparator(pad=(40, 0))],  # Espaçamento à direita da tabela
            [sg.VerticalSeparator(pad=(0, 20))],
            [sg.Button("Voltar", button_color=("#FFFFFF", "#3E4349"), pad=((0, 0), (10, 0)))]
        ]

        window = sg.Window("Vendedores", layout, background_color="#2C2F36", size=(900, 600), resizable=True)
        window.read()
        window.close()

    def editar_dados_vendedor(self, vendedor: dict, pesquisa_vendedor_callback) -> (dict, bool):
        layout = [
            [sg.Text('Editar Vendedor', font=("Courier", 18, "bold"), text_color="white",
                     background_color="#2C2F36", justification='center', expand_x=True, pad=(0, 10))],
            [sg.Text('Código:', font=("Arial", 12, "bold"), size=(15, 1), background_color="#2C2F36",
                     text_color="white"), sg.Text(f"{vendedor['codigo']}", font=("Arial", 12),
                                                  background_color="#2C2F36", text_color="white")],
            [sg.Text('Nome:', font=("Arial", 12, "bold"), size=(15, 1), background_color="#2C2F36",
                     text_color="white"), sg.InputText(key='nome', default_text=vendedor['nome'])],
            [sg.Text('CPF:', font=("Arial", 12, "bold"), size=(15, 1), background_color="#2C2F36",
                     text_color="white"), sg.InputText(key='cpf', default_text=vendedor['cpf'])],
            [sg.Text('Data de nascimento:', font=("Arial", 12, "bold"), size=(15, 1), background_color="#2C2F36",
                     text_color="white"), sg.InputText(key='data_nasc', default_text=vendedor['data_nasc'])],
            [sg.Text('Salário:', font=("Arial", 12, "bold"), size=(15, 1), background_color="#2C2F36",
                     text_color="white"), sg.InputText(key='salario', default_text=f"{vendedor['salario']:.2f}")],
            [sg.Text('', size=(1, 1), background_color="#2C2F36")],
            [sg.Button('OK', font=("Arial", 12), size=(10, 1), button_color=("#FFFFFF", "#3E4349"), disabled=True),
             sg.Button('Cancelar', font=("Arial", 12), button_color=("#FFFFFF", "#3E4349"),
                       mouseover_colors=("#FFFFFF", "#FF0000"), size=(10, 1))]
        ]

        window = sg.Window('Editar Vendedor', layout, background_color="#2C2F36", finalize=True)
        should_exit_to_menu = False
        dados_vendedor = {}

        window['cpf'].bind('<FocusOut>', '+FOCUS_OUT+')

        def has_changes(values):
            validacao_cpf, validacao_nome, validacao_data_nasc = self.validar_campos(values, window)
            return (
                    validacao_cpf != vendedor['cpf'] or
                    validacao_nome != vendedor['nome'] or
                    validacao_data_nasc != vendedor['data_nasc'] or
                    (values['salario'] and float(values['salario']) != vendedor['salario'])
            )

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                if not has_changes(values):
                    should_exit_to_menu = True
                    break
                else:
                    if self.confirmar_alteracoes_editar():
                        should_exit_to_menu = True
                        break

            elif event == 'OK':
                validacao_cpf, validacao_nome, validacao_data_nasc = self.validar_campos(values, window)

                # Verificar se o CPF foi alterado e se já existe
                if validacao_cpf != vendedor['cpf']:
                    vendedor_existente = pesquisa_vendedor_callback(validacao_cpf)
                    if vendedor_existente:
                        sg.popup("CPF já cadastrado em outro vendedor. Por favor, insira um CPF diferente.",
                                 background_color='#2C2F36', text_color='#FFFFFF')
                        continue

                dados_vendedor = {
                    "cpf": validacao_cpf,
                    "nome": validacao_nome,
                    "data_nasc": validacao_data_nasc,
                    "salario": float(values['salario']) if values['salario'].strip() else vendedor["salario"]
                }
                break

            elif event.endswith('+FOCUS_OUT+'):
                # Aqui podemos validar o CPF assim que perdemos o foco
                cpf_novo = values['cpf']
                if cpf_novo != vendedor['cpf']:  # Apenas verifica se o CPF foi alterado
                    vendedor_existente = pesquisa_vendedor_callback(cpf_novo)
                    if vendedor_existente:
                        sg.popup("CPF já cadastrado em outro vendedor. Por favor, insira um CPF diferente.",
                                 background_color='#2C2F36', text_color='#FFFFFF')
                        window['cpf'].update(background_color='red')

            elif event.endswith('+UPDATE+'):
                _, _, _ = self.validar_campos(values, window)
                all_filled = all(values[key].strip() for key in ['cpf', 'nome', 'data_nasc', 'salario'])
                window['OK'].update(disabled=not (has_changes(values) and all_filled))

        window.close()
        return dados_vendedor, should_exit_to_menu
