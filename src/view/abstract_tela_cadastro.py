from typing import List

from src.utils.enum_operacoes import Operacao
from src.utils.enum_tipo_cadastro import TipoCadastro
from src.view.abstract_tela import AbstractTela


class AbstractTelaCadastro(AbstractTela):
    def __init__(self, tipo_cadastro: TipoCadastro) -> None:
        self.tipo_cadastro = tipo_cadastro

    def menu(self, opcoes: List[int]) -> int:
        print(f"\n--- Menu de {self.tipo_cadastro.plural.capitalize()} ---")
        print(f"1. Cadastrar novo {self.tipo_cadastro.singular}")
        print(f"2. Listar {self.tipo_cadastro.plural}")
        if not self.tipo_cadastro == TipoCadastro.PEDIDO:
            print(f"3. Procurar {self.tipo_cadastro.singular} por {self.tipo_cadastro.identificador}")
        print(f"4. Excluir {self.tipo_cadastro.singular} por {self.tipo_cadastro.identificador}")
        if not self.tipo_cadastro == TipoCadastro.PEDIDO:
            print(f"5. Editar {self.tipo_cadastro.singular} por {self.tipo_cadastro.identificador}")
        print("0. Voltar ao menu principal")
        opcao = self.le_num_inteiro("Escolha a opção: ", opcoes)
        return opcao

    def obter_cpf(self, tipo_busca: Operacao) -> str:
        print(f"\n--- Qual CPF do {self.tipo_cadastro.singular} que deseja {tipo_busca.value}? ---")
        cpf = input("CPF: ")
        return cpf

    def sucesso_cadastro(self):
        print(f"{self.tipo_cadastro.singular.capitalize()} cadastrado com sucesso!")

    def sucesso_alteracao(self):
        print(f"{self.tipo_cadastro.singular.capitalize()} alterado com sucesso!")

    def sucesso_exclusao(self, nome: str = ""):
        print(f"{self.tipo_cadastro.singular.capitalize()} {nome} excluído com sucesso!")

    def sem_cadastro(self):
        print(f"Não há {self.tipo_cadastro.plural} cadastrados.")

    def cadastro_nao_encontrado(self):
        print("Cadastro não encontrado.")

    def mostrar_erro(self, erro: str):
        print(erro)
