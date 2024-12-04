import PySimpleGUI as sg
from src.utils.enum_tipo_cadastro import TipoCadastro
from src.utils.validador import Validador


class TelaVendedores:
    def __init__(self):
        self.tipo_cadastro = TipoCadastro.VENDEDOR

    def obter_dados_vendedor(self, codigo: int):
        layout = [
            [sg.Text("Cadastro de Vendedor", font=("Helvetica", 16))],
            [sg.Text("CPF:", size=(15, 1)), sg.InputText(key="cpf")],
            [sg.Text("Nome:", size=(15, 1)), sg.InputText(key="nome")],
            [sg.Text("Data de Nascimento:", size=(15, 1)), sg.InputText(key="data_nasc")],
            [sg.Text(f"Código gerado: {codigo}", size=(15, 1))],
            [sg.Text("Salário:", size=(15, 1)), sg.InputText(key="salario")],
            [sg.Button("Salvar"), sg.Button("Cancelar")]
        ]

        window = sg.Window("Cadastro de Vendedor", layout)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                window.close()
                return None

            try:
                cpf = Validador.validar_cpf(values["cpf"])
                nome = Validador.validar_nome(values["nome"])
                data_nasc = Validador.validar_data_nascimento(values["data_nasc"])
                salario = float(values["salario"])
                window.close()
                return {"cpf": cpf, "nome": nome, "data_nasc": data_nasc, "codigo": codigo, "salario": salario}
            except ValueError as e:
                sg.popup_error(f"Erro de validação: {e}")

    def exibir_vendedor(self, vendedor):
        layout = [
            [sg.Text("Dados do Vendedor", font=("Helvetica", 16))],
            [sg.Text(f"CPF: {vendedor['cpf']}")],
            [sg.Text(f"Nome: {vendedor['nome']}")],
            [sg.Text(f"Data de Nascimento: {vendedor['data_nasc']}")],
            [sg.Text(f"Código: {vendedor['codigo']}")],
            [sg.Text(f"Salário: R${vendedor['salario']:.2f}".replace('.', ','))],
            [sg.Button("Fechar")]
        ]

        window = sg.Window("Exibir Vendedor", layout)

        while True:
            event, _ = window.read()
            if event in (sg.WINDOW_CLOSED, "Fechar"):
                break

        window.close()

    def exibir_vendedores(self, vendedores):
        layout = [
            [sg.Text("Lista de Vendedores", font=("Helvetica", 16))],
            [sg.Listbox(values=[
                f"CPF: {v['cpf']}, Nome: {v['nome']}, Salário: R${v['salario']:.2f}".replace('.', ',')
                for v in vendedores
            ], size=(60, len(vendedores)), key="vendedores")],
            [sg.Button("Fechar")]
        ]

        window = sg.Window("Lista de Vendedores", layout)

        while True:
            event, _ = window.read()
            if event in (sg.WINDOW_CLOSED, "Fechar"):
                break

        window.close()
