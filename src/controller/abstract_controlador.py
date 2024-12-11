from abc import ABC, abstractmethod
from src.exceptions.valor_invalido_exception import ValorInvalidoException


class AbstractControlador(ABC):
    @abstractmethod
    def __init__(self, controlador_sistema) -> None:
        self._controlador_sistema = controlador_sistema

    def retornar(self):
        self._controlador_sistema.abre_tela()

    @abstractmethod
    def abre_tela(self):
        pass

    def validar_preco(self, preco: str) -> float:
        try:
            return float(preco)
        except ValueError:
            raise ValorInvalidoException("O valor fornecido para o preço é inválido. "
                                         "Por favor, insira um número.")
