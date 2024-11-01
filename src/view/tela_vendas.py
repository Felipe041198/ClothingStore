from typing import List

from src.model.cliente import Cliente
from src.model.item_venda import ItemVenda
from src.model.produto import Produto
from src.model.venda import Venda
from src.model.vendedor import Vendedor
from src.view.abstract_tela import AbstractTela


class TelaVendas(AbstractTela):
    def __init__(self):
        pass

    def menu(self, opcoes: List[int]) -> int:
        print("\n--- Menu de vendas ---")
        print("1. Realizar uma nova venda")
        print("2. Listar vendas")
        print("3. Detalhar venda")
        print("4. Excluir venda")
        print("0. Voltar ao menu principal")
        opcao = self.le_num_inteiro("Escolha a opção: ", opcoes)
        return opcao

    def obter_dados_venda(
        self,
        clientes: List[Cliente],
        vendedores: List[Vendedor],
        produtos: List[Produto]
    ) -> Venda:
        print("\n--- Pedido de venda ---")

        # Selecionando cliente:
        cliente_selecionado = self.seleciona_cliente(clientes)

        # Selecionando vendedor:
        vendedor_selecionado = self.seleciona_vendedor(vendedores)

        # Selecionando produtos:
        produtos_selecionados = self.seleciona_produtos(produtos)

        return Venda(
            cliente=cliente_selecionado,
            vendedor=vendedor_selecionado,
            produtos=produtos_selecionados
        )

    def seleciona_cliente(self, clientes) -> Cliente:
        print("\nClientes disponíveis:")
        lista_opcoes = []
        for i, cliente in enumerate(clientes, 1):
            print(f"{i}. {cliente.nome} - CPF: {cliente.cpf}")
            lista_opcoes.append(i)

        indice_cliente = self.le_num_inteiro("Escolha o cliente (número): ", lista_opcoes)
        cliente_selecionado = clientes[indice_cliente - 1]
        return cliente_selecionado

    def seleciona_vendedor(self, vendedores) -> Vendedor:
        print("\nVendedores disponíveis:")
        lista_opcoes = []
        for i, vendedor in enumerate(vendedores, 1):
            print(f"{i}. {vendedor.nome} - Código: {vendedor.cpf}")
            lista_opcoes.append(i)
        indice_vendedor = self.le_num_inteiro("Escolha o vendedor (número): ", lista_opcoes)
        vendedor_selecionado = vendedores[indice_vendedor - 1]
        return vendedor_selecionado

    def seleciona_produtos(self, produtos) -> List[ItemVenda]:
        produtos_selecionados = []
        while True:
            print("\nProdutos disponíveis:")
            for i, produto in enumerate(produtos, 1):
                print(f"{i}. {produto.nome} - Preço: {produto.preco}")
            indice_produto = self.le_num_inteiro("Escolha o produto (número) ou 0 para finalizar: ",
                                                 list(range(len(produtos) + 1)))
            if indice_produto == 0:
                break
            produto_selecionado = produtos[indice_produto - 1]

            # Solicitar quantidade do produto selecionado
            quantidade = self.le_num_inteiro(f"Digite a quantidade para {produto_selecionado.nome}: ",
                                             list(range(1, 101)))
            produto_pedido = ItemVenda(
                produto_selecionado.codigo,
                quantidade,
                produto_selecionado.preco
            )
            produtos_selecionados.append(produto_pedido)
        return produtos_selecionados

    def sucesso_venda(self):
        print("\n Venda cadastrada com sucesso")
