import PySimpleGUI as sg
from src.view.abstract_tela_registro import AbstractTelaRelatorio
from src.utils.enum_tipo_cadastro import TipoCadastro


class TelaRelatorio(AbstractTelaRelatorio):
    def __init__(self):
        super().__init__(tipo_cadastro=TipoCadastro.PEDIDO)

    def exibir_ultima_compra(self, venda: dict):
        layout = [
            [sg.Text("Última Compra do Cliente", font=("Courier", 18, "bold"), text_color="white",
                     background_color="#2C2F36", justification="center", expand_x=True)],
            [sg.Text(f"Cliente: {venda['cliente_nome']}", background_color="#2C2F36", text_color="white")],
            [sg.Text(f"CPF: {venda['cliente_cpf']}", background_color="#2C2F36", text_color="white")],
            [sg.Text(f"Data da Venda: {venda['data_venda']}", background_color="#2C2F36", text_color="white")],
            [sg.Text("Produtos Comprados:", background_color="#2C2F36", text_color="white")],
            [
                sg.Table(
                    values=[
                        [produto['codigo'], produto['nome'], produto['quantidade'], f"R$ {produto['valor']:.2f}"]
                        for produto in venda['produtos']
                    ],
                    headings=["Código", "Nome", "Quantidade", "Valor"],
                    num_rows=min(len(venda['produtos']), 10),
                    background_color="#2C2F36",
                    header_background_color="#007ACC",
                    text_color="white",
                    alternating_row_color="#3E4349",
                    justification="center",
                    auto_size_columns=True,
                )
            ],
            [sg.Text(f"Valor Total: R$ {venda['valor_total']:.2f}", background_color="#2C2F36", text_color="white")],
            [sg.Button("OK", size=(10, 1), button_color=("#FFFFFF", "#3E4349"))],
        ]

        sg.Window("Última Compra", layout, background_color="#2C2F36", finalize=True).read(close=True)

    def exibir_ultima_venda(self, venda: dict):
        layout = [
            [sg.Text("Última Venda do Vendedor", font=("Courier", 18, "bold"), text_color="white",
                     background_color="#2C2F36", justification="center", expand_x=True)],
            [sg.Text(f"Vendedor: {venda['vendedor_nome']}", background_color="#2C2F36", text_color="white")],
            [sg.Text(f"CPF: {venda['vendedor_cpf']}", background_color="#2C2F36", text_color="white")],
            [sg.Text(f"Cliente: {venda['cliente_nome']}", background_color="#2C2F36", text_color="white")],
            [sg.Text(f"Data da Venda: {venda['data_venda']}", background_color="#2C2F36", text_color="white")],
            [sg.Text("Produtos Vendidos:", background_color="#2C2F36", text_color="white")],
            [
                sg.Table(
                    values=[
                        [produto['codigo'], produto['nome'], produto['quantidade'], f"R$ {produto['valor']:.2f}"]
                        for produto in venda['produtos']
                    ],
                    headings=["Código", "Nome", "Quantidade", "Valor"],
                    num_rows=min(len(venda['produtos']), 10),
                    background_color="#2C2F36",
                    header_background_color="#007ACC",
                    text_color="white",
                    alternating_row_color="#3E4349",
                    justification="center",
                    auto_size_columns=True,
                )
            ],
            [sg.Text(f"Valor Total: R$ {venda['valor_total']:.2f}", background_color="#2C2F36", text_color="white")],
            [sg.Button("OK", size=(10, 1), button_color=("#FFFFFF", "#3E4349"))],
        ]

        sg.Window("Última Venda", layout, background_color="#2C2F36", finalize=True).read(close=True)

    def mostrar_relatorio_vendas(self, relatorio: dict):
        layout = [
            [sg.Text("Relatório de Vendas", font=("Courier", 18, "bold"), text_color="white",
                     background_color="#2C2F36", justification="center", expand_x=True)],
            [sg.Text(f"Total de Vendas no Período: R$ {relatorio['total_vendas_periodo']:.2f}",
                     background_color="#2C2F36", text_color="white", font=("Courier", 14, "bold"))],
            [
                sg.Table(
                    values=[
                        [
                            venda['data_venda'], venda['cliente_nome'], venda['cliente_cpf'],
                            venda['vendedor_nome'], venda['vendedor_cpf'], f"R$ {venda['valor_total']:.2f}"
                        ]
                        for venda in relatorio['vendas']
                    ],
                    headings=["Data", "Cliente", "CPF Cliente", "Vendedor", "CPF Vendedor", "Total"],
                    num_rows=15,
                    header_background_color="#007ACC",
                    text_color="white",
                    alternating_row_color="#3E4349",
                    background_color="#2C2F36",
                    justification="center",
                    auto_size_columns=True,
                )
            ],
            [sg.Button("OK", size=(10, 1), button_color=("#FFFFFF", "#3E4349"))],
        ]

        sg.Window("Relatório de Vendas", layout, background_color="#2C2F36", size=(900, 600), finalize=True).read(
            close=True)

    def mostrar_relatorio_por_tipo_cliente(self, relatorio_por_tipo: dict):
        for tipo, vendas in relatorio_por_tipo.items():
            titulo = f"Categoria: {tipo}" if vendas else f"Categoria: {tipo} (Sem registro)"
            layout = [
                [sg.Text(titulo, font=("Courier", 18, "bold"), text_color="white",
                         background_color="#2C2F36", justification="center", expand_x=True)],
                [
                    sg.Table(
                        values=[
                            [venda['cliente_nome'], venda['vendedor_nome'], f"R$ {venda['valor_total']:.2f}"]
                            for venda in vendas
                        ],
                        headings=["Cliente", "Vendedor", "Total"],
                        num_rows=min(len(vendas), 10),
                        background_color="#2C2F36",
                        header_background_color="#007ACC",
                        text_color="white",
                        alternating_row_color="#3E4349",
                        justification="center",
                    )
                ] if vendas else [sg.Text("Nenhuma venda registrada.", background_color="#2C2F36", text_color="white")],
                [sg.Button("OK", size=(10, 1), button_color=("#FFFFFF", "#3E4349"))],
            ]

            sg.Window(f"Relatório - {tipo}", layout, background_color="#2C2F36", finalize=True).read(close=True)
