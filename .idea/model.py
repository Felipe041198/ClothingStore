from datetime import datetime

class Pessoa:
    def __init__(self, cpf:int, nome:str, data_nasc:str, endereco: str):
        self.__cpf = self.validar_cpf(cpf)
        self.__nome = nome
        self.__data_nasc = self.converter_data(data_nasc) 
        self.__endereco = endereco

    @property
    def cpf(self):
        return self._cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome:str):
        self.validar_nome(nome)
        self.__nome = nome

    @property
    def data_nasc(self):
        return self.__data_nasc.strftime('%d/%m/%Y')

    @data_nasc.setter
    def data_nasc(self, data_nasc: str):
        self.__data_nasc = self.validar_data_nascimento(data_nasc)

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco:str):
        self.validar_endereco(endereco)
        self.__endereco = endereco

    def validar_data_nascimento(self, data_nasc: str):
        try:
            data = datetime.strptime(data_nasc, '%d/%m/%Y').date()
            if data > datetime.today().date():
                raise ValueError("Data inválida!")
            return data
        except ValueError:
            raise ValueError("Data de nascimento inválida!")

    @staticmethod
    def validar_cpf(cpf):
        cpf = ''.join(filter(str.isdigit, cpf))
        if len(cpf) != 11:
            raise ValueError("CPF inválido!")

        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
        resto = soma % 11
        digito1 = 0 if resto < 2 else 11 - resto

        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)
        resto = soma % 11
        digito2 = 0 if resto < 2 else 11 - resto

        if digito1 != int(cpf[9]) or digito2 != int(cpf[10]):
            raise ValueError("CPF inválido!")
        return cpf

    @staticmethod
    def validar_nome(nome: str):
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("Nome inválido!")

    @staticmethod
    def validar_endereco(endereco: str):
        if not isinstance(endereco, str) or not endereco.strip():
            raise ValueError("Endereço inválido!")

#cliente e vendedor herdam atributos de pessoa
class Cliente(Pessoa):
    def __init__(self, cpf:int, nome:str, data_nasc:str, endereco: str):
        super().__init__(cpf, nome, data_nasc, endereco)
        self.historico_compras = []


    def adicionar_compra(self, venda):
        self.historico_compras.append(venda)

    def consultar_historico(self):
        return self.historico_compras


class Vendedor(Pessoa):
    def __init__(self, cpf:int, nome:str, data_nasc:str, endereco: str, cargo:str):
        super().__init__(cpf, nome, data_nasc, endereco)
        self.cargo = cargo
        self.historico_vendas = []

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo: str):
        self.validar_cargo(cargo)
        self.__cargo = cargo

    def adicionar_venda(self, venda):
        self.historico_vendas.append(venda)

    def consultar_historico(self):
        return self.historico_vendas

    def validar_cargo(self, cargo: str):
        if not isinstance(cargo, str) or not cargo.strip():
            raise ValueError("Cargo inválido!")


class Produto:
    def __init__(self, codigo:int, nome: str, descricao:str, tamanho:str, cor:str, preco:float):
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.tamanho = tamanho
        self.cor = cor
        self.preco = preco


class Venda:
    def __init__(self, cliente:Cliente, vendedor: Vendedor, produtos:list, data_venda:str):
        self.cliente = cliente
        self.vendedor = vendedor
        self.produtos = produtos
        self.data_venda = data_venda
        self.data_venda = self.converter_data(data_venda)
        self.valor_total = self.calcular_total()

    def converter_data(self, data_str):
        return datetime.strptime(data_str, '%d/%m/%Y').date()

    def calcular_total(self):
        return sum(produto.preco for produto in self.produtos)
