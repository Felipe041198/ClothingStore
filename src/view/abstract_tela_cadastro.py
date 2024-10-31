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
        print(f"3. Procurar {self.tipo_cadastro.singular} por CPF")
        print(f"4. Excluir {self.tipo_cadastro.singular} por CPF")
        print(f"5. Editar {self.tipo_cadastro.singular} por CPF")
        print("0. Voltar ao menu principal")
        opcao = self.le_num_inteiro("Escolha a opção: ", opcoes)
        return opcao

    def obter_cpf(self, tipo_busca: Operacao) -> int:
        print(f"\n--- Qual CPF do {self.tipo_cadastro.singular} que deseja {tipo_busca.value}? ---")
        cpf = input("CPF: ")
        return int(cpf)

    def sucesso_cadastro(self):
        print(f"{self.tipo_cadastro.singular} cadastrado com sucesso!")

    def sucesso_alteracao(self):
        print(f"{self.tipo_cadastro.singular} alterado com sucesso!")

    def sucesso_exclusao(self, nome: str):
        print(f"{self.tipo_cadastro.singular} {nome} excluído com sucesso!")

    def sem_cadastro(self):
        print(f"Não há {self.tipo_cadastro.plural} cadastrados.")

    def cpf_ja_cadastrado(self):
        print(f"Erro: {self.tipo_cadastro.singular} já cadastrado com este CPF.")

    def cadastro_nao_encontrado(self):
        print("CPF não encontrado.")
