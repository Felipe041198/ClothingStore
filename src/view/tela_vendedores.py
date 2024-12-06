from typing import List

from src.utils.enum_tipo_cadastro import TipoCadastro
from src.utils.validador import Validador
from src.view.abstract_tela_cadastro import AbstractTelaCadastro


class TelaVendedores(AbstractTelaCadastro):
    def __init__(self):
        super().__init__(tipo_cadastro=TipoCadastro.VENDEDOR)

    def obter_dados_vendedor(self, codigo: int):
        while True:
            print("\n--- Cadastro de Vendedor ---")
            cpf = Validador.validar_cpf()
            nome = Validador.validar_nome()
            data_nasc = Validador.validar_data_nascimento()
            print(f"Código gerado: {codigo}")
            salario = float(input("Salário: "))

            dados_vendedor = {
                "cpf": cpf,
                "nome": nome,
                "data_nasc": data_nasc,
                "codigo": codigo,
                "salario": salario
            }

            return dados_vendedor

    def exibir_vendedor(self, vendedor: dict):
        salario_formatado = f"R${vendedor['salario']}".replace('.', ',')
        print(f"Código: {vendedor['codigo']}, "
              f"Nome: {vendedor['nome']}, "
              f"CPF: {vendedor['cpf']}, "
              f"Data de nascimento: {vendedor['data_nasc']}, "
              f"Salário: {salario_formatado}")

    def exibir_vendedores(self, vendedores: List[dict]):
        print("\n--- Lista de Vendedores ---")
        for vendedor in vendedores:
            salario_formatado = f"R${vendedor['salario']}".replace('.', ',')
            print(f"Código: {vendedor['codigo']}, "
                  f"Nome: {vendedor['nome']}, "
                  f"CPF: {vendedor['cpf']}, "
                  f"Data de nascimento: {vendedor['data_nasc']}, "
                  f"Salário: {salario_formatado}")

    def editar_dados_vendedor(self, vendedor: dict) -> dict:
        print("\n--- Editar Vendedor ---")
        print("Deixe em branco para manter os dados atuais.")
        nome = vendedor['nome']
        cpf = vendedor['cpf']
        data_nasc = vendedor['data_nasc']
        salario = vendedor['salario']

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

        salario_novo = input(f"Salário atual ({salario:.2f}): ") or salario
        try:
            salario = float(salario_novo)
        except ValueError:
            print("Salário inválido. Mantendo o valor atual.")

        return {
            "cpf": cpf,
            "nome": nome,
            "data_nasc": data_nasc,
            "codigo": vendedor['codigo'],
            "salario": salario,
        }
