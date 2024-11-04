from src.mocks.cliente_mock import cliente1, cliente2, cliente4
from src.mocks.produtos_mock import produto1, produto2, produto3, produto4, produto5
from src.mocks.vendedores_mock import vendedor1, vendedor3, vendedor2
from src.model.item_venda import ItemVenda
from src.model.venda import Venda

item_camiseta = ItemVenda(produto1.codigo, 2, produto1.preco)
item_calca_jeans = ItemVenda(produto2.codigo, 3, produto2.preco)
item_jaqueta = ItemVenda(produto3.codigo, 1, produto3.preco)
item_vestido = ItemVenda(produto4.codigo, 2, produto4.preco)
item_blusa_trico = ItemVenda(produto5.codigo, 2, produto5.preco)

venda1 = Venda(cliente1, vendedor1, [item_camiseta, item_jaqueta])
venda2 = Venda(cliente2, vendedor3, [item_calca_jeans, item_vestido])
venda3 = Venda(cliente1, vendedor3, [item_jaqueta])
venda4 = Venda(cliente4, vendedor2, [item_blusa_trico, item_camiseta])

lista_vendas_mock = [
    venda1, venda2, venda3, venda4
]
