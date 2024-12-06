from src.view.abstract_tela_cadastro import AbstractTelaCadastro
from src.utils.enum_tipo_cadastro import TipoCadastro
from typing import List


class TelaProduto(AbstractTelaCadastro):
    def __init__(self):
        super().__init__(tipo_cadastro=TipoCadastro.PRODUTO)

    def obter_dados_produto(self, codigo: int):
        while True:
            print("\n--- Cadastro de Produto ---")
            nome = input("Digite o nome do produto: ")
            descricao = input("Digite a descrição do produto: ")
            tamanho = input("Digite o tamanho do produto (P/M/G): ")
            cor = input("Digite a cor do produto: ")
            preco = float(input("Digite o preço do produto: "))
            return {
                "codigo": codigo,
                "nome": nome,
                "descricao": descricao,
                "tamanho": tamanho,
                "cor": cor,
                "preco": preco
            }

    def busca_produto(self):
        try:
            return int(input("Digite o código do produto: "))
        except ValueError:
            print("Código inválido.")
            return None

    def exibir_produto(self, dados_produto: dict):
        print(f"Código: {dados_produto['codigo']} | "
              f"Nome: {dados_produto['nome']} | "
              f"Descrição: {dados_produto['descricao']} | "
              f"Tamanho: {dados_produto['tamanho']} | "
              f"Cor: {dados_produto['cor']} | "
              f"Preço: R${dados_produto['preco']:.2f}")

    def exibir_lista_produtos(self, produtos: List[dict]):
        print("\n--- Lista de Produtos ---")
        if not produtos:
            print("\nNenhum produto cadastrado.")
        else:
            for produto in produtos:
                print(f"Código: {produto['codigo']} | "
                      f"Nome: {produto['nome']} | "
                      f"Preço: R${produto['preco']:.2f}")

    def mostrar_mensagem(self, mensagem):
        print(f"\n{mensagem}")

    def editar_dados_produto(self, dados_produto: dict) -> dict:
        print("\n--- Editar Produto ---")
        print(f"Produto Atual: {dados_produto['nome']} (Código: {dados_produto['codigo']})")
        nome = input(f"Novo nome ({dados_produto['nome']}): ") or dados_produto['nome']
        descricao = input(f"Nova descrição ({dados_produto['descricao']}): ") or dados_produto['descricao']
        tamanho = input(f"Novo tamanho ({dados_produto['tamanho']}): ") or dados_produto['tamanho']
        cor = input(f"Nova cor ({dados_produto['cor']}): ") or dados_produto['cor']
        try:
            preco = float(input(f"Novo preço (R${dados_produto['preco']}): ")) or dados_produto['preco']
        except ValueError:
            print("Preço inválido. Mantendo o preço atual.")
            preco = dados_produto['preco']
        return {
            "codigo": dados_produto['codigo'],
            "nome": nome,
            "descricao": descricao,
            "tamanho": tamanho,
            "cor": cor,
            "preco": preco
        }
