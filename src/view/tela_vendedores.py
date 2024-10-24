from src.model.vendedor import Vendedor
from typing import List
from src.model.validador import Validador


class TelaVendedores:
    def menu(self):
        print("\n--- Menu de Vendedores ---")
        print("1. Cadastrar novo vendedor")
        print("2. Listar vendedores")
        print("3. Buscar vendedor por CPF")
        print("4. Editar vendedor por CPF")
        print("5. Excluir vendedor por CPF")
        print("0. Voltar ao menu principal")
        return input("Escolha uma opção: ")

    def obter_dados_vendedor(self) -> Vendedor:
        while True:
            try:
                print("\n--- Cadastro de Vendedor ---")
                cpf = Validador.validar_cpf()
                nome = Validador.validar_nome()
                data_nasc = Validador.validar_data_nascimento()
                codigo = input("Código: ")
                salario = input("Salário: ")
                
                return Vendedor(cpf, nome, data_nasc, int(codigo), float(salario))
            
            except ValueError as e:
                print(f"Erro ao cadastrar vendedor: {e}. Tente novamente.")

    def cpf_ja_cadastrado(self):
        print("Erro: Vendedor já cadastrado com este CPF.")

    def obter_cpf(self) -> str:
        return Validador.validar_cpf()

    def sucesso_cadastro(self):
        print("Vendedor cadastrado com sucesso!")

    def sucesso_alteracao(self):
        print("Vendedor alterado com sucesso!")

    def sucesso_exclusao(self, nome_vendedor: str):
        print(f"Vendedor {nome_vendedor} excluído com sucesso!")

    def sem_vendedores(self):
        print("Não há vendedores cadastrados.")

    def vendedor_nao_encontrado(self):
        print("Vendedor não encontrado.")

    def exibir_vendedor(self, vendedor: Vendedor):
        print(f"Nome: {vendedor.nome}, CPF: {vendedor.cpf}, Salário: {vendedor.salario}")

    def exibir_vendedores(self, vendedores: List[Vendedor]):
        print("\n--- Lista de Vendedores ---")
        for vendedor in vendedores:
            print(f"Nome: {vendedor.nome}, CPF: {vendedor.cpf}, Salário: {vendedor.salario}")

    def editar_dados_vendedor(self, vendedor: Vendedor) -> Vendedor:
        print("\n--- Editar Vendedor ---")
        print("Deixe em branco para manter os dados atuais.")
        nome = input(f"Nome atual: {vendedor.nome} (novo nome): ") or vendedor.nome
        cpf = input(f"CPF atual: {vendedor.cpf} (novo CPF): ") or vendedor.cpf
        data_nasc = input(f"Data de nascimento atual: {vendedor.data_nasc} (nova data de nascimento): ") or vendedor.data_nasc
        codigo = input(f"Código atual: {vendedor.codigo} (novo código): ") or vendedor.codigo
        salario = input(f"Salário atual: {vendedor.salario} (novo salário): ") or vendedor.salario

        return Vendedor(cpf, nome, data_nasc, int(codigo), float(salario))
