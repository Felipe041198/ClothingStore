import pickle


class DAOGeneric:
    def __init__(self, nome_dao: str):
        self.__arquivo = nome_dao + ".pkl"

    def salvar(self, dados):
        with open(self.__arquivo, 'wb') as file:
            pickle.dump(dados, file)

    def carregar(self):
        try:
            with open(self.__arquivo, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return []
