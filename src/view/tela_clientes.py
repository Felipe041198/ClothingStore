from typing import List

from src.model.cliente import Cliente
from src.utils.enum_tipo_cadastro import TipoCadastro
from src.view.abstract_tela_cadastro import AbstractTelaCadastro


class TelaClientes(AbstractTelaCadastro):

    def __init__(self):
        super().__init__(tipo_cadastro=TipoCadastro.CLIENTE)

    def obter_dados_cliente(self) -> Cliente:
        print("\n--- Cadastro de Cliente ---")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        data_nasc = input("Data de nascimento: ")
        categoria = input("Categoria: ")
        return Cliente(int(cpf), nome, data_nasc, int(categoria))

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
