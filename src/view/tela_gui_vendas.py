import PySimpleGUI as sg
from typing import List, Dict
from src.utils.enum_tipo_cadastro import TipoCadastro
from src.view.abstract_gui_tela_cadastro import AbstractTelaCadastro


class TelaVendas(AbstractTelaCadastro):
    def __init__(self):
        super().__init__(tipo_cadastro=TipoCadastro.PEDIDO)

    def obter_dados_venda(self, clientes: List[Dict], vendedores: List[Dict], produtos: List[Dict]) -> Dict:
        layout_cliente_vendedor = [
            [sg.Text("Registrar Venda", font=("Courier", 24), text_color="white", background_color="#2C2F36",
                     justification="center", expand_x=True)],
            [sg.Text("", size=(1, 1), background_color="#2C2F36")],
            [sg.Text("Selecione o Cliente:", text_color="white", background_color="#2C2F36")],
            [sg.Combo([f"CPF: {cliente['cpf']} - Nome: {cliente['nome']}" for cliente in clientes],
                      key="cliente_selecionado", size=(50, 1), readonly=True)],
            [sg.Text("Ou digite o CPF para buscar:", text_color="white", background_color="#2C2F36")],
            [
                sg.InputText(key="cpf_cliente", size=(25, 1), background_color="#3E4349", text_color="white"),
                sg.Button("Buscar Cliente", key="buscar_cliente", button_color=("#FFFFFF", "#3E4349"))
            ],
            [sg.Text("", size=(1, 1), background_color="#2C2F36")],
            [sg.Text("Selecione o Vendedor:", text_color="white", background_color="#2C2F36")],
            [sg.Combo([f"CPF: {vendedor['cpf']} - Nome: {vendedor['nome']}" for vendedor in vendedores],
                      key="vendedor_selecionado", size=(50, 1), readonly=True)],
            [sg.Text("Ou digite o CPF para buscar:", text_color="white", background_color="#2C2F36")],
            [
                sg.InputText(key="cpf_vendedor", size=(25, 1), background_color="#3E4349", text_color="white"),
                sg.Button("Buscar Vendedor", key="buscar_vendedor", button_color=("#FFFFFF", "#3E4349"))
            ],
        ]

        layout_produtos_selecionados = [
            [sg.Text("", size=(1, 1), background_color="#2C2F36")],
            [sg.Text("Selecione os Produtos Desejados:", text_color="white", background_color="#2C2F36")],
            [sg.Listbox(values=[f"{produto['nome']} - Preço: R${produto['preco']:.2f}" for produto in produtos],
                        select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, size=(50, 10), key="produtos_selecionados",
                        background_color="#3E4349", text_color="white")],
            [sg.Button("Selecionar Quantidades", size=(25, 1), button_color=("#FFFFFF", "#3E4349")),
             sg.Button("Cancelar", size=(25, 1), button_color=("#FFFFFF", "#FF0000"))]
        ]

        janela = sg.Window("Registrar Venda", layout_cliente_vendedor + layout_produtos_selecionados,
                           background_color="#2C2F36", modal=True)

        cliente, vendedor, produtos_selecionados = None, None, []

        while True:
            event, values = janela.read()

            if event in (sg.WIN_CLOSED, "Cancelar"):
                janela.close()
                return {}

            if event == "buscar_cliente":
                cpf = values.get("cpf_cliente", "").strip()
                cliente_encontrado = next((f"CPF: {c['cpf']} - Nome: {c['nome']}" for c in clientes if c["cpf"] == cpf),
                                          None)
                if cliente_encontrado:
                    janela["cliente_selecionado"].update(cliente_encontrado)
                else:
                    sg.popup("Cliente não encontrado!", title="Erro", text_color="red", background_color="#2C2F36")

            elif event == "buscar_vendedor":
                cpf = values.get("cpf_vendedor", "").strip()
                vendedor_encontrado = next(
                    (f"CPF: {v['cpf']} - Nome: {v['nome']}" for v in vendedores if v["cpf"] == cpf),
                    None)
                if vendedor_encontrado:
                    janela["vendedor_selecionado"].update(vendedor_encontrado)
                else:
                    sg.popup("Vendedor não encontrado!", title="Erro", text_color="red", background_color="#2C2F36")

            elif event == "Selecionar Quantidades":
                cliente = values.get("cliente_selecionado")
                vendedor = values.get("vendedor_selecionado")
                produtos_selecionados = values.get("produtos_selecionados")

                if not cliente:
                    sg.popup("Selecione um cliente!", title="Erro", text_color="red", background_color="#2C2F36")
                    continue
                if not vendedor:
                    sg.popup("Selecione um vendedor!", title="Erro", text_color="red", background_color="#2C2F36")
                    continue
                if not produtos_selecionados:
                    sg.popup("Selecione pelo menos um produto!", title="Erro", text_color="red",
                             background_color="#2C2F36")
                    continue

                break

        janela.close()

        layout_quantidades = [
            [sg.Text("Informe as Quantidades:", font=("Courier", 20), text_color="white", background_color="#2C2F36",
                     justification="center", expand_x=True)],
            *[
                [sg.Text(produto, size=(40, 1), text_color="white", background_color="#2C2F36"),
                 sg.InputText(default_text="1", size=(5, 1), key=f"quantidade_{produto}",
                              background_color="#3E4349", text_color="white")]
                for produto in produtos_selecionados
            ],
            [sg.Button("Confirmar", size=(20, 1), button_color=("#FFFFFF", "#3E4349")),
             sg.Button("Cancelar", size=(20, 1), button_color=("#FFFFFF", "#FF0000"))]
        ]

        janela_quantidade = sg.Window("Selecionar Quantidades", layout_quantidades, background_color="#2C2F36",
                                      modal=True)

        produtos_final = []
        while True:
            event, values = janela_quantidade.read()

            if event in (sg.WIN_CLOSED, "Cancelar"):
                janela_quantidade.close()
                return {}

            elif event == "Confirmar":
                try:
                    for produto in produtos_selecionados:
                        quantidade = int(values[f"quantidade_{produto}"])
                        produto_dados = next(
                            p for p in produtos if f"{p['nome']} - Preço: R${p['preco']:.2f}" == produto)
                        produto_dados["quantidade"] = quantidade
                        produtos_final.append(produto_dados)
                    break
                except ValueError:
                    sg.popup("Informe quantidades válidas para todos os produtos.", title="Erro", text_color="red",
                             background_color="#2C2F36")

        janela_quantidade.close()

        return {
            "cliente": next(c for c in clientes if f"CPF: {c['cpf']} - Nome: {c['nome']}" == cliente),
            "vendedor": next(v for v in vendedores if f"CPF: {v['cpf']} - Nome: {v['nome']}" == vendedor),
            "produtos": produtos_final
        }

    def seleciona_vendas(self, vendas: List[Dict]) -> int:
        layout = [
            [sg.Text("Selecione uma Venda para Excluir", font=("Courier", 24), text_color="white",
                     background_color="#2C2F36", justification="center", expand_x=True)],
            [sg.Listbox(values=[
                f"Venda {i + 1}: Cliente: {venda['cliente']['nome']} - Valor Total: R${venda['valor_total']:.2f}"
                for i, venda in enumerate(vendas)],
                        size=(70, 10), select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, key="indice_venda",
                        background_color="#3E4349", text_color="white")],
            [sg.Button("Excluir", size=(20, 1), button_color=("#FFFFFF", "#FF4500")),
             sg.Button("Cancelar", size=(20, 1), button_color=("#FFFFFF", "#3E4349"))]
        ]

        janela = sg.Window("Excluir Venda", layout, background_color="#2C2F36", modal=True)

        selected_index = None
        while True:
            event, values = janela.read()

            if event in (sg.WIN_CLOSED, "Cancelar"):
                break

            elif event == "Excluir":
                selected_index = values.get("indice_venda")
                if selected_index:
                    selected_index = vendas.index(selected_index[0])  # Retorna o índice na lista original
                    break
                else:
                    sg.popup("Selecione uma venda para excluir!", title="Aviso", text_color="white",
                             background_color="#2C2F36")

        janela.close()
        return selected_index

    def exibir_vendas(self, vendas: List[Dict]):
        if not vendas:
            sg.popup("Não há vendas registradas.", title="Aviso", text_color="white", background_color="#2C2F36")
            return
        texto_formatado = ""
        for i, venda in enumerate(vendas, 1):
            try:
                cliente = venda.get("cliente", {})
                vendedor = venda.get("vendedor", {})
                produtos = venda.get("produtos", [])

                texto_formatado += f"Pedido {i}:\n"
                texto_formatado += f"• Cliente: {cliente.get('nome', 'N/A')} (CPF: {cliente.get('cpf', 'N/A')})\n"
                texto_formatado += f"• Vendedor: {vendedor.get('nome', 'N/A')} (CPF: {vendedor.get('cpf', 'N/A')})\n"
                texto_formatado += "• Produtos:\n"

                if produtos:
                    for produto in produtos:
                        nome_produto = produto.get('nome', 'Produto Desconhecido')
                        quantidade = produto.get('quantidade', 0)
                        preco = produto.get('preco', 0.0)
                        texto_formatado += f"    - {nome_produto} | Quantidade: {quantidade} | Preço: R${preco:.2f}\n"
                else:
                    texto_formatado += "    Nenhum produto registrado.\n"

                texto_formatado += f"Valor Total: R${venda.get('valor_total', 0.0):.2f}\n"
                texto_formatado += "━" * 50 + "\n"  # Linha divisória estilizada

            except KeyError as e:
                sg.popup(f"Erro ao processar vendas: campo '{e.args[0]}' não encontrado.",
                         title="Erro de Dados", text_color="red", background_color="#2C2F36", modal=True)
                return

        layout = [
            [sg.Text("Lista de Vendas Registradas", font=("Courier New Bold", 20), text_color="white",
                     background_color="#1F1F1F", justification="center", expand_x=True)],
            [sg.Text("Detalhes das vendas estão listados abaixo:", text_color="white", background_color="#1F1F1F",
                     font=("Arial", 12))],
            [sg.Multiline(texto_formatado, size=(80, 25), background_color="#3E4349", font=("Courier New", 12),
                          text_color="white", disabled=True, border_width=1, autoscroll=True)],
            [sg.Button("Fechar", size=(20, 1), button_color=("#FFFFFF", "#FF4500"))]
        ]

        janela = sg.Window(
            "Lista de Vendas",
            layout,
            background_color="#1F1F1F",
            element_justification="center",
            resizable=False,
            modal=True,
        )

        while True:
            event, _ = janela.read()

            if event in (sg.WIN_CLOSED, "Fechar"):
                break

        janela.close()
