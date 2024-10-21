from typing import List
from src.model.cliente import Cliente
from src.utils.enum_operacoes import Operacao
from src.view.abstract_tela_clientes import AbstractTelaClientes


class TelaClientes(AbstractTelaClientes):

    def menu(self):
        print("\n--- Menu de Clientes ---")
        print("1. Cadastrar novo cliente")
        print("2. Listar clientes")
        print("3. Procurar cliente por CPF")
        print("4. Excluir cliente por CPF")
        print("5. Editar cliente por CPF")
        print("0. Voltar ao menu principal")
        return input("Escolha uma opção: ")

    def obter_dados_cliente(self) -> Cliente:
        print("\n--- Cadastro de Cliente ---")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        data_nasc = input("Data de nascimento: ")
        categoria = input("Categoria: ")
        return Cliente(int(cpf), nome, data_nasc, int(categoria))

    def obter_cpf(self, tipo_busca: Operacao) -> int:
        print(f"\n--- Qual CPF do cliente que deseja {tipo_busca.value}? ---")
        cpf = input("CPF: ")
        return int(cpf)

    def sucesso_cadastro(self):
        print("Cliente cadastrado com sucesso!")

    def sucesso_alteracao(self):
        print("Cliente alterado com sucesso!")

    def sucesso_exclusao(self, nome_cliente: str):
        print(f"Cliente {nome_cliente} excluído com sucesso!")

    def sem_clientes(self):
        print("Não há clientes cadastrados.")

    def cliente_nao_encontrado(self):
        print("CPF não encontrado.")

    def exibir_cliente(self, cliente: Cliente):
        print(f"Nome: {cliente.nome}, "
              f"CPF: {cliente.cpf}, "
              f"Data de nascimento: {cliente.data_nasc}, "
              f"Categoria: {cliente.categoria}")

    def exibir_clientes(self, clientes: List[Cliente]):
        print("\n--- Lista de Clientes ---")
        for cliente in clientes:
            print(f"Nome: {cliente.nome}, "
                  f"CPF: {cliente.cpf}, "
                  f"Data de nascimento: {cliente.data_nasc}, "
                  f"Categoria: {cliente.categoria}")

    def editar_dados_cliente(self, cliente: Cliente) -> Cliente:
        print("\n--- Editar Cliente ---")
        print("Deixe em branco para manter os dados atuais.")

        nome = input(f"Nome atual: {cliente.nome} (novo nome): ") or cliente.nome
        cpf = input(f"CPF atual: {cliente.cpf} (novo CPF): ") or cliente.cpf
        data_nasc = input(
            f"Data de nascimento atual: {cliente.data_nasc} (nova data de nascimento): ") or cliente.data_nasc
        categoria = input(f"Categoria atual: {cliente.categoria} (nova categoria): ") or cliente.categoria

        # Atualiza os dados do cliente mantendo os não alterados
        return Cliente(int(cpf), nome, data_nasc, int(categoria))

    def opcao_invalida(self):
        print("Opção inválida, tente novamente.")
