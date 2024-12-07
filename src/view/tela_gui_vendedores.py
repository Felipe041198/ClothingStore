from typing import List

import PySimpleGUI as sg
from src.model.vendedor import Vendedor
from src.utils.enum_tipo_cadastro import TipoCadastro
from src.utils.validador import Validador


class TelaVendedores(AbstractTelaCadastro):
    def __init__(self):
        super().__init__(tipo_cadastro=TipoCadastro.VENDEDOR)

    def obter_dados_vendedor(self, codigo: int) -> Vendedor:
        layout = [
            [sg.Text(f"--- Cadastro de Vendedor (Código: {codigo}) ---", font=("Helvetica", 14))],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText(key='cpf')],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText(key='nome')],
            [sg.Text('Data de Nascimento:', size=(15, 1)), sg.InputText(key='data_nasc')],
            [sg.Text('Salário:', size=(15, 1)), sg.InputText(key='salario')],
            [sg.Submit(), sg.Cancel()]
        ]

        window = sg.Window('Cadastro de Vendedor', layout)
        event, values = window.read()
        window.close()

        if event == 'Submit':
            cpf = Validador.validar_cpf(values['cpf'])
            nome = Validador.validar_nome(values['nome'])
            data_nasc = Validador.validar_data_nascimento(values['data_nasc'])
            salario = float(values['salario'])

            return Vendedor(cpf, nome, data_nasc, codigo, salario)

    def exibir_vendedor(self, vendedor: Vendedor):
        salario_formatado = f"R${vendedor.salario:,.2f}".replace('.', ',')
        sg.popup(f"Vendedor\n\n"
                 f"Código: {vendedor.codigo}\n"
                 f"Nome: {vendedor.nome}\n"
                 f"CPF: {vendedor.cpf}\n"
                 f"Data de nascimento: {vendedor.data_nasc}\n"
                 f"Salário: {salario_formatado}", title="Detalhes do Vendedor")

    def exibir_vendedores(self, vendedores: List[Vendedor]):
        if not vendedores:
            self.sem_cadastro()
            return

        layout = [[sg.Text("--- Lista de Vendedores ---", font=("Helvetica", 14))],
                  [sg.Listbox(values=[f"Código: {v.codigo}, Nome: {v.nome}, CPF: {v.cpf}" for v in vendedores],
                              size=(60, len(vendedores)))]]

        window = sg.Window('Lista de Vendedores', layout)
        window.read()
        window.close()

    def editar_dados_vendedor(self, vendedor: Vendedor) -> Vendedor:
        layout = [
            [sg.Text("--- Editar Vendedor ---", font=("Helvetica", 14))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText(vendedor.nome, key='nome')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText(vendedor.cpf, key='cpf')],
            [sg.Text('Data de Nascimento:', size=(15, 1)), sg.InputText(vendedor.data_nasc, key='data_nasc')],
            [sg.Text('Salário:', size=(15, 1)), sg.InputText(f"{vendedor.salario:.2f}", key='salario')],
            [sg.Submit(), sg.Cancel()]
        ]

        window = sg.Window('Editar Vendedor', layout)
        event, values = window.read()
        window.close()

        if event == 'Submit':
            nome = Validador.validar_nome(values['nome'])
            cpf = Validador.validar_cpf(values['cpf'])
            data_nasc = Validador.validar_data_nascimento(values['data_nasc'])
            try:
                salario = float(values['salario'])
            except ValueError:
                salario = vendedor.salario
                sg.popup("Salário inválido. Mantendo o valor atual.", title="Erro")

            return Vendedor(cpf, nome, data_nasc, vendedor.codigo, salario)
