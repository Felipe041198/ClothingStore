from src.model.pessoa import Pessoa


class Vendedor(Pessoa):

    def __init__(self, cpf: str, nome: str, data_nasc: str, codigo: int, salario: float):
        super().__init__(cpf, nome, data_nasc, codigo)
        if isinstance(salario, float):
            self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        if isinstance(salario, float) and salario > 0:
            self.__salario = salario
        elif salario <= 0:
            raise ValueError("Salário deve ser maior que zero.")
        else:
            raise ValueError("Salário inválido")

    def to_dict(self):
        return {
            "cpf": self.cpf,
            "nome": self.nome,
            "data_nasc": self.data_nasc,
            "codigo": self.codigo,
            "salario": self.__salario
        }
