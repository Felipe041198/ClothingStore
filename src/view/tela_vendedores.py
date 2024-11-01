from src.model.vendedor import Vendedor
from typing import List
from src.model.validador import Validador
from src.view.abstract_tela_cadastro import AbstractTelaCadastro
from src.utils.enum_tipo_cadastro import TipoCadastro
from src.utils.codigo_gerador import GeradorCodigo


class TelaVendedores(AbstractTelaCadastro):
    def __init__(self):
        super().__init__(tipo_cadastro=TipoCadastro.VENDEDOR)

    def obter_dados_vendedor(self) -> Vendedor:
        while True:
            print("\n--- Cadastro de Vendedor ---")
            cpf = Validador.validar_cpf()
            nome = Validador.validar_nome()
            data_nasc = Validador.validar_data_nascimento()
            codigo = GeradorCodigo().gerar_codigo("vendedor")
            print(f"Código gerado: {codigo}")
            salario = input("Salário: ")

            return Vendedor(cpf, nome, data_nasc, int(codigo), float(salario))

    def exibir_vendedor(self, vendedor: Vendedor):
        salario_formatado = f"R${vendedor.salario}".replace('.', ',')
        print(f"Nome: {vendedor.nome}, "
              f"CPF: {vendedor.cpf}, "
              f"Data de nascimento: {vendedor.data_nasc}, "
              f"Categoria: {vendedor.codigo}, "
              f"Salário: {salario_formatado}")

    def exibir_vendedores(self, vendedores: List[Vendedor]):
        print("\n--- Lista de Vendedores ---")
        for vendedor in vendedores:
            salario_formatado = f"R${vendedor.salario}".replace('.', ',')
            print(f"Nome: {vendedor.nome}, "
                f"CPF: {vendedor.cpf}, "
                f"Data de nascimento: {vendedor.data_nasc}, "
                f"Categoria: {vendedor.codigo}, "
                f"Salário: {salario_formatado}")

    def editar_dados_vendedor(self, vendedor: Vendedor) -> Vendedor:
        print("\n--- Editar Vendedor ---")
        print("Deixe em branco para manter os dados atuais.")
        nome = vendedor.nome
        cpf = vendedor.cpf
        data_nasc = vendedor.data_nasc
        salario = vendedor.salario
        codigo = vendedor.codigo

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

        return Vendedor(int(cpf), nome, data_nasc, codigo, salario)
