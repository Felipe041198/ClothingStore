from src.view.abstract_tela_registro import AbstractTelaRelatorio
from src.utils.enum_tipo_cadastro import TipoCadastro


class TelaRelatorio(AbstractTelaRelatorio):
    def __init__(self, controlador_relatorio):
        super().__init__(tipo_cadastro=TipoCadastro.PEDIDO)
        self.controlador_relatorio = controlador_relatorio

    def exibir_mensagem(self, mensagem: str):
        print(mensagem)

    def exibir_ultima_compra(self, venda):
        """Exibe os detalhes da última compra."""
        cliente = venda.cliente
        print(f"--- Última Compra ---")
        print(f"Cliente: {cliente.nome}")
        print(f"CPF: {cliente.cpf}")
        print(f"Data da Venda: {venda.data_venda.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Produtos Comprados:")

        for produto in venda.produtos:
            print(
                f"- (Código: {produto.codigo_produto}, Quantidade: {produto.quantidade}, Valor: R$ {produto.valor_total:.2f})")

        print(f"Valor Total: R$ {venda.valor_total:.2f}")

    def mostrar_relatorio_vendas(self, periodo="total", data_inicial=None, data_final=None):
        relatorio = self.controlador_relatorio.gerar_relatorio_vendas(periodo, data_inicial, data_final)

        print("Relatório de Vendas:")
        print(f"Total de Vendas no Período: R${relatorio['total_vendas_periodo']:.2f}\n")

        if not relatorio['vendas']:
            print("Nenhuma venda encontrada para o período especificado.")
            return

        for venda in relatorio['vendas']:
            print(f"Data: {venda['data_venda'].strftime('%d/%m/%Y')}")
            print(f"Cliente: {venda['cliente_nome']} (CPF: {venda['cliente_cpf']})")
            print(f"Vendedor: {venda['vendedor_nome']} (CPF: {venda['vendedor_cpf']})")
            print("Produtos:")
            for produto in venda['produtos']:
                print(f"    - Código: {produto['codigo']}, Nome: {produto['nome']}, "
                      f"Quantidade: {produto['quantidade']}, Valor: R${produto['valor']:.2f}")
            print(f"Total da Venda: R${venda['valor_total']:.2f}\n")
