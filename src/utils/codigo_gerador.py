

class GeradorCodigo:
    def __init__(self):
        self.contador = 0

    def gerar_codigo(self, tipo: str) -> int:
        try:
            if tipo.lower() == "vendedor":
                primeiro_digito = "1"
            elif tipo.lower() == "cliente":
                primeiro_digito = "2"
            else:
                raise ValueError("Tipo inválido. Use 'vendedor' ou 'cliente'.")

            while True:
                codigo = int(primeiro_digito + f"{self.contador:04d}")
                self.contador += 1
                return codigo
        except ValueError as e:
            print(f"Erro: {e}")
            return None
