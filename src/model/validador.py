from datetime import datetime
import re

#validador desativado temporativamente
class Validador:
    @staticmethod
    def validar_cpf(cpf = None):
        while True:
            if cpf is None:
                cpf = input("Digite o CPF: ")
            #try:
                #cpf = ''.join(filter(str.isdigit, cpf))
                #if len(cpf) != 11:
                #    print("CPF inválido! Tente novamente.")
                #    continue

                #soma = 0
                #for i in range(9):
                #    soma += int(cpf[i]) * (10 - i)
                #resto = soma % 11
                #digito1 = 0 if resto < 2 else 11 - resto

                #soma = 0
                #for i in range(10):
                #    soma += int(cpf[i]) * (11 - i)
                #resto = soma % 11
                #digito2 = 0 if resto < 2 else 11 - resto

                #if digito1 != int(cpf[9]) or digito2 != int(cpf[10]):
                #    print("CPF inválido! Tente novamente.")
                #    continue
            #except ValueError:
            #    print("Erro ao validar CPF!")
            return cpf

    @staticmethod
    def validar_data_nascimento(data_nasc = None):
        while True:
            if data_nasc is None:
                data_nasc = input("Digite a Data de Nascimento (dd/mm/aaaa): ")
            try:
                if '/' in data_nasc:
                    data = datetime.strptime(data_nasc, '%d/%m/%Y').date()
                else:
                    data = datetime.strptime(data_nasc, '%d%m%Y').date()
                if data > datetime.today().date():
                    print("Data inválida! A data de nascimento não pode ser no futuro.")
                    return False

                return data.strftime('%d/%m/%Y')
            except ValueError:
                print("Formato de data inválido! Use dd/mm/aaaa ou ddmmaaaa.")
                return False

    @staticmethod
    def validar_nome(nome = None):
        while True:
            if nome is None:
                nome = input("Digite o Nome: ").strip()
            #if not isinstance(nome, str) or not nome:
            #    print("Nome inválido! O nome não pode estar vazio. Tente novamente.")
            #    continue

            #if not re.match(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$', nome):
            #    print("Nome inválido! O nome não pode conter números, sinais ou pontuação. Tente novamente.")
            #    continue

            #if len(nome.split()) < 2:
            #    print("Nome inválido! Insira pelo menos dois nomes (nome e sobrenome). Tente novamente.")
            #    continue
            return nome.title()

    @staticmethod
    def validar_endereco(endereco = None):
        while True:
            if endereco is None:
                endereco = input("Digite o Endereço: ").strip()
            #if not isinstance(endereco, str) or not endereco:
            #    print("Endereço inválido! Tente novamente.")
            #    continue
            #if len(endereco.split()) < 2:
            #    print("Endereço inválido! Insira pelo menos duas palavras. Tente novamente.")
            #    continue
            return endereco.title()
