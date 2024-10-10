from typing import List
from src.model.cliente import Cliente
from src.view.abstract_tela_clientes import AbstractTelaClientes


class TelaClientes(AbstractTelaClientes):

    def menu(self):
        print("\n--- Menu de Clientes ---")
        print("1. Cadastrar novo cliente")
        print("2. Listar clientes")
        print("3. Voltar ao menu principal")
        return input("Escolha uma opção: ")

    def obter_dados_cliente(self) -> Cliente:
        print("\n--- Cadastro de Cliente ---")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        data_nasc = input("Data de nascimento: ")
        categoria = input("Categoria: ")
        return Cliente(int(cpf), nome, data_nasc, int(categoria))

    def sucesso_cadastro(self):
        print("Cliente cadastrado com sucesso!")

    def sem_clientes(self):
        print("Não há clientes cadastrados.")

    def exibir_clientes(self, clientes: List[Cliente]):
        print("\n--- Lista de Clientes ---")
        for cliente in clientes:
            print(f"Nome: {cliente.nome}, CPF: {cliente.cpf}, Data de nascimento: {cliente.data_nasc}, Categoria: {cliente.categoria}")

    def opcao_invalida(self):
        print("Opção inválida, tente novamente.")