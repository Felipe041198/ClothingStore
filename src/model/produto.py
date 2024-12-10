from src.exceptions.atributo_invalido_produto_exception import AtributoInvalidoProdutoException
from src.exceptions.produto_sem_estoque_exception import ProdutoSemEstoqueException


class Produto:
    def __init__(
            self,
            codigo: int,
            nome: str,
            descricao: str,
            tamanhos: list,
            cor: str,
            preco: float
    ):
        if not isinstance(tamanhos, list):
            raise TypeError("Os tamanhos devem ser fornecidos como uma lista.")
        if not set(tamanhos).issubset({'P', 'M', 'G'}):
            raise ValueError("Os tamanhos permitidos são apenas 'P', 'M' ou 'G'.")

        self.__codigo = codigo
        self.__nome = nome
        self.__descricao = descricao
        self.__tamanhos = tamanhos
        self.__cor = cor
        self.__preco = preco

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        if not isinstance(codigo, int):
            raise TypeError("O código do produto deve ser um número inteiro.")
        self.__codigo = codigo

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if not isinstance(nome, str):
            raise TypeError("O nome do produto inválido.")
        self.__nome = nome

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        if not isinstance(descricao, str):
            raise TypeError("Descrição do produto inválida.")
        self.__descricao = descricao

    @property
    def tamanhos(self) -> list:
        return self.__tamanhos

    @tamanhos.setter
    def tamanhos(self, tamanhos):
        if not all(isinstance(t, str) for t in tamanhos):
            raise TypeError("Todos os tamanhos devem ser strings.")
        if not set(tamanhos).issubset({'P', 'M', 'G'}):
            raise ValueError("Os tamanhos permitidos são apenas 'P', 'M' ou 'G'.")
        self.__tamanhos = tamanhos

    @property
    def cor(self) -> str:
        return self.__cor

    @cor.setter
    def cor(self, cor: str):
        if not isinstance(cor, str):
            raise TypeError("Cor do produto inválida.")
        self.__cor = cor

    @property
    def preco(self) -> float:
        return self.__preco

    @preco.setter
    def preco(self, preco):
        if not isinstance(preco, (int, float)):
            raise TypeError("Preço do produto inválido.")
        if preco < 0:
            raise ValueError("O preço do produto não pode ser negativo.")
        self.__preco = preco


    def to_dict(self):
        return {
            "codigo": self.__codigo,
            "nome": self.__nome,
            "descricao": self.__descricao,
            "tamanhos": self.__tamanhos,
            "cor": self.__cor,
            "preco": self.__preco
        }
