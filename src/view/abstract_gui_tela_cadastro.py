import PySimpleGUI as sg
from typing import List
from src.utils.enum_operacoes import Operacao
from src.utils.enum_tipo_cadastro import TipoCadastro
from src.utils.validador import Validador


class AbstractTelaCadastro:
    def __init__(self, tipo_cadastro: TipoCadastro) -> None:
        self.option = None
        self.tipo_cadastro = tipo_cadastro
        self.validador = Validador()
        sg.theme_background_color("#2C2F36")

    def criar_layout(self):
        layout = [
            [sg.Text(f"MENU DE {self.tipo_cadastro.plural.upper()}",
                     font=("Courier", 24, "bold"),
                     text_color="white",
                     background_color="#2C2F36",
                     justification='center',
                     expand_x=True)],
            [sg.Text("", size=(1, 2), background_color="#2C2F36")],  # Espaçamento vertical
            [sg.Button(f"Cadastrar novo {self.tipo_cadastro.singular}", key=1, size=(25, 2),
                       font=("Arial", 12), button_color=("#FFFFFF", "#3E4349"),
                       mouseover_colors=("#FFFFFF", "#1F2225"))],
            [sg.Button(f"Listar {self.tipo_cadastro.plural}", key=2, size=(25, 2),
                       font=("Arial", 12), button_color=("#FFFFFF", "#3E4349"),
                       mouseover_colors=("#FFFFFF", "#1F2225"))],
            [sg.Button(f"Procurar {self.tipo_cadastro.singular} por "
                       f"{self.tipo_cadastro.identificador}", key=3,
                       size=(25, 2),
                       font=("Arial", 12), button_color=("#FFFFFF", "#3E4349"),
                       mouseover_colors=("#FFFFFF", "#1F2225"))]
            if not self.tipo_cadastro == TipoCadastro.PEDIDO else None,
            [sg.Button(f"Excluir {self.tipo_cadastro.singular} por {self.tipo_cadastro.identificador}", key=4,
                       size=(25, 2),
                       font=("Arial", 12), button_color=("#FFFFFF", "#3E4349"),
                       mouseover_colors=("#FFFFFF", "#1F2225"))],
            [sg.Button(f"Editar {self.tipo_cadastro.singular} por {self.tipo_cadastro.identificador}", key=5,
                       size=(25, 2),
                       font=("Arial", 12), button_color=("#FFFFFF", "#3E4349"),
                       mouseover_colors=("#FFFFFF", "#1F2225"))]
            if not self.tipo_cadastro == TipoCadastro.PEDIDO else None,
            [sg.Button("Voltar ao menu principal", key=0, size=(25, 2),
                       font=("Arial", 12), button_color=("#FFFFFF", "red"),
                       mouseover_colors=("#FFFFFF", "#500000"))]
        ]

        return [element for element in layout if element is not None]

    def menu(self, opcoes: List[int]) -> int:
        layout = self.criar_layout()
        window = sg.Window(f"Menu de {self.tipo_cadastro.plural.capitalize()}", layout, size=(800, 500),
                           element_justification='center')

        while True:
            event, _ = window.read()

            if event in opcoes or event in [sg.WIN_CLOSED, 0]:
                self.option = event
                break

        window.close()
        return self.option

    def busca_produto(self) -> int | None:
        layout = [
            [sg.Text('Digite o código do produto que deseja buscar:',
                     background_color="#2C2F36",
                     text_color="#FFFFFF")],
            [sg.InputText(key='codigo')],
            [sg.Button('Pesquisar', size=(10, 1), button_color=("#FFFFFF", "#3E4349"),
                       mouseover_colors=("#FFFFFF", "#1F2225")),
             sg.Button('Voltar', size=(10, 1), button_color=("#FFFFFF", "#FF0000"),
                       mouseover_colors=("#FFFFFF", "#8B0000"))]
        ]

        window = sg.Window('Procurar Produto', layout, background_color="#2C2F36")

        while True:
            event, values = window.read()

            if event in (sg.WIN_CLOSED, 'Voltar'):
                window.close()
                return None

            elif event == 'Pesquisar':
                codigo_str = values['codigo']

                try:
                    codigo = int(codigo_str.strip())
                    window.close()
                    return codigo
                except ValueError:
                    sg.popup('Código inválido! Por favor, insira um número inteiro.',
                             background_color='#2C2F36',
                             text_color='#FFFFFF')

    def obter_cpf(self, tipo_busca: Operacao) -> str:
        layout = [
            [sg.Text(f'Qual CPF do {self.tipo_cadastro.singular} que deseja {tipo_busca.value}?',
                     background_color="#2C2F36", text_color="#FFFFFF")],
            [sg.InputText(key='cpf')],
            [sg.Button('Pesquisar', size=(10, 1), button_color=("#FFFFFF", "#3E4349"),
                       mouseover_colors=("#FFFFFF", "#1F2225")),
             sg.Button('Voltar', size=(10, 1), button_color=("#FFFFFF", "#FF0000"),
                       mouseover_colors=("#FFFFFF", "#8B0000"))]
        ]

        window = sg.Window('Procurar CPF', layout, background_color="#2C2F36")

        while True:
            event, values = window.read()

            if event == 'Voltar' or event == sg.WIN_CLOSED:
                window.close()
                return ''
            elif event == 'Pesquisar':
                cpf = values['cpf']
                validacao_cpf = Validador.validar_cpf(cpf)
                is_cpf_valido = "inválido" not in validacao_cpf.lower()

                if is_cpf_valido:
                    window.close()
                    return validacao_cpf
                else:
                    sg.popup('CPF inválido!', background_color='#2C2F36', text_color='#FFFFFF')

    def obter_campos_invalidos(self, values, contexto: str) -> list:
        campos_obrigatorios = []
        validacoes_personalizadas = {}
        if contexto == 'produto':
            campos_obrigatorios = ['nome', 'descricao', 'tamanho', 'cor', 'preco']
            validacoes_personalizadas = {
                'nome': Validador.validar_nome,
                'preco': lambda preco: 'inválido'
                if not isinstance(preco, (int, float)) or preco <= 0 else 'válido',
            }
        elif contexto == 'cliente':
            campos_obrigatorios = ['nome', 'cpf', 'data_nasc', 'categoria']
            validacoes_personalizadas = {
                'cpf': Validador.validar_cpf,
                'nome': Validador.validar_nome,
                'data_nasc': Validador.validar_data_nascimento,
            }
        elif contexto == 'vendedor':
            campos_obrigatorios = ['nome', 'cpf', 'data_nasc', 'salario']
            validacoes_personalizadas = {
                'cpf': Validador.validar_cpf,
                'nome': Validador.validar_nome,
                'data_nasc': Validador.validar_data_nascimento,
                'salario': lambda salario: 'inválido'
                if not isinstance(salario, float) or salario <= 0 else 'válido',
            }
        elif contexto == 'item_venda':
            campos_obrigatorios = ['codigo_produto', 'quantidade', 'preco_venda']
            validacoes_personalizadas = {
                'codigo_produto': lambda codigo: 'inválido'
                if not isinstance(codigo, int) or codigo <= 0 else 'válido',
                'quantidade': lambda quantidade: 'inválido' if not isinstance(quantidade, int
                                                                              ) or quantidade <= 0
                else 'válido',

                'preco_venda': lambda preco: 'inválido' if not isinstance(preco, (int, float)
                                                                          ) or preco < 0 else 'válido',

            }
        elif contexto == 'venda':
            campos_obrigatorios = ['cliente', 'vendedor', 'produtos', 'data_venda']
        else:
            raise ValueError(f"Contexto desconhecido: {contexto}")

        return self.validar_campos(values, campos_obrigatorios, validacoes_personalizadas)

    def validar_campos(self, values: dict, campos_obrigatorios: list,
                       validacoes_personalizadas: dict = None) -> list:
        campos_invalidos = []

        for campo in campos_obrigatorios:
            if not values.get(campo):
                campos_invalidos.append(campo)

        if validacoes_personalizadas:
            for campo, validacao in validacoes_personalizadas.items():
                if campo in values:
                    resultado = validacao(values[campo])
                    if "inválido" in str(resultado).lower():
                        campos_invalidos.append(campo)

        return campos_invalidos

    def confirmar_acoes(self, mensagem: str) -> bool:
        return sg.popup_yes_no(
            mensagem,
            title="Confirmação",
            background_color="#2C2F36",
            text_color="white",
            button_color=("#FFFFFF", "#3E4349")
        ) == "Yes"

    def confirmar_alteracoes_editar(self):
        return sg.popup_yes_no(
            "Há informações preenchidas diferentes do original. Tem certeza que deseja voltar? "
            "As informações serão perdidas.", title="Confirmação",
            background_color="#2C2F36", text_color="white",
            button_color=("#FFFFFF", "#3E4349")) == "Yes"

    def sucesso_cadastro(self):
        sg.popup(f"{self.tipo_cadastro.singular.capitalize()} cadastrado com sucesso!")

    def sucesso_alteracao(self):
        sg.popup(f"{self.tipo_cadastro.singular.capitalize()} alterado com sucesso!")

    def sucesso_exclusao(self, nome: str = ""):
        sg.popup(f"{self.tipo_cadastro.singular.capitalize()} {nome} excluído com sucesso!")

    def sem_cadastro(self):
        sg.popup(f"Não há {self.tipo_cadastro.plural} cadastrados.")

    def cadastro_nao_encontrado(self):
        sg.popup("Cadastro não encontrado.")

    def mostrar_erro(self, erro: str):
        sg.popup(erro)
