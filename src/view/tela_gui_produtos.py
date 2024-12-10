import PySimpleGUI as sg
from typing import List
from src.utils.enum_tipo_cadastro import TipoCadastro
from src.view.abstract_gui_tela_cadastro import AbstractTelaCadastro


class TelaProdutos(AbstractTelaCadastro):
    def __init__(self):
        super().__init__(tipo_cadastro=TipoCadastro.PRODUTO)

    def obter_dados_produto(self, codigo: int) -> tuple[dict | None, bool]:
        layout = [
            [sg.Text('CADASTRO DE PRODUTO', font=("Courier", 24, "bold"), text_color="white",
                     background_color="#2C2F36", justification='center', expand_x=True)],
            [sg.Text('Nome do Produto:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.InputText(key='nome')],
            [sg.Text('Descrição:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.InputText(key='descricao')],
            [sg.Text('Tamanhos:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.Checkbox("P", key='tamanho_P', background_color="#2C2F36", text_color="white"),
             sg.Checkbox("M", key='tamanho_M', background_color="#2C2F36", text_color="white"),
             sg.Checkbox("G", key='tamanho_G', background_color="#2C2F36", text_color="white")],
            [sg.Text('Cor:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.InputText(key='cor')],
            [sg.Text('Código gerado:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.Text(f'{codigo}', size=(15, 1), background_color="#2C2F36", text_color="white")],
            [sg.Text('Preço:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.InputText(key='preco')],
            [sg.Text('', size=(1, 1), background_color="#2C2F36")],
            [sg.Button('Cadastrar', size=(10, 1), button_color=("#FFFFFF", "#3E4349"), disabled=True),
             sg.Button('Voltar', size=(10, 1), button_color=("#FFFFFF", "#3E4349"))]
        ]

        window = sg.Window('Cadastro de Produto', layout, background_color="#2C2F36", finalize=True)

        produto = None
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
                            "Há informações preenchidas. Tem certeza que deseja voltar? As informações serão perdidas."
                    ):
                        should_exit_to_menu = True
                        break

            tamanhos_validos = self.verificar_tamanhos_selecionados(values)
            all_filled = (
                    all(values[key].strip() for key in ['nome', 'descricao', 'cor', 'preco']) and tamanhos_validos
            )
            window['Cadastrar'].update(disabled=not all_filled)

            if event == 'Cadastrar':
                tamanhos_selecionados = []
                if values['tamanho_P']:
                    tamanhos_selecionados.append("P")
                if values['tamanho_M']:
                    tamanhos_selecionados.append("M")
                if values['tamanho_G']:
                    tamanhos_selecionados.append("G")

                produto = {
                    "nome": values['nome'],
                    "descricao": values['descricao'],
                    "tamanho": tamanhos_selecionados,
                    "cor": values['cor'],
                    "codigo": codigo,
                    "preco": float(values['preco']) if values['preco'] else 0.0
                }
                break

        window.close()
        return produto, should_exit_to_menu

    @staticmethod
    def verificar_tamanhos_selecionados(values: dict) -> bool:
        return values['tamanho_P'] or values['tamanho_M'] or values['tamanho_G']

    def exibir_produto(self, produto: dict):
        preco_formatado = f"R${produto['preco']:.2f}".replace('.', ',')
        tamanhos_formatados = ", ".join(produto['tamanho']) if produto['tamanho'] else "Nenhum"
        sg.theme_background_color("#2C2F36")

        layout = [
            [sg.Text("Detalhes do Produto", font=("Courier", 18, "bold"), text_color="white",
                     background_color="#2C2F36", justification='center', expand_x=True, pad=(0, 10))],
            [sg.Text("Nome:", font=("Arial", 12, "bold"), background_color="#2C2F36", text_color="white"),
             sg.Text(f"{produto['nome']}", font=("Arial", 12),
                     background_color="#2C2F36", text_color="white")],
            [sg.Text("Código:", font=("Arial", 12, "bold"), background_color="#2C2F36", text_color="white"),
             sg.Text(f"{produto['codigo']}", font=("Arial", 12),
                     background_color="#2C2F36", text_color="white")],
            [sg.Text("Descrição:", font=("Arial", 12, "bold"), background_color="#2C2F36", text_color="white"),
             sg.Text(f"{produto['descricao']}", font=("Arial", 12),
                     background_color="#2C2F36", text_color="white")],
            [sg.Text("Tamanho:", font=("Arial", 12, "bold"), background_color="#2C2F36",
                     text_color="white"),
             sg.Text(f"{produto['tamanho']}", font=("Arial", 12),
                     background_color="#2C2F36", text_color="white")],
            [sg.Text("Cor:", font=("Arial", 12, "bold"), background_color="#2C2F36", text_color="white"),
             sg.Text(f"{produto['cor']}", font=("Arial", 12),
                     background_color="#2C2F36", text_color="white")],
            [sg.Text("Preço:", font=("Arial", 12, "bold"), background_color="#2C2F36", text_color="white"),
             sg.Text(f"{preco_formatado}", font=("Arial", 12),
                     background_color="#2C2F36", text_color="white")],
            [sg.Text('', size=(1, 1), background_color="#2C2F36")],  # Espaçamento extra
            [sg.Button('Voltar', button_color=("#FFFFFF", "#3E4349"), mouseover_colors=("#FFFFFF", "#FF0000"),
                       size=(10, 1))]
        ]

        window = sg.Window("Detalhes do Produto", layout, background_color="#2C2F36")
        window.read()
        window.close()

    def busca_produto(self) -> int | None:
        try:
            codigo = int(input("Digite o código do produto que deseja buscar: "))
            return codigo
        except ValueError:
            print("Código inválido. Por favor, insira um número inteiro.")
            return None

    def exibir_lista_produtos(self, produtos: List[dict]):
        header = ['CÓDIGO', 'NOME', 'DESCRIÇÃO', 'TAMANHO', 'COR', 'PREÇO']
        data = [[produto['codigo'],
                 produto['nome'],
                 produto['descricao'],
                 produto['tamanho'],
                 produto['cor'],
                 f"R${produto['preco']:.2f}".replace('.', ',')] for produto in produtos]

        layout = [
            [sg.Text("Lista de Produtos", font=("Courier", 18, "bold"), text_color="white",
                     background_color="#2C2F36", justification='center', expand_x=True)],
            [sg.HorizontalSeparator()],
            [sg.HorizontalSeparator(pad=(40, 0))],  # Espaçamento à esquerda da tabela
            [sg.Table(values=data,
                      headings=header,
                      auto_size_columns=False,
                      col_widths=[10, 20, 30, 15, 10, 15],
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

        window = sg.Window("Produtos", layout, background_color="#2C2F36", size=(900, 600), resizable=True)
        window.read()
        window.close()

    def editar_dados_produto(self, produto: dict) -> dict:
        layout = [
            [sg.Text('Editar Produto', font=("Courier", 18, "bold"), text_color="white",
                     background_color="#2C2F36", justification='center', expand_x=True, pad=(0, 10))],
            [sg.Text('Código:', size=(15, 1), background_color="#2C2F36",
                     text_color="white"),
             sg.Text(f"{produto['codigo']}", background_color="#2C2F36", text_color="white")],
            [sg.Text('Nome:', size=(15, 1), background_color="#2C2F36",
                     text_color="white"), sg.InputText(key='nome', default_text=produto['nome'])],
            [sg.Text('Descrição:', size=(15, 1), background_color="#2C2F36",
                     text_color="white"), sg.InputText(key='descricao', default_text=produto['descricao'])],
            [sg.Text('Tamanho:', size=(15, 1), background_color="#2C2F36",
                     text_color="white"), sg.InputText(key='tamanho', default_text=produto['tamanho'])],
            [sg.Text('Cor:', size=(15, 1), background_color="#2C2F36",
                     text_color="white"), sg.InputText(key='cor', default_text=produto['cor'])],
            [sg.Text('Preço:', size=(15, 1), background_color="#2C2F36",
                     text_color="white"), sg.InputText(key='preco', default_text=f"{produto['preco']:.2f}")],
            [sg.Text('', size=(1, 1), background_color="#2C2F36")],
            [sg.Button('OK', size=(10, 1), button_color=("#FFFFFF", "#3E4349"), disabled=True),
             sg.Button('Cancelar', size=(10, 1), button_color=("#FFFFFF", "#3E4349"))]
        ]

        window = sg.Window('Editar Produto', layout, background_color="#2C2F36", finalize=True)
        updated_produto = {}

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                break

            elif event == 'OK':
                updated_produto = {
                    "nome": values['nome'],
                    "descricao": values['descricao'],
                    "tamanho": values['tamanho'],
                    "cor": values['cor'],
                    "preco": float(values['preco']) if values['preco'] else produto["preco"]
                }
                break

        window.close()
        return updated_produto
