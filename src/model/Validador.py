from datetime import datetime

class Validador:
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
    def validar_data_nascimento(data_nasc):
        try:
            data = datetime.strptime(data_nasc, '%d/%m/%Y').date()
            if data > datetime.today().date():
                raise ValueError("Data inválida!")
            return data
        except ValueError:
            raise ValueError("Data inválida!")

    @staticmethod
    def validar_nome(nome: str):
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("Nome inválido!")

    @staticmethod
    def validar_endereco(endereco: str):
        if not isinstance(endereco, str) or not endereco.strip():
            raise ValueError("Endereço inválido!")
