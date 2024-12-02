from datetime import date

from src.mocks.cliente_mock import cliente1, cliente2, cliente4
from src.mocks.produtos_mock import produto1, produto2, produto3, produto4, produto5
from src.mocks.vendedores_mock import vendedor1, vendedor3, vendedor2
from src.model.venda import Venda

item_camiseta = {"codigo" : produto1.codigo, "quantidade" : 2, "preco" : produto1.preco}
item_calca_jeans = {"codigo" : produto2.codigo, "quantidade" : 3, "preco" : produto2.preco}
item_jaqueta = {"codigo" : produto3.codigo, "quantidade" : 1, "preco" : produto3.preco}
item_vestido = {"codigo" : produto4.codigo, "quantidade" : 2, "preco" : produto4.preco}
item_blusa_trico = {"codigo" : produto5.codigo, "quantidade" : 2, "preco" : produto5.preco}

venda1 = Venda(cliente1, vendedor1, date(2024, 11, 3))
venda1.adiciona_items([item_camiseta, item_jaqueta])

venda2 = Venda(cliente2, vendedor3, date(2024, 11, 3))
venda2.adiciona_items([item_calca_jeans, item_vestido])

venda3 = Venda(cliente1, vendedor3, date(2024, 10, 20))
venda3.adiciona_items([item_jaqueta])

venda4 = Venda(cliente4, vendedor2, date(2024, 10, 5))
venda4.adiciona_items([item_blusa_trico, item_camiseta])

lista_vendas_mock = [
    venda1, venda2, venda3, venda4
]
