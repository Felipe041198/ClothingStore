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
            [sg.Text('Tamanho:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.Combo(['P', 'M', 'G', 'GG'], key='tamanho', readonly=True)],
            [sg.Text('Cor:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.InputText(key='cor')],
            [sg.Text('Código gerado:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.Text(f'{codigo}', size=(15, 1), background_color="#2C2F36", text_color="white")],
            [sg.Text('Preço:', size=(15, 1), background_color="#2C2F36", text_color="white"),
             sg.InputText(key='preco')],
            [sg.Button('Cadastrar', size=(10, 1), button_color=("#FFFFFF", "#3E4349")),
             sg.Button('Voltar', size=(10, 1), button_color=("#FFFFFF", "#3E4349"))]
        ]

        window = sg.Window('Cadastro de Produto', layout, background_color="#2C2F36", finalize=True)
        produto = None
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
                campos_invalidos = self.validar_campos(values, ['nome', 'descricao',
                                                                'tamanho', 'cor', 'preco'])

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
                    preco = float(values['preco'])
                    if preco <= 0:
                        raise ValueError("O preço deve ser maior que zero.")
                except ValueError:
                    sg.popup("Preço inválido! Insira um valor numérico maior que zero.",
                             title="Erro no Preço", background_color="#2C2F36", text_color="white")
                    continue

                produto = self.criar_produto(values, codigo)
                break

        window.close()
        return produto, should_exit_to_menu

    def criar_produto(self, values: dict, codigo: int) -> dict:
        tamanho = values['tamanho'].strip()
        if tamanho not in ['P', 'M', 'G', 'GG']:
            raise ValueError("Tamanho selecionado é inválido.")
        return {
            "nome": values['nome'].strip(),
            "descricao": values['descricao'].strip(),
            "tamanho": values['tamanho'].strip(),
            "cor": values['cor'].strip(),
            "codigo": codigo,
            "preco": float(values['preco'].strip())
        }

    def exibir_produto(self, produto: dict):
        preco = float(produto['preco']) if not isinstance(produto['preco'], float) else produto['preco']
        preco_formatado = f"R${preco:.2f}"

        layout = [
            [sg.Text("Detalhes do Produto", font=("Courier", 18, "bold"), text_color="white",
                     background_color="#2C2F36", justification='center', expand_x=True, pad=(0, 10))],
            [sg.Text("Nome:", font=("Arial", 12, "bold"), background_color="#2C2F36", text_color="white"),
             sg.Text(produto['nome'], font=("Arial", 12), background_color="#2C2F36", text_color="white")],
            [sg.Text("Código:", font=("Arial", 12, "bold"), background_color="#2C2F36", text_color="white"),
             sg.Text(produto['codigo'], font=("Arial", 12), background_color="#2C2F36", text_color="white")],
            [sg.Text("Descrição:", font=("Arial", 12, "bold"),
                     background_color="#2C2F36", text_color="white"),
             sg.Text(produto['descricao'], font=("Arial", 12),
                     background_color="#2C2F36", text_color="white")],
            [sg.Text("Tamanho:", font=("Arial", 12, "bold"), background_color="#2C2F36", text_color="white"),
             sg.Text(produto['tamanho'], font=("Arial", 12), background_color="#2C2F36", text_color="white")],
            [sg.Text("Cor:", font=("Arial", 12, "bold"), background_color="#2C2F36", text_color="white"),
             sg.Text(produto['cor'], font=("Arial", 12), background_color="#2C2F36", text_color="white")],
            [sg.Text("Preço:", font=("Arial", 12, "bold"), background_color="#2C2F36", text_color="white"),
             sg.Text(preco_formatado, font=("Arial", 12), background_color="#2C2F36", text_color="white")],
            [sg.Button('OK', button_color=("#FFFFFF", "#3E4349"), size=(10, 1))]
        ]
        sg.Window("Detalhes do Produto", layout, background_color="#2C2F36").read(close=True)

    def exibir_lista_produtos(self, produtos: List[dict]):
        header = ['CÓDIGO', 'NOME', 'DESCRIÇÃO', 'TAMANHO', 'COR', 'PREÇO']
        data = [
            [p['codigo'], p['nome'], p['descricao'], p['tamanho'], p['cor'], f"R${p['preco']:.2f}"]
            for p in produtos
        ]

        layout = [
            [sg.Text("Lista de Produtos", font=("Courier", 18, "bold"), text_color="white",
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
                        col_widths=[8, 20, 30, 10, 10, 12],
                        justification='center',
                        row_height=35,
                        enable_events=True
                    )]],
                    element_justification='center',
                    expand_x=True
                )
            ],
            [sg.Button("Voltar", button_color=("#FFFFFF", "#3E4349"))]
        ]

        sg.Window(
            "Produtos",
            layout,
            background_color="#2C2F36",
            size=(900, 500),
            resizable=True
        ).read(close=True)

    def editar_dados_produto(self, dados_atual: dict) -> tuple[dict | None, bool]:
        layout = [
            [sg.Text('Editar Produto', background_color="#2C2F36", text_color="#FFFFFF")],
            [sg.Text('Nome:', size=(15, 1), background_color="#2C2F36", text_color="#FFFFFF"),
             sg.InputText(default_text=dados_atual.get('nome', ''), key='nome')],
            [sg.Text('Descrição:', size=(15, 1), background_color="#2C2F36", text_color="#FFFFFF"),
             sg.InputText(default_text=dados_atual.get('descricao', ''), key='descricao')],
            [sg.Text('Preço:', size=(15, 1), background_color="#2C2F36", text_color="#FFFFFF"),
             sg.InputText(default_text=dados_atual.get('preco', ''), key='preco')],
            [sg.Text('Tamanho:', size=(15, 1), background_color="#2C2F36", text_color="#FFFFFF"),
             sg.Combo(['P', 'M', 'G', 'GG'], default_value=dados_atual.get('tamanho', ''), key='tamanho',
                      readonly=True)],
            [sg.Text('Cor:', size=(15, 1), background_color="#2C2F36", text_color="#FFFFFF"),
             sg.InputText(default_text=dados_atual.get('cor', ''), key='cor')],
            [sg.Button('Salvar', button_color=("#FFFFFF", "#3E4349")),
             sg.Button('Cancelar', button_color=("#FFFFFF", "#FF0000"))]
        ]
        window = sg.Window('Editar Produto', layout, background_color="#2C2F36")

        should_exit_to_menu = False

        while True:
            event, values = window.read()

            if event in (sg.WIN_CLOSED, 'Cancelar'):
                dados_alterados = any(
                    values[k] != str(dados_atual.get(k, '')) for k in ['nome', 'descricao',
                                                                       'preco', 'tamanho', 'cor']
                )

                if dados_alterados:
                    if sg.popup_yes_no("Você alterou dados. Deseja descartar as mudanças?") != 'Yes':
                        continue

                should_exit_to_menu = True
                break

            if event == 'Salvar':
                campos_invalidos = self.validar_campos(values, ['nome', 'descricao',
                                                                'tamanho', 'cor', 'preco'])

                if campos_invalidos:
                    sg.popup(
                        f"Preencha os seguintes campos obrigatórios ou corrija valores inválidos: "
                        f"{', '.join(campos_invalidos)}",
                        title="Erro",
                        background_color="#2C2F36",
                        text_color="white"
                    )
                    continue

                try:
                    preco = float(values['preco'])
                    if preco <= 0:
                        raise ValueError("O preço deve ser maior que zero.")
                except ValueError:
                    sg.popup("Preço inválido! Insira um valor numérico maior que zero.",
                             title="Erro no Preço", background_color="#2C2F36", text_color="white")
                    continue

                novos_dados = {k: values[k] for k in ['nome', 'descricao', 'preco', 'tamanho', 'cor']}
                novos_dados['codigo'] = dados_atual.get('codigo')
                window.close()
                return novos_dados, should_exit_to_menu

        window.close()
        return None, should_exit_to_menu

    def destaque_campos_invalidos(self, window, campos):
        for campo in campos:
            window[campo].update(background_color='red')
