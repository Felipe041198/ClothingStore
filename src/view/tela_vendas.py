from typing import List

from src.utils.enum_tipo_cadastro import TipoCadastro
from src.view.abstract_tela_cadastro import AbstractTelaCadastro


class TelaVendas(AbstractTelaCadastro):
    def __init__(self):
        super().__init__(tipo_cadastro=TipoCadastro.PEDIDO)

    def obter_dados_venda(
        self,
        clientes: List[dict],
        vendedores: List[dict],
        produtos: List[dict]
    ) -> dict:
        print("\n--- Pedido de venda ---")

        # Selecionando cliente:
        cliente_selecionado = self.seleciona_cliente(clientes)

        # Selecionando vendedor:
        vendedor_selecionado = self.seleciona_vendedor(vendedores)

        # Selecionando produtos:
        produtos_selecionados = self.seleciona_produtos(produtos)

        return {
            "cliente": cliente_selecionado,
            "vendedor": vendedor_selecionado,
            "produtos": produtos_selecionados,
        }

    def seleciona_cliente(self, clientes) -> dict:
        print("\nClientes disponíveis:")
        lista_opcoes = []
        for cliente in clientes:
            print(f"{cliente['codigo']}. {cliente['nome']} - CPF: {cliente['cpf']}")
            lista_opcoes.append(cliente["codigo"])

        codigo_cliente = self.le_num_inteiro("Escolha o cliente (número): ", lista_opcoes)

        cliente_selecionado = (
            next((cliente for cliente in clientes if cliente["codigo"] == codigo_cliente), None)
        )
        return cliente_selecionado

    def seleciona_vendedor(self, vendedores) -> dict:
        print("\nVendedores disponíveis:")
        lista_opcoes = []
        for vendedor in vendedores:
            print(f"{vendedor['codigo']}. {vendedor['nome']} - Código: {vendedor['cpf']}")
            lista_opcoes.append(vendedor['codigo'])
        codigo_vendedor = self.le_num_inteiro("Escolha o vendedor (número): ", lista_opcoes)
        vendedor_selecionado = (
            next((vendedor for vendedor in vendedores if vendedor['codigo'] == codigo_vendedor), None)
        )
        return vendedor_selecionado

    def seleciona_produtos(self, produtos) -> list[dict]:
        produtos_selecionados = []
        while True:
            print("\nProdutos disponíveis:")
            for i, produto in enumerate(produtos, 1):
                print(f"{i}. {produto['nome']} - Preço: {produto['preco']}")
            indice_produto = self.le_num_inteiro("Escolha o produto (número) ou 0 para finalizar: ",
                                                 list(range(len(produtos) + 1)))
            if indice_produto == 0:
                break
            produto_selecionado = produtos[indice_produto - 1]

            # Solicitar quantidade do produto selecionado
            quantidade = self.le_num_inteiro(f"Digite a quantidade para {produto_selecionado['nome']}: ",
                                             list(range(1, 101)))
            produto_pedido = {
                "codigo": produto_selecionado['codigo'],
                "quantidade": quantidade,
                "preco": produto_selecionado['preco'],
            }
            produtos_selecionados.append(produto_pedido)
        return produtos_selecionados

    def exibir_vendas(self, vendas: List[dict]):

        print("\n--- Lista de Pedidos ---")
        for venda in vendas:
            print(f"\nCliente: {venda['cliente']['nome']}, "
                  f"Vendedor: {venda['vendedor']['nome']}, "
                  f"Data da venda: {venda['data_venda']} ")
            for produto in venda['produtos']:
                print(f"Código do produto: {produto['codigo_produto']}, "
                      f"qnt: {produto['quantidade']}, "
                      f"preco: {produto['preco_venda']}")
            print(f"Preço total: {venda['valor_total']}")
            print("----------------------------------")

    def seleciona_vendas(self, vendas) -> dict:
        print("\nPedidos disponíveis:")
        lista_opcoes = []
        for i, venda in enumerate(vendas, 1):
            print(f"{i}. {venda.cliente.nome} - Data: {venda.data_venda} - Preço: {venda.valor_total}")
            lista_opcoes.append(i)
        indice_venda = self.le_num_inteiro("Escolha o pedido (número): ", lista_opcoes)
        venda_selecionada = vendas[indice_venda - 1]
        return venda_selecionada
