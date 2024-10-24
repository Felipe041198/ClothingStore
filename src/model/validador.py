from datetime import datetime
import re


class Validador:
    @staticmethod
    def validar_cpf():
        while True:
            cpf = input("Digite o CPF: ")
            cpf = ''.join(filter(str.isdigit, cpf))
            if len(cpf) != 11:
                print("CPF inválido! Tente novamente.")
                continue

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
                print("CPF inválido! Tente novamente.")
                continue
            return cpf

    @staticmethod
    def validar_data_nascimento():
        while True:
            data_nasc = input("Digite a Data de Nascimento (dd/mm/aaaa): ")
            try:
                data = datetime.strptime(data_nasc, '%d/%m/%Y').date()
                if data > datetime.today().date():
                    print("Data inválida! Tente novamente.")
                    continue
                return data
            except ValueError:
                print("Data inválida! Tente novamente.")

    @staticmethod
    def validar_nome():
        while True:
            nome = input("Digite o Nome: ").strip()
            if not isinstance(nome, str) or not nome:
                print("Nome inválido! O nome não pode estar vazio. Tente novamente.")
                continue
         
            if not re.match(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$', nome):
                print("Nome inválido! O nome não pode conter números, sinais ou pontuação. Tente novamente.")
                continue
         
            if len(nome.split()) < 2:
                print("Nome inválido! Insira pelo menos dois nomes (nome e sobrenome). Tente novamente.")
                continue
            return nome

    @staticmethod
    def validar_endereco():
        while True:
            endereco = input("Digite o Endereço: ").strip()
            if not isinstance(endereco, str) or not endereco:
                print("Endereço inválido! Tente novamente.")
                continue
            return endereco
