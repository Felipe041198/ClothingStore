from src.view.abstract_tela_cadastro import AbstractTelaCadastro
from src.utils.enum_tipo_cadastro import TipoCadastro
from src.model.produto import Produto
from typing import List


class TelaProduto(AbstractTelaCadastro):
    def __init__(self):
        super().__init__(tipo_cadastro=TipoCadastro.PRODUTO)

    def obter_dados_produto(self, codigo: int) -> Produto:
        while True:
            print("\n--- Cadastro de Produto ---")
            nome = input("Digite o nome do produto: ")
            descricao = input("Digite a descrição do produto: ")
            tamanho = input("Digite o tamanho do produto (P/M/G): ")
            cor = input("Digite a cor do produto: ")
            preco = float(input("Digite o preço do produto: "))
            return Produto(codigo, nome, descricao, tamanho, cor, preco)

    def busca_produto(self):
        try:
            return int(input("Digite o código do produto: "))
        except ValueError:
            print("Código inválido.")
            return None

    def exibir_produto(self, produto: Produto):
        print(f"Código: {produto.codigo} | Nome: {produto.nome} | Descrição: {produto.descricao} | "
              f"Tamanho: {produto.tamanho} | Cor: {produto.cor} | Preço: R${produto.preco:.2f}")

    def exibir_lista_produtos(self, produtos: List[Produto]):
        print("\n--- Lista de Produtos ---")
        if not produtos:
            print("\nNenhum produto cadastrado.")
        else:
            for produto in produtos:
                print(f"Código: {produto.codigo} | Nome: {produto.nome} | Preço: R${produto.preco:.2f}")

    def mostrar_mensagem(self, mensagem):
        print(f"\n{mensagem}")

    def editar_dados_produto(self, produto: Produto) -> Produto:
        print("\n--- Editar Produto ---")
        print(f"Produto Atual: {produto.nome} (Código: {produto.codigo})")
        nome = input(f"Novo nome ({produto.nome}): ") or produto.nome
        descricao = input(f"Nova descrição ({produto.descricao}): ") or produto.descricao
        tamanho = input(f"Novo tamanho ({produto.tamanho}): ") or produto.tamanho
        cor = input(f"Nova cor ({produto.cor}): ") or produto.cor
        try:
            preco = float(input(f"Novo preço (R${produto.preco}): ")) or produto.preco
        except ValueError:
            print("Preço inválido. Mantendo o preço atual.")
            preco = produto.preco
        return Produto(produto.codigo, nome, descricao, tamanho, cor, preco)
