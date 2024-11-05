from datetime import datetime
from src.model.cliente import Cliente
from src.model.vendedor import Vendedor
from src.model.produto import Produto
from src.model.item_venda import ItemVenda
from src.model.venda import Venda

# Mock de clientes
cliente1 = Cliente(11466534680, "Felipe Vieira", "04/11/1998", 1)
cliente2 = Cliente(35922540068, "Cliente teste 1", "01/01/1999", 1)
cliente3 = Cliente(222, "Cliente teste 2", "02/02/2002", 2)
cliente4 = Cliente(61497778042, "Cliente teste 3", "03/03/2003", 2)

# Mock de vendedores
vendedor1 = Vendedor(1111, "Vendedor 1", "01/01/1999", 1001, 3000.0)
vendedor2 = Vendedor(98765432100, "Vendedor 2", "15/05/1985", 1002, 3500.0)

# Mock de produtos
produto1 = Produto(1, "Camiseta", "Camiseta de algodão", "M", "Azul", 29.90)
produto2 = Produto(2, "Calça Jeans", "Calça jeans azul", "G", "Azul", 29.90)
produto3 = Produto(3, "Tênis", "Tênis esportivo", "42", "Preto", 120.0)
produto4 = Produto(4, "Jaqueta", "Jaqueta de inverno", "M", "Preto", 150.0)

# Mock de vendas com diferentes itens e quantidades
item_venda1 = ItemVenda(produto1.nome, 2, 29.90)  # 2 Camisetas
item_venda2 = ItemVenda(produto2.nome, 1, 29.90)  # 1 Calça Jeans
item_venda3 = ItemVenda(produto3.nome, 3, 120.0)  # 3 Tênis
item_venda4 = ItemVenda(produto4.nome, 1, 150.0)  # 1 Jaqueta

# Mock de vendas
venda1 = Venda(cliente1, vendedor1, [item_venda1, item_venda2], datetime(2024, 11, 3))
venda2 = Venda(cliente2, vendedor2, [item_venda3], datetime(2024, 11, 3))
venda3 = Venda(cliente3, vendedor1, [item_venda4, item_venda1], datetime(2024, 10, 20))
venda4 = Venda(cliente1, vendedor2, [item_venda2, item_venda3, item_venda4], datetime(2024, 10, 5))

# Lista de vendas mock
lista_vendas_mock = [venda1, venda2, venda3, venda4]
