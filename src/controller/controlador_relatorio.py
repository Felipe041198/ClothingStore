from src.controller.abstract_controlador import AbstractControlador
from src.model.venda import Venda
from datetime import datetime, timedelta
from typing import List, Optional, Tuple

from src.utils.decorators import tratar_excecoes
from src.utils.enum_categoria_cliente import CategoriaCliente
from src.model.cliente import Cliente
from src.model.vendedor import Vendedor
from src.view.tela_gui_relatorio import TelaRelatorio


class ControladorRelatorio(AbstractControlador):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__tela_relatorio = TelaRelatorio()
        self.controlador_clientes = controlador_sistema.controlador_clientes
        self.controlador_vendedores = controlador_sistema.controlador_vendedores
        self.controlador_produtos = controlador_sistema.controlador_produtos
        self.controlador_vendas = controlador_sistema.controlador_vendas

    @tratar_excecoes
    def abre_tela(self):
        lista_opcoes = {
            1: self.ultima_compra_cliente,
            2: self.ultima_venda_vendedor,
            3: self.exibir_relatorio_por_tipo_cliente,
            4: self.exibir_relatorio_por_dia,
            0: self.retornar,
        }

        while True:
            escolha = self.__tela_relatorio.menu(list(lista_opcoes.keys()))
            if escolha in lista_opcoes:
                lista_opcoes[escolha]()
            else:
                print("Opção inválida. Tente novamente.")

    @tratar_excecoes
    def ultima_compra_cliente(self):
        cliente_relatorio = self.controlador_clientes.busca_cliente()
        if not cliente_relatorio:
            self.__tela_relatorio.exibir_mensagem("Cliente não encontrado.")
            return []

        vendas = self.controlador_vendas.vendas
        vendas_cliente = [venda for venda in vendas if venda.cliente.cpf == cliente_relatorio.cpf]

        if not vendas_cliente:
            self.__tela_relatorio.exibir_mensagem("Nenhuma compra encontrada para este cliente.")
            return []

        vendas_cliente.sort(key=lambda venda: venda.data_venda, reverse=True)
        ultima_compra = vendas_cliente[0].to_dict()

        ultima_compra = self.busca_dados_produtos(ultima_compra)

        # Exibir detalhes da última compra
        self.__tela_relatorio.exibir_ultima_compra(ultima_compra)
        return ultima_compra['produtos']

    @tratar_excecoes
    def ultima_venda_vendedor(self):
        vendedor_relatorio = self.controlador_vendedores.busca_vendedor()
        if not vendedor_relatorio:
            self.__tela_relatorio.exibir_mensagem("Vendedor não encontrado.")
            return []

        vendas = self.controlador_vendas.vendas
        vendas_vendedor = [venda for venda in vendas if venda.vendedor.cpf == vendedor_relatorio.cpf]

        if not vendas_vendedor:
            self.__tela_relatorio.exibir_mensagem("Nenhuma venda encontrada para este vendedor.")
            return []

        vendas_vendedor.sort(key=lambda venda: venda.data_venda, reverse=True)
        ultima_venda = vendas_vendedor[0].to_dict()

        ultima_venda = self.busca_dados_produtos(ultima_venda)

        # Exibir detalhes da última compra
        self.__tela_relatorio.exibir_ultima_venda(ultima_venda)
        return ultima_venda['produtos']

    def busca_dados_produtos(self, venda) -> dict:
        for produto in venda['produtos']:
            produto_detalhado = self.controlador_produtos.pesquisa_produto(produto['codigo_produto'])
            if produto_detalhado:
                produto["nome"] = produto_detalhado.nome
            else:
                produto["nome"] = "Produto não encontrado"
        return venda

    @tratar_excecoes
    def exibir_relatorio_por_tipo_cliente(self):
        relatorio = {categoria: [] for categoria in CategoriaCliente}
        for venda in self._controlador_sistema.controlador_vendas.vendas:
            cliente_categoria = venda.cliente.categoria
            relatorio[cliente_categoria].append(venda.to_dict())

        self.__tela_relatorio.mostrar_relatorio_por_tipo_cliente(relatorio)

    @tratar_excecoes
    def exibir_relatorio_por_dia(self):
        vendas_por_dia = {}
        for venda in self._controlador_sistema.controlador_vendas.vendas:
            if venda.data_venda not in vendas_por_dia:
                vendas_por_dia[venda.data_venda] = []
            vendas_por_dia[venda.data_venda].append(venda.to_dict())

        dias = list(vendas_por_dia.keys())
        opcao_dia = self.__tela_relatorio.selecionar_dia_relatorio(dias)
        vendas_no_dia = vendas_por_dia.get(opcao_dia, [])
        self.__tela_relatorio.mostrar_relatorio_por_dia(opcao_dia, vendas_no_dia)

    def mostrar_erro(self, e: str):
        self.__tela_relatorio.mostrar_erro(e)
