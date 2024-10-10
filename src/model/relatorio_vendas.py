from datetime import datetime, timedelta
from venda import Venda
from cliente import Cliente
from vendedor import Vendedor


class RelatorioVendas:

    def __init__(
            self,
            vendas: list[Venda],
            cliente=None,
            vendedor=None,
            inicio=None,
            fim=None
    ):
        self.__vendas = vendas
        self.__cliente = cliente
        self.__vendedor = vendedor
        self.__inicio = inicio
        self.__fim = fim
        self.__vendas = self.aplicar_filtros()

    @property
    def vendas(self):
        return self.__vendas

    @vendas.setter
    def vendas(self, vendas):
        if not isinstance(vendas, list):
            raise TypeError("Vendas inválidas.")
        self.__vendas = vendas

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        if cliente and not isinstance(cliente, Cliente):
            raise TypeError("O cliente inválido.")
        self.__cliente = cliente

    @property
    def vendedor(self):
        return self.__vendedor

    @vendedor.setter
    def vendedor(self, vendedor):
        if vendedor and not isinstance(vendedor, Vendedor):
            raise TypeError("O vendedor inválido")
        self.__vendedor = vendedor

    @property
    def inicio(self):
        return self.__inicio

    @inicio.setter
    def inicio(self, inicio):
        if inicio and not isinstance(inicio, datetime):
            raise TypeError("A data de início inválida.")
        self.__inicio = inicio

    @property
    def fim(self):
        return self.__fim

    @fim.setter
    def fim(self, fim):
        if fim and not isinstance(fim, datetime):
            raise TypeError("A data de fim inválida.")
        self.__fim = fim

    def aplicar_filtros(self):
        vendas_filtradas = self.__vendas

        if self.__cliente:
            vendas_filtradas = [venda for venda in vendas_filtradas if venda.cliente == self.__cliente]
        if self.__vendedor:
            vendas_filtradas = [venda for venda in vendas_filtradas if venda.vendedor == self.__vendedor]
        if self.__inicio or self.__fim:
            vendas_filtradas = self.filtrar_por_periodo(vendas_filtradas, self.__inicio, self.__fim)

        return vendas_filtradas

    # MÉTODOS DE RELATÓRIOS
    def filtrar_por_periodo(self, vendas, inicio=None, fim=None):
        if inicio and fim:
            return [venda for venda in vendas if inicio <= venda.data_venda <= fim]
        return vendas

    # Última compra por cliente ou vendedor
    def ultima_compra_cliente(self, cliente: Cliente):
        vendas_cliente = sorted(self.gerar_relatorio_completo(cliente=cliente), key=lambda x: x.data_venda,
                                reverse=True)
        return vendas_cliente[0].produtos if vendas_cliente else []

    def ultima_compra_vendedor(self, vendedor: Vendedor):
        vendas_vendedor = sorted(self.gerar_relatorio_completo(vendedor=vendedor), key=lambda x: x.data_venda,
                                 reverse=True)
        return vendas_vendedor[0].produtos if vendas_vendedor else []

    def valor_total(self):
        return sum(venda.valor_total for venda in self.__vendas)

    def gerar_relatorio_completo(self, cliente=None, vendedor=None, inicio=None, fim=None):
        vendas_filtradas = self.__vendas

        if cliente:
            vendas_filtradas = [venda for venda in vendas_filtradas if venda.cliente == cliente]
        if vendedor:
            vendas_filtradas = [venda for venda in vendas_filtradas if venda.vendedor == vendedor]
        if inicio and fim:
            vendas_filtradas = [venda for venda in vendas_filtradas if inicio <= venda.data_venda <= fim]

        return vendas_filtradas

    # FILTROS DE PERÍODOS ESPECÍFICOS
    def ultimos_15_dias(self):
        fim = datetime.now()
        inicio = fim - timedelta(days=15)
        return self.filtrar_por_periodo(self.__vendas, inicio, fim)

    def vendas_anuais(self, ano=None):
        ano = ano or datetime.now().year
        inicio = datetime(ano, 1, 1)
        fim = datetime(ano, 12, 31)
        return self.filtrar_por_periodo(self.__vendas, inicio, fim)

    def vendas_mensais(self, ano=None, mes=None):
        agora = datetime.now()
        ano = ano or agora.year
        mes = mes or agora.month
        inicio = datetime(ano, mes, 1)
        fim = datetime(ano, mes + 1, 1) - timedelta(seconds=1) \
            if mes < 12 else datetime(ano + 1, 1, 1) - timedelta(seconds=1)
        return self.filtrar_por_periodo(self.__vendas, inicio, fim)
