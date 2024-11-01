from typing import List

from src.model.cliente import Cliente
from src.utils.enum_tipo_cadastro import TipoCadastro
from src.utils.codigo_gerador import GeradorCodigo
from titi.ClothingStore.src.utils.validador import Validador
from src.view.abstract_tela_cadastro import AbstractTelaCadastro


class TelaClientes(AbstractTelaCadastro):

    def __init__(self):
        super().__init__(tipo_cadastro=TipoCadastro.CLIENTE)

    def obter_dados_cliente(self) -> Cliente:
        print("\n--- Cadastro de Cliente ---")
        cpf = Validador.validar_cpf()
        nome = Validador.validar_nome()
        data_nasc = Validador.validar_data_nascimento()
        categoria = GeradorCodigo().gerar_codigo("cliente")
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
        try:
            print("\n--- Editar Cliente ---")
            print("Deixe em branco para manter os dados atuais.")

            nome = cliente.nome
            cpf = cliente.cpf
            data_nasc = cliente.data_nasc
            categoria = cliente.categoria

            nome_novo = input(f"Nome atual ({nome}): ") or nome
            if nome_novo != nome:
                Validador.validar_nome(nome_novo)
                nome = nome_novo

            cpf_novo = input(f"CPF atual ({cpf}): ") or cpf
            if cpf_novo != cpf:
                Validador.validar_cpf(cpf_novo)
                cpf = cpf_novo

            data_nasc_novo = input(f"Data de nascimento atual ({data_nasc}): ") or data_nasc
            if data_nasc_novo != data_nasc:
                Validador.validar_data_nascimento(data_nasc_novo)
                data_nasc = data_nasc_novo

            return Cliente(int(cpf), nome, data_nasc, categoria)
        except ValueError as e:
            print(f"Erro ao editar os dados do cliente: {e}. Tente novamente.")
