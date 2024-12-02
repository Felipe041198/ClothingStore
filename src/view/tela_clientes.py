from typing import List

from src.utils.enum_categoria_cliente import CategoriaCliente
from src.utils.enum_tipo_cadastro import TipoCadastro
from src.utils.validador import Validador
from src.view.abstract_tela_cadastro import AbstractTelaCadastro


class TelaClientes(AbstractTelaCadastro):

    def __init__(self):
        super().__init__(tipo_cadastro=TipoCadastro.CLIENTE)

    def obter_dados_cliente(self, codigo: int):
        print("\n--- Cadastro de Cliente ---")
        cpf = Validador.validar_cpf()
        nome = Validador.validar_nome()
        data_nasc = Validador.validar_data_nascimento()
        print("Categoria:")
        for categoria in CategoriaCliente:
            print(f"{categoria.codigo} - {categoria.nome}")

        opcao_categoria = self.le_num_inteiro("Escolha uma opção: ", CategoriaCliente.opcoes())
        categoria = CategoriaCliente.busca_categoria(opcao_categoria)
        dados_cliente = {
            "cpf": cpf,
            "nome": nome,
            "data_nascimento": data_nasc,
            "categoria": categoria,
            "codigo": codigo,
        }
        return dados_cliente

    def exibir_cliente(self, dados_cliente: dict):
        print(f"Código: {dados_cliente['codigo']}, "
              f"Nome: {dados_cliente['nome']}, "
              f"CPF: {dados_cliente['cpf']}, "
              f"Data de nascimento: {dados_cliente['data_nasc']}, "
              f"Categoria: {dados_cliente['categoria'].nome}")

    def exibir_clientes(self, clientes: List[dict]):
        print("\n--- Lista de Clientes ---")
        for cliente in clientes:
            print(f"Código: {cliente['codigo']}, "
                  f"Nome: {cliente['nome']}, "
                  f"CPF: {cliente['cpf']}, "
                  f"Data de nascimento: {cliente['data_nasc']}, "
                  f"Categoria: {cliente['categoria'].nome}")

    def editar_dados_cliente(self, dados_cliente: dict) -> dict:
        try:
            print("\n--- Editar Cliente ---")
            print("Deixe em branco para manter os dados atuais.")

            nome = dados_cliente['nome']
            cpf = dados_cliente['cpf']
            data_nasc = dados_cliente['data_nasc']
            categoria = dados_cliente['categoria']

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

            return {"nome": nome, "cpf": cpf, "data_nasc": data_nasc, "categoria": categoria, "codigo": dados_cliente['codigo']}
        except ValueError as e:
            print(f"Erro ao editar os dados do cliente: {e}. Tente novamente.")
