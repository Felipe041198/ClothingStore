class Produto:
    def __init__(self, codigo: int, nome: str, descricao: str, tamanho: str, cor: str, preco: float):
        self.__codigo = codigo
        self.__nome = nome
        self.__descricao = descricao
        self.__tamanho = tamanho
        self.__cor = cor
        self.__preco = preco

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        if not isinstance(codigo, int):
            raise TypeError("O código do produto deve ser um número inteiro.")
        self.__codigo = codigo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if not isinstance(nome,  str):
            raise TypeError("O nome do produto inválido.")
        self.__nome = nome

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        if not isinstance(descricao, str):
            raise TypeError("Descrição do produto inválida.")
        self.__descricao = descricao

    @property
    def tamanho(self):
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, tamanho):
        if not isinstance(tamanho, str):
            raise TypeError("Tamanho do produto inválido.")
        self.__tamanho = tamanho

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, cor:str):
        if not isinstance(cor, str):
            raise TypeError("Cor do produto inválida.")
        self.__cor = cor

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        if not isinstance(preco, (int, float)):
            raise TypeError("Preço do produto inválido.")
        if preco < 0:
            raise ValueError("O preço do produto não pode ser negativo.")
        self.__preco = preco
        
