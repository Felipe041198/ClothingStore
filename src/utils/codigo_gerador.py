import random

class GeradorCodigo:
    def __init__(self):
        self.codigos_existentes = set()

    def gerar_codigo(self, tipo: str) -> int:
        try:
            if tipo.lower() == "vendedor":
                primeiro_digito = "1"
            elif tipo.lower() == "cliente":
                primeiro_digito = "2"
            else:
                raise ValueError("Tipo inválido. Use 'vendedor' ou 'cliente'.")

            while True:
                codigo = int(primeiro_digito + ''.join(str(random.randint(0, 9)) for _ in range(5)))
                if codigo not in self.codigos_existentes:
                    self.codigos_existentes.add(codigo)
                    return codigo
        except ValueError as e:
            print(f"Erro: {e}")
            return None

