from src.controller.abstract_controlador import AbstractControlador
from src.model.venda import Venda
from datetime import datetime, timedelta
from typing import List, Optional, Tuple

from src.utils.decorators import tratar_excecoes
from src.utils.enum_categoria_cliente import CategoriaCliente
from src.view.tela_relatorio import TelaRelatorio
from src.model.cliente import Cliente
from src.model.vendedor import Vendedor


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
            escolha = self.__tela_relatorio.menu_principal(list(lista_opcoes.keys()))
            if escolha in lista_opcoes:
                lista_opcoes[escolha]()
            else:
                print("Opção inválida. Tente novamente.")

    def selecionar_periodo(self) -> Optional[Tuple[Optional[datetime], Optional[datetime]]]:
        periodo_opcoes = {
            1: ("Últimas 24 horas", datetime.now() - timedelta(days=1)),
            2: ("Últimos 7 dias", datetime.now() - timedelta(days=7)),
            3: ("Últimos 15 dias", datetime.now() - timedelta(days=15)),
            4: ("Último mês", datetime.now() - timedelta(days=30)),
            5: ("Visualizar todos os registros", None),
            0: self.retornar,
        }

        escolha_periodo = self.__tela_relatorio.menu_periodo(list(periodo_opcoes.keys()))
        if escolha_periodo == 0:
            return None, None
        descricao, data_inicial = periodo_opcoes.get(escolha_periodo, (None, None))
        if escolha_periodo == 5:
            return None, None

        data_final = datetime.now()

        return data_inicial, data_final

    # Temporariamente desativada
    def gerar_relatorio_vendas(self):
        # Busca cliente e vendedor
        cliente = self.controlador_clientes.busca_cliente()
        vendedor = self.controlador_vendedores.busca_vendedor()
        data_inicial, data_final = self.selecionar_periodo()

        # Recupera todas as vendas
        vendas = self.controlador_vendas.listar_vendas()

        # Filtra vendas por data
        relatorio_vendas = [
            venda for venda in vendas
            if (data_inicial is None or venda.data_venda >= data_inicial)
            and (data_final is None or venda.data_venda <= data_final)
        ]

        # Filtra por cliente, se um cliente foi encontrado
        if cliente:
            relatorio_vendas = [
                venda for venda in relatorio_vendas
                if venda.cliente.cpf == cliente.cpf  # ou outra lógica de comparação se necessário
            ]

        # Filtra por vendedor, se um vendedor foi encontrado
        if vendedor:
            relatorio_vendas = [
                venda for venda in relatorio_vendas
                if venda.vendedor.cpf == vendedor.cpf  # ou outra lógica de comparação se necessário
            ]

        # Calcula o total das vendas no período filtrado
        total_vendas_periodo = sum(venda.valor_total for venda in relatorio_vendas)

        relatorio = {
            'total_vendas_periodo': total_vendas_periodo,
            'vendas': []
        }

        # Monta o relatório com os dados das vendas filtradas
        for venda in relatorio_vendas:
            cliente = venda.cliente
            vendedor = venda.vendedor

            produtos = [
                {
                    'codigo': produto.codigo,
                    'nome': produto.nome,
                    'quantidade': produto.quantidade,
                    'valor': produto.valor_total
                } for produto in venda.produtos
            ]

            relatorio['vendas'].append({
                'data_venda': venda.data_venda,
                'cliente_nome': cliente.nome if cliente else 'Desconhecido',
                'cliente_cpf': cliente.cpf if cliente else 'Desconhecido',
                'vendedor_nome': vendedor.nome if vendedor else 'Desconhecido',
                'vendedor_cpf': vendedor.cpf if vendedor else 'Desconhecido',
                'produtos': produtos,
                'valor_total': venda.valor_total
            })

        # Mostra o relatório final
        self.__tela_relatorio.mostrar_relatorio_vendas(relatorio)

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
        ultima_compra = vendas_cliente[0]

        # Exibir detalhes da última compra
        self.__tela_relatorio.exibir_ultima_compra(ultima_compra)
        return ultima_compra.produtos

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
        ultima_venda = vendas_vendedor[0]

        # Exibir detalhes da última compra
        self.__tela_relatorio.exibir_ultima_compra(ultima_venda)
        return ultima_venda.produtos

    def gerar_relatorio_completo(self, cliente: Optional[Cliente] = None,
                                 vendedor: Optional[Vendedor] = None) -> List[Venda]:
        vendas = self.controlador_vendas.listar_vendas()
        if cliente:
            return [venda for venda in vendas if venda.cliente.cpf == cliente.cpf]
        elif vendedor:
            return [venda for venda in vendas if venda.vendedor.cpf == vendedor.cpf]
        return vendas

    @tratar_excecoes
    def exibir_relatorio_por_tipo_cliente(self):
        relatorio = {categoria: [] for categoria in CategoriaCliente}
        for venda in self._controlador_sistema.controlador_vendas.vendas:
            cliente_categoria = venda.cliente.categoria
            relatorio[cliente_categoria].append(venda)

        self.__tela_relatorio.mostrar_relatorio_por_tipo_cliente(relatorio)

    @tratar_excecoes
    def exibir_relatorio_por_dia(self):
        vendas_por_dia = {}
        for venda in self._controlador_sistema.controlador_vendas.vendas:
            if venda.data_venda not in vendas_por_dia:
                vendas_por_dia[venda.data_venda] = []
            vendas_por_dia[venda.data_venda].append(venda)

        dias = list(vendas_por_dia.keys())
        opcao_dia = self.__tela_relatorio.selecionar_dia_relatorio(dias)
        vendas_no_dia = vendas_por_dia.get(opcao_dia, [])
        self.__tela_relatorio.mostrar_relatorio_por_dia(opcao_dia, vendas_no_dia)
