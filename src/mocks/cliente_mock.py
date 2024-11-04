from src.model.cliente import Cliente
from src.utils.enum_categoria_cliente import CategoriaCliente

cliente1 = Cliente("11466534680", "Felipe Vieira", "04/11/1998", CategoriaCliente.NORMAL, 1)
cliente2 = Cliente("35922540068", "Cliente teste 1", "01/01/1999", CategoriaCliente.PREMIUM, 2)
cliente3 = Cliente("222", "Cliente teste 2", "02/02/2002", CategoriaCliente.NORMAL, 3)
cliente4 = Cliente("61497778042", "Cliente teste 3", "03/03/2003", CategoriaCliente.PREMIUM, 4)

lista_clientes_mock = [
    cliente1, cliente2, cliente3, cliente4
]
