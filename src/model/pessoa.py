from abc import ABC, abstractmethod


class Pessoa(ABC):

    @abstractmethod
    def __init__(self, cpf: str, nome: str, data_nasc: str, codigo: int):
        self.__cpf = None
        self.__nome = None
        self.__data_nasc = None
        self.__codigo = None
        if isinstance(cpf, str):
            self.__cpf = cpf
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(data_nasc, str):
            self.__data_nasc = data_nasc
        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        if isinstance(cpf, str):
            self.__cpf = cpf

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def data_nasc(self) -> str:
        return self.__data_nasc

    @data_nasc.setter
    def data_nasc(self, data_nasc):
        if isinstance(data_nasc, str):
            self.__data_nasc = data_nasc

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, int):
            self.__codigo = codigo
